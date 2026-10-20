# AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
struct ReasonNotRecommendedForCaptureUse
```

```c
typedef NSString * AVExternalStorageDeviceReasonNotRecommendedForCaptureUse;
```

#### Overview

Constants indicating the reasons external storage device is not recommended for capturing high data rate videos based on https://support.apple.com/en-us/109041.

## Topics

### Creating a reason
- [init(rawValue: String)](./reasonnotrecommendedforcaptureuse/init%28rawvalue%29.md)
### Reasons
- [static let encrypted: AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse](./reasonnotrecommendedforcaptureuse/encrypted.md)
- [static let slowWritingSpeed: AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse](./reasonnotrecommendedforcaptureuse/slowwritingspeed.md)
- [static let unknownWritingSpeed: AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse](./reasonnotrecommendedforcaptureuse/unknownwritingspeed.md)
- [static let unsupportedFileSystem: AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse](./reasonnotrecommendedforcaptureuse/unsupportedfilesystem.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting a storage device
- [var isConnected: Bool](./isconnected.md)
  A Boolean value that indicates whether the system has a connection to the external storage device.
- [var displayName: String?](./displayname.md)
  The name of an external storage device that’s appropriate for a user interface.
- [var uuid: UUID?](./uuid.md)
  The external storage device’s unique identifier.
- [var freeSize: Int](./freesize.md)
  The amount of free storage space, in bytes, that’s available on the external storage device.
- [var totalSize: Int](./totalsize.md)
  The total amount of storage space, in bytes, that’s available on the external storage device.
- [var isNotRecommendedForCaptureUse: Bool](./isnotrecommendedforcaptureuse.md)
  A Boolean value that indicates whether the external storage device is suitable for camera capture.
- [var reasonsNotRecommendedForCaptureUse: Set<AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse>](./reasonsnotrecommendedforcaptureuse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/reasonnotrecommendedforcaptureuse)*