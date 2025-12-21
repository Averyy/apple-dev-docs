# AVCaptureDeviceInput

**Framework**: AVFoundation  
**Kind**: class

An object that provides media input from a capture device to a capture session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class AVCaptureDeviceInput
```

## Mentions

- [Setting up a capture session](setting-up-a-capture-session.md)

#### Overview

This class is a concrete subclass of [`AVCaptureInput`](avcaptureinput.md) that you use to connect a capture device to a capture session.

## Topics

### Creating an input
- [init(device: AVCaptureDevice) throws](avcapturedeviceinput/init(device:).md)
  Creates an input for the specified capture device.
### Configuring video properties
- [var unifiedAutoExposureDefaultsEnabled: Bool](avcapturedeviceinput/unifiedautoexposuredefaultsenabled.md)
  A Boolean value that indicates whether the input enables unified auto-exposure defaults.
- [var videoMinFrameDurationOverride: CMTime](avcapturedeviceinput/videominframedurationoverride.md)
  A time value that acts as a modifier to a capture device’s active video minimum frame duration.
### Configuring audio properties
- [func isMultichannelAudioModeSupported(AVCaptureMultichannelAudioMode) -> Bool](avcapturedeviceinput/ismultichannelaudiomodesupported(_:).md)
  A Boolean value that indicates whether the input supports the specified multichannel audio mode.
- [var multichannelAudioMode: AVCaptureMultichannelAudioMode](avcapturedeviceinput/multichannelaudiomode.md)
  The multichannel audio mode to apply when recording audio.
- [enum AVCaptureMultichannelAudioMode](avcapturemultichannelaudiomode.md)
  Constants that indicate the modes of multichannel audio.
- [var isWindNoiseRemovalSupported: Bool](avcapturedeviceinput/iswindnoiseremovalsupported.md)
- [var isWindNoiseRemovalEnabled: Bool](avcapturedeviceinput/iswindnoiseremovalenabled.md)
### Configuring Cinematic video capture
- [var isCinematicVideoCaptureSupported: Bool](avcapturedeviceinput/iscinematicvideocapturesupported.md)
  A BOOL value specifying whether Cinematic Video capture is supported.
- [var isCinematicVideoCaptureEnabled: Bool](avcapturedeviceinput/iscinematicvideocaptureenabled.md)
  A BOOL value specifying whether the Cinematic Video effect is being applied to any movie file output, video data output, metadata output, or video preview layer added to the capture session.
- [var simulatedAperture: Float](avcapturedeviceinput/simulatedaperture.md)
  Shallow depth of field simulated aperture.
### Locking frame duration
- [var activeLockedVideoFrameDuration: CMTime](avcapturedeviceinput/activelockedvideoframeduration.md)
  The receiver’s locked frame duration (the reciprocal of its frame rate). Setting this property guarantees the intra-frame duration delivered by the device input is precisely the frame duration you request.
- [var isLockedVideoFrameDurationSupported: Bool](avcapturedeviceinput/islockedvideoframedurationsupported.md)
  Indicates whether the device input supports locked frame durations.
### Synchronizing with external devices
- [var isExternalSyncSupported: Bool](avcapturedeviceinput/isexternalsyncsupported.md)
  Indicates whether the device input supports being configured to follow an external sync device.
- [func follow(AVExternalSyncDevice, videoFrameDuration: CMTime, delegate: (any AVExternalSyncDeviceDelegate)?)](avcapturedeviceinput/follow(_:videoframeduration:delegate:).md)
  Configures the the device input to follow an external sync device at the given frame duration.
- [func unfollowExternalSyncDevice()](avcapturedeviceinput/unfollowexternalsyncdevice.md)
  Discontinues external sync.
- [var activeExternalSyncVideoFrameDuration: CMTime](avcapturedeviceinput/activeexternalsyncvideoframeduration.md)
  The receiver’s external sync frame duration (the reciprocal of its frame rate) when being driven by an external sync device.
- [var externalSyncDevice: AVExternalSyncDevice?](avcapturedeviceinput/externalsyncdevice.md)
  The external sync device currently being followed by this input.
### Accessing the device
- [var device: AVCaptureDevice](avcapturedeviceinput/device.md)
  A capture device associated with this input.
- [func ports(for: AVMediaType?, sourceDeviceType: AVCaptureDevice.DeviceType?, sourceDevicePosition: AVCaptureDevice.Position) -> [AVCaptureInput.Port]](avcapturedeviceinput/ports(for:sourcedevicetype:sourcedeviceposition:).md)
  Retrieves a virtual device’s constituent device ports for use in a multi-camera session.

## Relationships

### Inherits From
- [AVCaptureInput](avcaptureinput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Choosing a capture device](choosing-a-capture-device.md)
  Select the front or back camera, or use advanced features like the TrueDepth camera or dual camera.
- [Adopting smart framing in your camera app](adopting-smart-framing-in-your-camera-app.md)
  Capture the optimal shot by providing automatic framing recommendations.
- [class AVCaptureDevice](avcapturedevice.md)
  An object that represents a hardware or virtual capture device like a camera or microphone.
- [class AVContinuityDevice](avcontinuitydevice.md)
  A class that represents a physical iOS device that’s nearby and can provide access to its cameras and microphones.
- [class AVExternalStorageDevice](avexternalstoragedevice.md)
  Represents a physical external storage device that stores media assets.
- [class AVExternalStorageDeviceDiscoverySession](avexternalstoragedevicediscoverysession.md)
  Informs your app when the external storage devices connect to and disconnect from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput)*