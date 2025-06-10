# IKCameraDeviceViewTransferMode

**Framework**: Quartz  
**Kind**: enum

These constants specify the transfer mode used by the camera view. These constants are used by [`mode`](ikcameradeviceview/mode.md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
@frozen
enum IKCameraDeviceViewTransferMode
```

## Topics

### Constants
- [IKCameraDeviceViewTransferMode.fileBased](ikcameradeviceviewtransfermode/filebased.md)
  Transferred files will be saved to disk by the delegate.
- [IKCameraDeviceViewTransferMode.memoryBased](ikcameradeviceviewtransfermode/memorybased.md)
  Transferred files will be supplied to the delegate as an `NSData` object.
### Initializers
- [init?(rawValue: Int)](ikcameradeviceviewtransfermode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum IKCameraDeviceViewDisplayMode](ikcameradeviceviewdisplaymode.md)
  These constants specify the display mode used by the camera view. These constants are used by [`mode`](ikcameradeviceview/mode.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceviewtransfermode)*