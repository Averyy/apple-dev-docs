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

- [Setting Up a Capture Session](setting-up-a-capture-session.md)

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
### Accessing the Device
- [var device: AVCaptureDevice](avcapturedeviceinput/device.md)
  A capture device associated with this input.
- [func ports(for: AVMediaType?, sourceDeviceType: AVCaptureDevice.DeviceType?, sourceDevicePosition: AVCaptureDevice.Position) -> [AVCaptureInput.Port]](avcapturedeviceinput/ports(for:sourcedevicetype:sourcedeviceposition:).md)
  Retrieves a virtual device’s constituent device ports for use in a multi-camera session.
### Instance Properties
- [var isWindNoiseRemovalEnabled: Bool](avcapturedeviceinput/iswindnoiseremovalenabled.md)
- [var isWindNoiseRemovalSupported: Bool](avcapturedeviceinput/iswindnoiseremovalsupported.md)
- [var isCinematicVideoCaptureEnabled: Bool](avcapturedeviceinput/iscinematicvideocaptureenabled.md)
- [var isCinematicVideoCaptureSupported: Bool](avcapturedeviceinput/iscinematicvideocapturesupported.md)
- [var simulatedAperture: Float](avcapturedeviceinput/simulatedaperture.md)

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

- [Choosing a Capture Device](choosing-a-capture-device.md)
  Select the front or back camera, or use advanced features like the TrueDepth camera or dual camera.
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