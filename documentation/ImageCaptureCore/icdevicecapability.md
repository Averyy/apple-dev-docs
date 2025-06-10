# ICDeviceCapability

**Framework**: ImageCaptureCore  
**Kind**: struct

Constants that describe the capabilities of a camera.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
struct ICDeviceCapability
```

## Topics

### Creating Device Capabilities
- [init(rawValue: String)](icdevicecapability/init(rawvalue:).md)
  Creates an ImageCaptureCore device capability.
### Taking Pictures
- [static let cameraDeviceCanTakePicture: ICDeviceCapability](icdevicecapability/cameradevicecantakepicture.md)
  The capability for the client to request to take a picture while the camera is connected.
- [static let cameraDeviceCanTakePictureUsingShutterReleaseOnCamera: ICDeviceCapability](icdevicecapability/cameradevicecantakepictureusingshutterreleaseoncamera.md)
  The capability to capture a picture if the user presses the shutter release on the camera while the camera is connected.
### Deleting Files
- [static let cameraDeviceCanDeleteOneFile: ICDeviceCapability](icdevicecapability/cameradevicecandeleteonefile.md)
  Indicates that the camera can delete a file at a time while it is connected.
- [static let cameraDeviceCanDeleteAllFiles: ICDeviceCapability](icdevicecapability/cameradevicecandeleteallfiles.md)
  Indicates that the camera can delete all files in a single operation while it is connected.
### Uploading Files
- [static let cameraDeviceCanReceiveFile: ICDeviceCapability](icdevicecapability/cameradevicecanreceivefile.md)
  Indicates that the host can upload files to the camera.
### Synchronizing the Clock
- [static let cameraDeviceCanSyncClock: ICDeviceCapability](icdevicecapability/cameradevicecansyncclock.md)
  Indicates that the camera can synchronize its date and time with that of the host computer.
### Sending PTP Commands
- [static let cameraDeviceCanAcceptPTPCommands: ICDeviceCapability](icdevicecapability/cameradevicecanacceptptpcommands.md)
  Indicates that the camera can accept PTP commands.
### Disconnecting
- [static let canEjectOrDisconnect: ICDeviceCapability](icdevicecapability/canejectordisconnect.md)
  Indicates that the camera can eject or disconnect.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var capabilities: [String]](icdevice/capabilities.md)
  The capabilities of the device as reported by the device module.
- [struct ICSessionOptions](icsessionoptions.md)
  Session options for altering the delivery of the device contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicecapability)*