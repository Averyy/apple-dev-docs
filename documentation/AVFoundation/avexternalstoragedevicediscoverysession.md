# AVExternalStorageDeviceDiscoverySession

**Framework**: AVFoundation  
**Kind**: class

Informs your app when the external storage devices connect to and disconnect from the system.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
class AVExternalStorageDeviceDiscoverySession
```

## Topics

### Checking for session support on a device
- [class var isSupported: Bool](avexternalstoragedevicediscoverysession/issupported.md)
  A Boolean value that indicates whether the system supports external storage devices.
### Retrieving the shared device discovery session instance
- [class var shared: AVExternalStorageDeviceDiscoverySession?](avexternalstoragedevicediscoverysession/shared.md)
  The system’s singleton device discovery session instance.
### Monitoring for storage device updates
- [var externalStorageDevices: [AVExternalStorageDevice]](avexternalstoragedevicediscoverysession/externalstoragedevices.md)
  An array of external storage devices the session updates as individual devices connect or disconnect from the system.

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

- [Choosing a Capture Device](choosing-a-capture-device.md)
  Select the front or back camera, or use advanced features like the TrueDepth camera or dual camera.
- [class AVCaptureDevice](avcapturedevice.md)
  An object that represents a hardware or virtual capture device like a camera or microphone.
- [class AVCaptureDeviceInput](avcapturedeviceinput.md)
  An object that provides media input from a capture device to a capture session.
- [class AVContinuityDevice](avcontinuitydevice.md)
  A class that represents a physical iOS device that’s nearby and can provide access to its cameras and microphones.
- [class AVExternalStorageDevice](avexternalstoragedevice.md)
  Represents a physical external storage device that stores media assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalstoragedevicediscoverysession)*