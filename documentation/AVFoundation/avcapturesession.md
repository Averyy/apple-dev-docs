# AVCaptureSession

**Framework**: AVFoundation  
**Kind**: class

An object that configures capture behavior and coordinates the flow of data from input devices to capture outputs.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class AVCaptureSession
```

## Mentions

- [Setting Up a Capture Session](setting-up-a-capture-session.md)
- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)

#### Overview

To perform real-time capture, you instantiate a capture session and add appropriate inputs and outputs. The following code fragment illustrates how to configure a capture device to record audio.

```swift
// Create the capture session.
let captureSession = AVCaptureSession()

// Find the default audio device.
guard let audioDevice = AVCaptureDevice.default(for: .audio) else { return }

do {
    // Wrap the audio device in a capture device input.
    let audioInput = try AVCaptureDeviceInput(device: audioDevice)
    // If the input can be added, add it to the session.
    if captureSession.canAddInput(audioInput) {
        captureSession.addInput(audioInput)
    }
} catch {
    // Configuration failed. Handle error.
}
```

Call the [`startRunning()`](avcapturesession/startrunning().md) method to start the flow of data from the inputs to the outputs, and call the [`stopRunning()`](avcapturesession/stoprunning().md) method to stop the flow.

> ❗ **Important**:  The [`startRunning()`](avcapturesession/startrunning().md) method is a blocking call which can take some time, therefore start the session on a serial dispatch queue so that you don’t block the main queue (which keeps the UI responsive). See [`AVCam: Building a camera app`](avcam-building-a-camera-app.md) for an implementation example.

You use the [`sessionPreset`](avcapturesession/sessionpreset.md) property to customize the quality level, bitrate, or other settings for the output. Most common capture configurations are available through session presets; however, some specialized options (such as high frame rate) require directly setting a capture format on an [`AVCaptureDevice`](avcapturedevice.md) instance.

## Topics

### Configuring a session
- [func beginConfiguration()](avcapturesession/beginconfiguration.md)
  Marks the beginning of changes to a running capture session’s configuration to perform in a single atomic update.
- [func commitConfiguration()](avcapturesession/commitconfiguration.md)
  Commits one or more changes to a running capture session’s configuration in a single atomic update.
### Setting a session preset
- [AVCaptureSession.Preset](avcapturesession/preset.md)
  Presets that define standard configurations for a capture session.
- [func canSetSessionPreset(AVCaptureSession.Preset) -> Bool](avcapturesession/cansetsessionpreset(_:).md)
  Determines whether you can configure a capture session with the specified preset.
- [var sessionPreset: AVCaptureSession.Preset](avcapturesession/sessionpreset.md)
  A preset value that indicates the quality level or bit rate of the output.
### Configuring inputs
- [var inputs: [AVCaptureInput]](avcapturesession/inputs.md)
  The inputs that provide media data to a capture session.
- [func canAddInput(AVCaptureInput) -> Bool](avcapturesession/canaddinput(_:).md)
  Determines whether you can add an input to a session.
- [func addInput(AVCaptureInput)](avcapturesession/addinput(_:).md)
  Adds a capture input to the session.
- [func removeInput(AVCaptureInput)](avcapturesession/removeinput(_:).md)
  Removes an input from the session.
### Configuring outputs
- [var outputs: [AVCaptureOutput]](avcapturesession/outputs.md)
  The output destinations to which a captures session sends its data.
- [func canAddOutput(AVCaptureOutput) -> Bool](avcapturesession/canaddoutput(_:).md)
  Determines whether you can add an output to a session.
- [func addOutput(AVCaptureOutput)](avcapturesession/addoutput(_:).md)
  Adds an output to the capture session.
- [func removeOutput(AVCaptureOutput)](avcapturesession/removeoutput(_:).md)
  Removes an output from a capture session.
### Connecting inputs and outputs
- [var connections: [AVCaptureConnection]](avcapturesession/connections.md)
  The connections between inputs and outputs that a capture session contains.
- [func addConnection(AVCaptureConnection)](avcapturesession/addconnection(_:).md)
  Adds a connection to the capture session.
- [func canAddConnection(AVCaptureConnection) -> Bool](avcapturesession/canaddconnection(_:).md)
  Determines whether a you can add a connection to a capture session.
- [func addInputWithNoConnections(AVCaptureInput)](avcapturesession/addinputwithnoconnections(_:).md)
  Adds a capture input to a session without forming any connections.
- [func addOutputWithNoConnections(AVCaptureOutput)](avcapturesession/addoutputwithnoconnections(_:).md)
  Adds a capture output to the session without forming any connections.
- [func removeConnection(AVCaptureConnection)](avcapturesession/removeconnection(_:).md)
  Removes a capture connection from the session.
- [class AVCaptureAudioChannel](avcaptureaudiochannel.md)
  An object that monitors average and peak power levels for an audio channel in a capture connection.
### Configuring deferred start
- [var isManualDeferredStartSupported: Bool](avcapturesession/ismanualdeferredstartsupported.md)
  A Boolean value that indicates whether the session supports manually running deferred start.
- [var automaticallyRunsDeferredStart: Bool](avcapturesession/automaticallyrunsdeferredstart.md)
  A Boolean value that indicates whether deferred start runs automatically.
- [func runDeferredStartWhenNeeded()](avcapturesession/rundeferredstartwhenneeded.md)
  Tells the session to run deferred start when appropriate.
- [var deferredStartDelegate: (any AVCaptureSessionDeferredStartDelegate)?](avcapturesession/deferredstartdelegate.md)
  A delegate object that observes events about deferred start.
- [var deferredStartDelegateCallbackQueue: dispatch_queue_t?](avcapturesession/deferredstartdelegatecallbackqueue.md)
  The dispatch queue on which the session calls deferred start delegate methods.
- [func setDeferredStartDelegate((any AVCaptureSessionDeferredStartDelegate)?, deferredStartDelegateCallbackQueue: dispatch_queue_t?)](avcapturesession/setdeferredstartdelegate(_:deferredstartdelegatecallbackqueue:).md)
  Sets a delegate object for the session to call when performing deferred start.
- [protocol AVCaptureSessionDeferredStartDelegate](avcapturesessiondeferredstartdelegate.md)
  A protocol that defines the interface to respond to events about a capture session’s deferred start.
### Configuring capture controls
- [var supportsControls: Bool](avcapturesession/supportscontrols.md)
  A Boolean value that indicates whether a capture session supports controls.
- [var maxControlsCount: Int](avcapturesession/maxcontrolscount.md)
  The maximum number of controls a capture session supports.
- [var controls: [AVCaptureControl]](avcapturesession/controls.md)
  The controls that allow configuring the camera system from device hardware.
- [func canAddControl(AVCaptureControl) -> Bool](avcapturesession/canaddcontrol(_:).md)
  Returns a Boolean value that indicates whether a capture session add the specified control.
- [func addControl(AVCaptureControl)](avcapturesession/addcontrol(_:).md)
  Adds a control to a capture session.
- [func removeControl(AVCaptureControl)](avcapturesession/removecontrol(_:).md)
  Removes a control from a capture session.
- [func setControlsDelegate((any AVCaptureSessionControlsDelegate)?, queue: dispatch_queue_t?)](avcapturesession/setcontrolsdelegate(_:queue:).md)
  Sets a delegate object for the system to call when it activates and presents controls.
- [protocol AVCaptureSessionControlsDelegate](avcapturesessioncontrolsdelegate.md)
  A protocol that defines the interface to respond to capture control activation and presentation events.
- [var controlsDelegate: (any AVCaptureSessionControlsDelegate)?](avcapturesession/controlsdelegate.md)
  A delegate object that observes changes to the state of capture controls.
- [var controlsDelegateCallbackQueue: dispatch_queue_t?](avcapturesession/controlsdelegatecallbackqueue.md)
  The dispatch queue on which the system calls controls delegate methods.
### Managing the session life cycle
- [func startRunning()](avcapturesession/startrunning.md)
  Starts the flow of data through the capture pipeline.
- [func stopRunning()](avcapturesession/stoprunning.md)
  Stops the flow of data through the capture pipeline.
### Observing session state
- [var isRunning: Bool](avcapturesession/isrunning.md)
  A Boolean value that indicates whether the capture session is in a running state.
- [var isInterrupted: Bool](avcapturesession/isinterrupted.md)
  A Boolean value that indicates whether the capture session is in an interrupted state.
- [class let didStartRunningNotification: NSNotification.Name](avcapturesession/didstartrunningnotification.md)
  A notification the system posts when a capture session starts.
- [class let didStopRunningNotification: NSNotification.Name](avcapturesession/didstoprunningnotification.md)
  A notification the system posts when a capture session stops.
- [class let wasInterruptedNotification: NSNotification.Name](avcapturesession/wasinterruptednotification.md)
  A notification the system posts when it interrupts a capture session.
- [class let interruptionEndedNotification: NSNotification.Name](avcapturesession/interruptionendednotification.md)
  A notification the system posts when an interruption to a capture session finishes.
- [class let runtimeErrorNotification: NSNotification.Name](avcapturesession/runtimeerrornotification.md)
  A notification the system posts when an error occurs during a capture session.
### Configuring multitasking
- [var isMultitaskingCameraAccessSupported: Bool](avcapturesession/ismultitaskingcameraaccesssupported.md)
  A Boolean value that indicates whether the capture session supports using the camera while multitasking.
- [var isMultitaskingCameraAccessEnabled: Bool](avcapturesession/ismultitaskingcameraaccessenabled.md)
  A Boolean value that indicates whether the capture session enables access to the camera while multitasking.
### Monitoring performance
- [var hardwareCost: Float](avcapturesession/hardwarecost.md)
  A value that indicates the percentage of the session’s available hardware budget in use.
### Configuring the app’s audio session
- [var usesApplicationAudioSession: Bool](avcapturesession/usesapplicationaudiosession.md)
  A Boolean value that indicates whether the capture session uses the app’s shared audio session.
- [var automaticallyConfiguresApplicationAudioSession: Bool](avcapturesession/automaticallyconfiguresapplicationaudiosession.md)
  A Boolean value that indicates whether the capture session automatically changes settings in the app’s shared audio session.
- [var configuresApplicationAudioSessionToMixWithOthers: Bool](avcapturesession/configuresapplicationaudiosessiontomixwithothers.md)
  A Boolean value that Indicates whether the capture session configures the app’s audio session to mix with others.
- [var configuresApplicationAudioSessionForBluetoothHighQualityRecording: Bool](avcapturesession/configuresapplicationaudiosessionforbluetoothhighqualityrecording.md)
  A Boolean value that indicates whether the capture session configures the app’s audio session for bluetooth high-quality recording.
### Managing color spaces
- [var automaticallyConfiguresCaptureDeviceForWideColor: Bool](avcapturesession/automaticallyconfigurescapturedeviceforwidecolor.md)
  A Boolean value that specifies whether the session should automatically use wide-gamut color where available.
### Synchronizing output
- [var synchronizationClock: CMClock?](avcapturesession/synchronizationclock.md)
  A clock to use for output synchronization.
- [var masterClock: CMClock?](avcapturesession/masterclock.md)
  A clock object used for output synchronization.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVCaptureMultiCamSession](avcapturemulticamsession.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Setting Up a Capture Session](setting-up-a-capture-session.md)
  Configure input devices, output media, preview views, and basic settings before capturing photos or video.
- [Accessing the camera while multitasking on iPad](../AVKit/accessing-the-camera-while-multitasking-on-ipad.md)
  Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
- [AVCam: Building a camera app](avcam-building-a-camera-app.md)
  Capture photos and record video using the front and rear iPhone and iPad cameras.
- [Capturing cinematic video](capturing-cinematic-video.md)
  Capture video with an adjustable depth of field and focus points.
- [AVMultiCamPiP: Capturing from Multiple Cameras](avmulticampip-capturing-from-multiple-cameras.md)
  Simultaneously record the output from the front and back cameras into a single movie file by using a multi-camera capture session.
- [AVCamBarcode: Detecting Barcodes and Faces](avcambarcode-detecting-barcodes-and-faces.md)
  Identify machine readable codes or faces by using the camera.
- [class AVCaptureMultiCamSession](avcapturemulticamsession.md)
  A capture session that supports simultaneous capture from multiple inputs of the same media type.
- [class AVCaptureInput](avcaptureinput.md)
  An abstract superclass for objects that provide input data to a capture session.
- [class AVCaptureOutput](avcaptureoutput.md)
  An abstract superclass for objects that provide media output destinations for a capture session.
- [class AVCaptureConnection](avcaptureconnection.md)
  An object that represents a connection from a capture input to a capture output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession)*