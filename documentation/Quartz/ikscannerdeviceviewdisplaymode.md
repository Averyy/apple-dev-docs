# IKScannerDeviceViewDisplayMode

**Framework**: Quartz  
**Kind**: enum  
**Role**: Enumeration

These constants specify the display mode the scanner view will use. They are used by the [`mode`](./ikscannerdeviceview/mode.md) property.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@frozen
enum IKScannerDeviceViewDisplayMode
```

```c
enum IKScannerDeviceViewDisplayMode : NSInteger;
```

## Topics

### Constants
- [IKScannerDeviceViewDisplayMode.simple](./ikscannerdeviceviewdisplaymode/simple.md)
  The view will display in simple mode.
- [IKScannerDeviceViewDisplayMode.advanced](./ikscannerdeviceviewdisplaymode/advanced.md)
  The view will display in advanced mode.
### Enumeration Cases
- [IKScannerDeviceViewDisplayMode.none](./ikscannerdeviceviewdisplaymode/none.md)
### Initializers
- [init?(rawValue: Int)](./ikscannerdeviceviewdisplaymode/init%28rawvalue%29.md)

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
- [enum IKScannerDeviceViewTransferMode](./ikscannerdeviceviewtransfermode.md)
  These constants determine how the scanner data is returned to the delegate. They are used by the [`transferMode`](./ikscannerdeviceview/transfermode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceviewdisplaymode)*