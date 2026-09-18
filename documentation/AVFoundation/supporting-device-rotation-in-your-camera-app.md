# Supporting device rotation in your camera app

**Framework**: AVFoundation

Keep your camera preview and captured photos and video upright by applying the angles a rotation coordinator reports.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- Xcode 27.0+

#### Overview

A capture device’s sensor has a fixed physical orientation, and rotating the device doesn’t change it. Nothing in the capture pipeline compensates for the difference. Unless your app accounts for rotation, it shows a landscape preview and saves photos and movies that appear in landscape in the Photos app.

AVCam corrects both by adopting [`AVCaptureDevice.RotationCoordinator`](avcapturedevice/rotationcoordinator.md), which reports how far to rotate video from a camera to appear level with the horizon, relative to gravity rather than the level relative to the sensor.

A rotation coordinator only reports angles. Applying them is the app’s work, and AVCam gives that job to a `RotationObserver` object on the main actor. The observer sets the preview angle on the preview layer’s connection and publishes the capture angles to the `CaptureService` actor. For more information about the app’s design, see [`AVCam: Building a camera app`](avcam-building-a-camera-app.md).

#### Create a Coordinator for the Camera

AVCam handles rotation in a dedicated type so the capture service stays focused on configuring and running the capture session. The `RotationObserver` object owns the coordinator, the camera it monitors, and a weak reference to the layer that displays the preview:

```swift
@MainActor
final class RotationObserver {

    // An object that provides the horizon-level angles for the current device
    // and preview layer.
    private var coordinator: AVCaptureDevice.RotationCoordinator?
    private var observations = [NSKeyValueObservation]()

    // The camera to monitor, and the layer that displays its preview.
    private var device: AVCaptureDevice?
    private weak var previewLayer: AVCaptureVideoPreviewLayer?

    func setDevice(_ device: AVCaptureDevice) {
        self.device = device
        startObserving()
    }

    func setPreviewLayer(_ previewLayer: AVCaptureVideoPreviewLayer) {
        self.previewLayer = previewLayer
        startObserving()
    }
}
```

A rotation coordinator binds to one device for its lifetime; changing cameras means creating a new coordinator. The observer runs on the main actor because the rotation coordinator computes the preview angle from a layer’s position in a view hierarchy and delivers its updates on the main queue. The type doesn’t impose isolation itself—that’s the app’s choice rather than an API requirement.

Creating a coordinator needs only a device. The app has one as soon as it selects a camera, which keeps the media it writes level even before a preview appears.

#### Provide the Preview Layer

The preview layer belongs to the view hierarchy on the main actor, and the capture session runs on the `CaptureService` actor. The app’s `PreviewSource` and `PreviewTarget` protocols connect those two sides. One method hands the session to the preview view and passes the layer back to the rotation observer. The capture service creates the source off the main actor, which is why the type is `nonisolated` and only `connect(to:)` runs there:

```swift
nonisolated struct DefaultPreviewSource: PreviewSource {

    private let session: AVCaptureSession
    private let rotationObserver: RotationObserver

    @MainActor func connect(to target: PreviewTarget) {
        target.setSession(session)

        // Provide the layer to the rotation observer, and again when the layer
        // joins a window, because it has no position in a hierarchy until then.
        target.previewLayerDidMoveToWindow = { previewLayer in
            rotationObserver.setPreviewLayer(previewLayer)
        }
        rotationObserver.setPreviewLayer(target.previewLayer)
    }
}
```

