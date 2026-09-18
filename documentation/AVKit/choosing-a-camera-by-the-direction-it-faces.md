# Choosing a camera by the direction it faces

**Framework**: AVKit

Find out which way each camera faces, and follow the change as someone opens and closes the device.

#### Overview

On an iPhone with one display, each camera faces a single direction. The front camera faces the same way as the display, the rear cameras face the opposite way, and their direction is a fixed property of the device. iPhone Duo has a display on each side and a camera above each one, so which way a camera faces depends on the display your app appears on. Opening or closing the device moves your app to the other display, and a camera that faced the same way as your interface now faces the opposite way.

The following illustrations show the same device in three configurations, drawn in the same place in each. An orange arrow marks a camera that faces forward, and a blue arrow marks one that faces backward:

**Closed**:

![An illustration that shows the device closed, with the outer display facing the reader. An orange arrow from the camera above that display points toward the reader, and a blue arrow points away from it.](/images/com.apple.avkit/camera-direction-closed-outer@2x.png)

**Open**:

![An illustration that shows the device open, with the inner display facing the reader. An orange arrow from the camera above that display points toward the reader, and two blue arrows point away from the cameras on the far side.](/images/com.apple.avkit/camera-direction-open-inner@2x.png)

**Open, turned around**:

![An illustration that shows the device open and turned around, with the rear cameras on the left panel and the outer display on the right. An orange arrow from the rear cameras and an orange arrow from the camera above the outer display both point toward the reader, and a blue arrow points away.](/images/com.apple.avkit/camera-direction-open-outer@2x.png)

Use [`AVCaptureDeviceDirectionCoordinator`](avcapturedevicedirectioncoordinator.md) to find out which way each camera faces right now. A coordinator takes the view that shows your preview as its frame of reference. It groups the cameras that you capture from into the ones that face forward, meaning the same way as that view, and the ones that face backward. Each time that grouping changes, the coordinator tells your app, which can then switch to a camera that faces forward. A rear camera can be the forward-facing one, which is how someone takes a selfie with it.

The [`position`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/position-swift.property) property describes where a camera sits in relation to the device’s display. On an iPhone with one display, that location also tells you which way the camera points. On iPhone Duo, position still reports where a camera sits, and the coordinator reports which way it faces.

#### Start From the Virtual Front Camera

Continue to discover cameras the way your app already does, with an [`AVCaptureDevice.DiscoverySession`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/discoverysession) that specifies your device types and the front position. On iPhone Duo, the [`builtInWideAngleCamera`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtinwideanglecamera) and [`builtInUltraWideCamera`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtinultrawidecamera) types return the virtual front camera. It streams from the camera above the display your app appears on, and it follows your app as someone opens and closes the device.

The system moves between the two physical cameras, so an app that captures from the front camera today works unchanged. The virtual front camera is a virtual device, so [`isVirtualDevice`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isvirtualdevice) is `true` and code that already handles the dual camera handles this one too. Query its [`activePrimaryConstituent`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activeprimaryconstituent) property to determine which camera is streaming.

The following example finds the front camera, and reports the physical camera it’s streaming from:

```swift
final class DeviceLookup {

    // On iPhone Duo, these device types return the virtual front camera.
    private let frontCameraDiscoverySession = AVCaptureDevice.DiscoverySession(
        deviceTypes: [.builtInWideAngleCamera, .builtInUltraWideCamera],
        mediaType: .video,
        position: .front
    )

    // The front camera to capture from, which is the virtual front camera on a device that has one.
    var frontCamera: AVCaptureDevice? {
        frontCameraDiscoverySession.devices.first
    }

    // The physical camera a virtual front camera streams from; this is `nil` until the session runs.
    func streamingCamera(for camera: AVCaptureDevice) -> AVCaptureDevice? {
        camera.isVirtualDevice ? camera.activePrimaryConstituent : camera
    }
}
```

The virtual front camera provides a good starting point for an existing app. It switches between the two physical cameras as someone opens and closes the device, and your app captures from it like any front camera. Its capabilities are the ones both cameras have in common, and the system decides which one streams.

Capture from the two physical cameras when capture is your app’s main job. The [`builtInOuterUltraWideCamera`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtinouterultrawidecamera) and [`builtInInnerUltraWideCamera`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtininnerultrawidecamera) types provide everything each camera can do. Following the direction they face becomes your app’s work, and a coordinator reports it.

#### Create a Direction Coordinator for Your Preview

Create an [`AVCaptureDeviceDirectionCoordinator`](avcapturedevicedirectioncoordinator.md) object to monitor the direction your cameras face. Pass it the view that shows your preview, the device types your app captures from, and a change handler that responds as the direction changes. The view is the coordinator’s frame of reference rather than something it draws into.

