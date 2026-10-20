# IKCameraDeviceViewTransferMode

**Framework**: Quartz  
**Kind**: enum  
**Role**: Enumeration

These constants specify the transfer mode used by the camera view. These constants are used by [`mode`](./ikcameradeviceview/mode.md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
@frozen
enum IKCameraDeviceViewTransferMode
```

```c
enum IKCameraDeviceViewTransferMode : NSInteger;
```

## Topics

### Constants
- [IKCameraDeviceViewTransferMode.fileBased](./ikcameradeviceviewtransfermode/filebased.md)
  Transferred files will be saved to disk by the delegate.
- [IKCameraDeviceViewTransferMode.memoryBased](./ikcameradeviceviewtransfermode/memorybased.md)
  Transferred files will be supplied to the delegate as an `NSData` object.
### Initializers
- [init?(rawValue: Int)](./ikcameradeviceviewtransfermode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum IKCameraDeviceViewDisplayMode](./ikcameradeviceviewdisplaymode.md)
  These constants specify the display mode used by the camera view. These constants are used by [`mode`](./ikcameradeviceview/mode.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceviewtransfermode)*