The observer receives the layer twice because a coordinator measures the layer’s position in a view hierarchy. The `CameraPreview` structure conforms to [`UIViewRepresentable`](https://developer.apple.com/documentation/swiftui/uiviewrepresentable) and builds its view before the system installs it. At connection time the layer has no position to measure. The nested `PreviewView` class reports the layer again after it joins a window:

```swift
class PreviewView: UIView, PreviewTarget {

    var previewLayerDidMoveToWindow: (@MainActor (AVCaptureVideoPreviewLayer) -> Void)?

    override func didMoveToWindow() {
        super.didMoveToWindow()
        // A coordinator measures the layer's position in a view hierarchy,
        // which the layer only has after it joins a window.
        guard window != nil else { return }
        previewLayerDidMoveToWindow?(previewLayer)
    }
}
```

> ❗ **Important**: A rotation coordinator that an app creates with a `nil` preview layer never reports a preview angle, even after a layer becomes available. When the preview layer arrives, `RotationObserver` creates a new coordinator for the same device. The new coordinator replaces the one the observer already holds.

#### Observe the Rotation Angles

A coordinator publishes two angles: [`videoRotationAngleForHorizonLevelPreview`](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelpreview.md) and [`videoRotationAngleForHorizonLevelCapture`](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelcapture.md). Both describe the rotation that makes video level with the horizon. The preview angle also accounts for where the layer sits in the interface, which is why the two can differ. Each supports key-value observing and delivers its updates on the main queue. The observer reads both one time, and then registers a key-value observation on each property:

```swift
private func startObserving() {
    guard let device else { return }

    // Cancel the previous observations so that an angle for the previous
    // device can't arrive after the angles for this one.
    for observation in observations {
        observation.invalidate()
    }
    observations.removeAll()

    let coordinator = AVCaptureDevice.RotationCoordinator(device: device, previewLayer: previewLayer)
    self.coordinator = coordinator

    // Set the initial angles for the preview and the capture outputs.
    update(previewAngle: coordinator.videoRotationAngleForHorizonLevelPreview)
    update(captureAngle: coordinator.videoRotationAngleForHorizonLevelCapture)

    // Monitor future changes to both angles.
    observe(\.videoRotationAngleForHorizonLevelPreview, of: coordinator) { [weak self] angle in
        self?.update(previewAngle: angle)
    }
    observe(\.videoRotationAngleForHorizonLevelCapture, of: coordinator) { [weak self] angle in
        self?.update(captureAngle: angle)
    }
}
```

Reading both properties before observing them matters, because a key-value observation reports only later changes, not the value a property already has. An app that only observes shows a sideways preview until the first time someone rotates the device.

Both registrations go through one method, which stores the observation and applies each new angle:

```swift
// Monitors one of a coordinator's angles, applying each new value on the
// main queue, where a coordinator delivers its updates.
private func observe(
    _ keyPath: KeyPath<AVCaptureDevice.RotationCoordinator, CGFloat>,
    of coordinator: AVCaptureDevice.RotationCoordinator,
    apply: @escaping @MainActor (CGFloat) -> Void
) {
    observations.append(
        coordinator.observe(keyPath, options: .new) { _, change in
            guard let angle = change.newValue else { return }
            MainActor.assumeIsolated { apply(angle) }
        }
    )
}
```

Handling each change synchronously preserves the coordinator’s ordering, which is what makes a rapid sequence of rotations settle on the correct final angle. The handler already runs on the main queue, and the `MainActor.assumeIsolated(_:)` method asserts that isolation rather than awaiting it. Awaiting would defer the work to a later turn of the main actor. The method traps if the assumption is ever wrong.

#### Apply the Preview Angle

The preview angle belongs to the connection that feeds the preview layer:

```swift
// Rotates the camera preview.
private func update(previewAngle angle: CGFloat) {
    previewLayer?.connection?.videoRotationAngle = angle
}
```

The assignment is a single line because the observer already holds the layer and runs on the main actor. It’s a lightweight call to make, because an [`AVCaptureVideoPreviewLayer`](avcapturevideopreviewlayer.md) rotates its contents with a transform rather than rotating pixels.

#### Publish the Capture Angles

The observer sets the preview angle on a layer it already holds, but it can’t reach the capture outputs the same way. They belong to the capture session, which AVCam isolates to the `CaptureService` actor. The observer yields each new angle into an asynchronous sequence that the service consumes:

```swift
nonisolated let captureAngles: AsyncStream<CGFloat>
nonisolated private let continuation: AsyncStream<CGFloat>.Continuation

nonisolated init() {
    // Retain only the most recent angle.
    let (captureAngles, continuation) = AsyncStream<CGFloat>.makeStream(
        bufferingPolicy: .bufferingNewest(1)
    )
    self.captureAngles = captureAngles
    self.continuation = continuation
}

// Provides the angle to the capture service, which applies it to its output
// connections.
private func update(captureAngle angle: CGFloat) {
    continuation.yield(angle)
}
```

The outputs only care about the latest angle. A buffering policy of [`AsyncStream.Continuation.BufferingPolicy.bufferingNewest(_:)`](https://developer.apple.com/documentation/swift/asyncstream/continuation/bufferingpolicy/bufferingnewest(_:)) keeps that one and drops the rest. Rotate the device a few times while the session reconfigures and the capture service still ends up with the latest angle instead of a backlog of stale ones.

#### Apply the Angle to the Outputs

The capture service consumes the sequence from a single task, stores each angle it receives, and applies it to every output:

```swift
actor CaptureService {

    // The most recent angle to apply to the video connection of each capture output.
    private var captureRotationAngle = CGFloat.zero

    // The task that applies the angles the rotation observer provides.
    private var rotationTask: Task<Void, Never>?

    private func observeRotationChanges() {
        // Hold `self` weakly, because the stream stays open for as long as the
        // observer lives.
        let captureAngles = rotationObserver.captureAngles
        rotationTask = Task { [weak self] in
            for await angle in captureAngles {
                guard let self else { break }
                await self.setCaptureRotationAngle(angle)
            }
        }
    }

    // Store the angle the rotation observer provides, then apply it to the
    // current outputs.
    private func setCaptureRotationAngle(_ angle: CGFloat) {
        captureRotationAngle = angle
        applyCaptureRotationAngle()
    }

    // Apply the current rotation angle to the video connection of each capture output.
    private func applyCaptureRotationAngle() {
        for service in outputServices {
            service.setVideoRotationAngle(captureRotationAngle)
        }
    }
}
```

The sequence stays open for as long as the observer lives, and capturing `self` strongly would keep the service alive that whole time. The task holds `self` weakly instead, and the service reads the sequence into a local constant so the body never needs `self` to reach it. A weak capture also puts the body outside the actor’s isolation, which is why it awaits `setCaptureRotationAngle(_:)` rather than assigning `captureRotationAngle` directly. Keeping the task in a property provides a reference that the service can cancel.

Each of the app’s output services applies the angle to its own output’s video connection:

```swift
extension OutputService {
    func setVideoRotationAngle(_ angle: CGFloat) {
        // Set the rotation angle on the output object's video connection.
        output.connection(with: .video)?.videoRotationAngle = angle
    }
}
```

Neither output rotates pixels to honor the angle: an [`AVCaptureMovieFileOutput`](avcapturemoviefileoutput.md) records it in a QuickTime track matrix, and an [`AVCapturePhotoOutput`](avcapturephotooutput.md) in Exif tags.

#### Keep New Outputs in Sync

Adding an output connects it to the session with a default rotation angle. After the first angle arrives, any output the app adds still starts at that default rather than the current angle. Switching between photo and video capture is where this occurs in AVCam, because it removes one output and adds another while the session runs. The method that adds an output applies the stored angle every time:

```swift
private func addOutput(_ output: AVCaptureOutput) throws {
    if captureSession.canAddOutput(output) {
        captureSession.addOutput(output)
        // Adding an output connects it with a default rotation angle, so
        // apply the current one.
        applyCaptureRotationAngle()
    } else {
        throw CameraError.addOutputFailed
    }
}
```

## See Also

- [Choosing a capture device](choosing-a-capture-device.md)
  Select the front or back camera, or use advanced features like the TrueDepth camera or dual camera.
- [Adopting smart framing in your camera app](adopting-smart-framing-in-your-camera-app.md)
  Capture the optimal shot by providing automatic framing recommendations.
- [class AVCaptureDevice](avcapturedevice.md)
  An object that represents a hardware or virtual capture device like a camera or microphone.
- [class AVCaptureDeviceInput](avcapturedeviceinput.md)
  An object that provides media input from a capture device to a capture session.
- [class AVContinuityDevice](avcontinuitydevice.md)
  A class that represents a physical iOS device that’s nearby and can provide access to its cameras and microphones.
- [class AVExternalStorageDevice](avexternalstoragedevice.md)
  Represents a physical external storage device that stores media assets.
- [class AVExternalStorageDeviceDiscoverySession](avexternalstoragedevicediscoverysession.md)
  Informs your app when the external storage devices connect to and disconnect from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/supporting-device-rotation-in-your-camera-app)*