Specify every built-in camera your app captures from, including its rear cameras. A rear camera can face forward on iPhone Duo. A coordinator reports only the built-in types you list, and listing an external camera, Continuity Camera, or Desk View camera has no effect. It also leaves out the virtual front camera, because the system moves it for you. List the two physical front cameras, [`builtInOuterUltraWideCamera`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtinouterultrawidecamera) and [`builtInInnerUltraWideCamera`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtininnerultrawidecamera), in its place.

> ❗ **Important**: Create the coordinator and handle its updates on the main actor. It reports the direction cameras face in relation to a view, which is main-actor state.

The following example creates the coordinator in a main actor observer, and installs a method as its change handler:

```swift
import AVKit

@MainActor
final class DirectionObserver {

    // A Swift actor that manages the capture pipeline.
    private let captureService: CaptureService
    private var coordinator: AVCaptureDeviceDirectionCoordinator?
    private var activeCameraDescriptor: AVCaptureDeviceDescriptor?

    init(captureService: CaptureService) {
        self.captureService = captureService
    }

    func startObserving(previewView: UIView) {
        coordinator = AVCaptureDeviceDirectionCoordinator(
            view: previewView,
            deviceTypes: [
                .builtInOuterUltraWideCamera,
                .builtInInnerUltraWideCamera,
                .builtInDualWideCamera,
            ]
        ) { [weak self] deviceDirections in
            self?.cameraDirectionsDidChange(deviceDirections)
        }
    }
}
```

Hold a strong reference to the coordinator for as long as its view stays onscreen. A coordinator reports directions in relation to one view, so an app that shows a preview on both displays creates a coordinator for each one. The same rear camera then comes back as forward facing from one coordinator and backward facing from the other.

#### Respond to a Change in Camera Direction

The coordinator calls your change handler on the main actor, soon after you create it and again on every change. The first call passes the directions in effect at that moment, so your app reads the starting configuration without a separate step. Until that call arrives, [`deviceDirections`](avcapturedevicedirectioncoordinator/devicedirections.md) returns an empty map.

Both the property and the handler report an [`AVCaptureDeviceDirectionMap`](avcapturedevicedirectionmap.md), which provides a [`forwardFacingDeviceDescriptors`](avcapturedevicedirectionmap/forwardfacingdevicedescriptors.md) array and a [`backwardFacingDeviceDescriptors`](avcapturedevicedirectionmap/backwardfacingdevicedescriptors.md) array. The forward-facing array holds the cameras that face the same way as your view, which isn’t the same as the cameras whose position is front. A camera your app treats as a rear camera appears there after a person opens or closes the device, which is how your app captures a selfie from that camera.

Compare the camera you’re capturing from against the forward-facing array rather than assuming it still faces the right way. When it no longer appears there, choose a replacement from the array.

The following example implements the change handler that the previous example installed, and hands a replacement camera to the capture actor:

```swift
extension DirectionObserver {

    func cameraDirectionsDidChange(_ deviceDirections: AVCaptureDeviceDirectionMap) {
        let forwardFacing = deviceDirections.forwardFacingDeviceDescriptors

        // Keep the active camera if it still faces forward.
        if let activeCameraDescriptor, forwardFacing.contains(activeCameraDescriptor) { return }

        guard let replacement = forwardFacing.first else {
            // No camera faces forward in this configuration.
            return
        }

        activeCameraDescriptor = replacement
        Task { try await captureService.selectCamera(with: replacement) }
    }
}
```

Reconfigure a single video input rather than connecting both cameras in a multicamera session. Reconfiguring one input costs less, and it covers what most apps need.

#### Create a Capture Device From a Descriptor

The coordinator reports each camera as an [`AVCaptureDeviceDescriptor`](avcapturedevicedescriptor.md), which provides the identifying properties of a capture device. A descriptor provides the camera’s `deviceType`, `mediaTypes`, `position`, `uniqueID`, and `localizedName`, so your app can get the defining characteristics of a camera without touching the capture system.

