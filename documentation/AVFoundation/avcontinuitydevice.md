# AVContinuityDevice

**Framework**: AVFoundation  
**Kind**: class

A class that represents a physical iOS device that’s nearby and can provide access to its cameras and microphones.

**Availability**:
- tvOS 17.0+

## Declaration

```swift
class AVContinuityDevice
```

#### Overview

Each continuity device instance represents another iOS device that’s nearby. Your app can access the other device’s cameras and microphones with its [`videoDevices`](avcontinuitydevice/videodevices.md) and [`audioSessionInputs`](avcontinuitydevice/audiosessioninputs.md) properties, respectively.

## Topics

### Checking a continuity device’s availability
- [var isConnected: Bool](avcontinuitydevice/isconnected.md)
  A Boolean value that indicates whether you can use the continuity device because it’s connected to the system.
### Retrieving video devices from a continuity device
- [var videoDevices: [AVCaptureDevice]](avcontinuitydevice/videodevices.md)
  An array of the continuity device’s video-capture devices available to your app.
### Retrieving audio ports from a continuity device
- [var audioSessionInputs: [AVAudioSessionPortDescription]](avcontinuitydevice/audiosessioninputs.md)
  An array of the continuity device’s audio session port descriptions that’s available to your app.
### Identifying a continuity device
- [var connectionID: UUID](avcontinuitydevice/connectionid.md)
  A universally unique value that identifies a specific continuity device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [class AVCaptureDeviceInput](avcapturedeviceinput.md)
  An object that provides media input from a capture device to a capture session.
- [class AVExternalStorageDevice](avexternalstoragedevice.md)
  Represents a physical external storage device that stores media assets.
- [class AVExternalStorageDeviceDiscoverySession](avexternalstoragedevicediscoverysession.md)
  Informs your app when the external storage devices connect to and disconnect from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontinuitydevice)*