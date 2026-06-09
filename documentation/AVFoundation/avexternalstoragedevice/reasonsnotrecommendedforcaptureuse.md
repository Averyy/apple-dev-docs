# reasonsNotRecommendedForCaptureUse

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var reasonsNotRecommendedForCaptureUse: Set<AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse> { get }
```

#### Discussion

A set of reasons why the storage device is not recommended for capture.

Contains one or more AVExternalStorageDeviceReasonNotRecommendedForCaptureUse values indicating the issues with the device. Returns an empty set if there are no known issues.

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
- [AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse](avexternalstoragedevice/reasonnotrecommendedforcaptureuse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/reasonsnotrecommendedforcaptureuse)*