# uuid

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The external storage device’s unique identifier.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
var uuid: UUID? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSUUID * uuid;
```

## Discussion

The value is `nil` when the system can’t retrieve information from external storage device.

## See Also

### Inspecting a storage device
- [var isConnected: Bool](./isconnected.md)
  A Boolean value that indicates whether the system has a connection to the external storage device.
- [var displayName: String?](./displayname.md)
  The name of an external storage device that’s appropriate for a user interface.
- [var freeSize: Int](./freesize.md)
  The amount of free storage space, in bytes, that’s available on the external storage device.
- [var totalSize: Int](./totalsize.md)
  The total amount of storage space, in bytes, that’s available on the external storage device.
- [var isNotRecommendedForCaptureUse: Bool](./isnotrecommendedforcaptureuse.md)
  A Boolean value that indicates whether the external storage device is suitable for camera capture.
- [var reasonsNotRecommendedForCaptureUse: Set<AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse>](./reasonsnotrecommendedforcaptureuse.md)
- [AVExternalStorageDevice.ReasonNotRecommendedForCaptureUse](./reasonnotrecommendedforcaptureuse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/uuid)*