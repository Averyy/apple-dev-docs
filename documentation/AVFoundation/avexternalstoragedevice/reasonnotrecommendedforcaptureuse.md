# AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse

**Framework**: AVFoundation  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
struct ReasonNotRecommendedForCaptureUse
```

#### Overview

Constants indicating the reasons external storage device is not recommended for capturing high data rate videos based on https://support.apple.com/en-us/109041.

## Topics

### Creating a reason
- [init(rawValue: String)](avexternalstoragedevice/reasonnotrecommendedforcaptureuse/init(rawvalue:).md)
### Reasons
- [static let encrypted: AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse](avexternalstoragedevice/reasonnotrecommendedforcaptureuse/encrypted.md)
- [static let slowWritingSpeed: AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse](avexternalstoragedevice/reasonnotrecommendedforcaptureuse/slowwritingspeed.md)
- [static let unknownWritingSpeed: AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse](avexternalstoragedevice/reasonnotrecommendedforcaptureuse/unknownwritingspeed.md)
- [static let unsupportedFileSystem: AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse](avexternalstoragedevice/reasonnotrecommendedforcaptureuse/unsupportedfilesystem.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var isConnected: Bool](avexternalstoragedevice/isconnected.md)
  A Boolean value that indicates whether the system has a connection to the external storage device.
- [var displayName: String?](avexternalstoragedevice/displayname.md)
  The name of an external storage device that’s appropriate for a user interface.
- [var uuid: UUID?](avexternalstoragedevice/uuid.md)
  The external storage device’s unique identifier.
- [var freeSize: Int](avexternalstoragedevice/freesize.md)
  The amount of free storage space, in bytes, that’s available on the external storage device.
- [var totalSize: Int](avexternalstoragedevice/totalsize.md)
  The total amount of storage space, in bytes, that’s available on the external storage device.
- [var isNotRecommendedForCaptureUse: Bool](avexternalstoragedevice/isnotrecommendedforcaptureuse.md)
  A Boolean value that indicates whether the external storage device is suitable for camera capture.
- [var reasonsNotRecommendedForCaptureUse: Set<AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse>](avexternalstoragedevice/reasonsnotrecommendedforcaptureuse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/reasonnotrecommendedforcaptureuse)*