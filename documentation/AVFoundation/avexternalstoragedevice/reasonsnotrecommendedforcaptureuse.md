# reasonsNotRecommendedForCaptureUse

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var reasonsNotRecommendedForCaptureUse: Set<AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse> { get }
```

```objc
@property (nonatomic, readonly) NSSet<NSString *> * reasonsNotRecommendedForCaptureUse;
```

#### Discussion

A set of reasons why the storage device is not recommended for capture.

Contains one or more AVExternalStorageDeviceReasonNotRecommendedForCaptureUse values indicating the issues with the device. Returns an empty set if there are no known issues.

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
- [AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse](./reasonnotrecommendedforcaptureuse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/reasonsnotrecommendedforcaptureuse)*