Descriptors and direction maps are both [`Sendable`](https://developer.apple.com/documentation/swift/sendable), which lets your app read them on the main actor and create the device somewhere else. Creating and configuring an [`AVCaptureDevice`](https://developer.apple.com/documentation/avfoundation/avcapturedevice) calls into the capture system, and that work belongs on the actor that owns your capture session.

> ❗ **Important**: Don’t call AVFoundation from the change handler. Pass the descriptor to the actor that owns your session, then resolve it and reconfigure there.

The following example resolves a descriptor into a device, and replaces the session’s video input:

```swift
actor CaptureService {

    private let captureSession = AVCaptureSession()
    private var activeVideoInput: AVCaptureDeviceInput?

    func selectCamera(with descriptor: AVCaptureDeviceDescriptor) throws {
        guard let device = AVCaptureDevice(uniqueID: descriptor.uniqueID) else {
            // The set of cameras changed again while dispatching.
            return
        }

        let newInput = try AVCaptureDeviceInput(device: device)

        captureSession.beginConfiguration()
        defer { captureSession.commitConfiguration() }

        if let activeVideoInput {
            captureSession.removeInput(activeVideoInput)
        }

        guard captureSession.canAddInput(newInput) else {
            // Restore the previous input if the new one doesn't fit the configuration.
            if let activeVideoInput { captureSession.addInput(activeVideoInput) }
            return
        }

        captureSession.addInput(newInput)
        activeVideoInput = newInput
    }
}
```

A descriptor identifies a camera, and it doesn’t reserve one. The set of cameras changes while your app dispatches to its session actor, so handle a resolution that produces no device rather than force-unwrapping the result.

#### Update Your Interface for the New Camera

A device change takes time, and frames from the outgoing camera reach the screen while the new camera starts. Mask the preview when your handler fires, and restore it after the new device delivers frames.

Decide mirroring from the direction map rather than from a camera’s position. A capture connection mirrors the preview of any camera whose [`position`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/position-swift.property) is [`AVCaptureDevice.Position.front`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/position-swift.enum/front), which describes where the camera sits rather than where it points. When a rear camera faces forward, mirror the preview yourself, so a person sees the selfie image they expect. When a front camera faces backward, present it unmirrored.

Set [`automaticallyAdjustsVideoMirroring`](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/automaticallyadjustsvideomirroring) to `false` before you assign [`isVideoMirrored`](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideomirrored), because assigning it while the connection adjusts mirroring on its own raises an exception:

```swift
private func applyVideoMirroring(from directionMap: AVCaptureDeviceDirectionMap) {
    // Assigning `isVideoMirrored` raises an exception when the connection doesn't support mirroring.
    guard let connection = previewConnection, connection.isVideoMirroringSupported else { return }

    let uniqueID = activeDevice.uniqueID
    let isFacingForward = directionMap.forwardFacingDeviceDescriptors
        .contains { $0.uniqueID == uniqueID }
    let isFacingBackward = directionMap.backwardFacingDeviceDescriptors
        .contains { $0.uniqueID == uniqueID }
    let isFrontCamera = activeDevice.position == .front

    // Take over mirroring only when a camera's position and its direction disagree.
    let needsOverride = (isFacingForward && !isFrontCamera) || (isFacingBackward && isFrontCamera)
    guard needsOverride else { return }

    // Assigning `isVideoMirrored` raises an exception while automatic adjustment stays on.
    connection.automaticallyAdjustsVideoMirroring = false
    connection.isVideoMirrored = isFacingForward
}
```

Call this method each time the coordinator reports a new map, and again after you connect a new device, because removing and adding an input creates a preview connection that doesn’t carry your override.

#### Keep the Preview and Your Captured Media Upright

An [`AVCaptureDevice.RotationCoordinator`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator) reports how much to rotate a camera’s preview and its captured output to keep both horizon-level relative to gravity. Create one with the device you capture from and the layer that shows its preview, then read the angles it reports as someone turns the device.

Your app needs this whether or not it changes cameras, and on iPhone Duo the angle also changes as your app moves between the two displays. A rotation coordinator reports angles for the device you create it with. Create a new one each time you switch cameras. For more information, see [`Supporting device rotation in your camera app`](https://developer.apple.com/documentation/avfoundation/supporting-device-rotation-in-your-camera-app).

#### Write One Code Path for Every Iphone

Your app runs the same code on every iPhone. On a device with a single display, a coordinator reports the cameras your app already expects. Front cameras arrive in the forward-facing array, back cameras arrive in the backward-facing array, and cameras with an unspecified position arrive in neither. Those cameras never change direction, so your handler receives one call and no more.

Ask a coordinator for the direction a camera faces instead of inferring it from the camera’s type or position. The same code then runs correctly on an iPhone whose cameras never change direction and on one whose cameras do.

## See Also

- [class AVCaptureDeviceDirectionCoordinator](avcapturedevicedirectioncoordinator.md)
  An object that tracks the direction each camera faces in relation to a view.
- [class AVCaptureDeviceDirectionMap](avcapturedevicedirectionmap.md)
  An object that groups the cameras a coordinator tracks by the direction they face.
- [class AVCaptureDeviceDescriptor](avcapturedevicedescriptor.md)
  An object that identifies a capture device and is safe to pass between actors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/choosing-a-camera-by-the-direction-it-faces)*