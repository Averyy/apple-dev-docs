# IKScannerDeviceViewTransferMode

**Framework**: Quartz  
**Kind**: enum

These constants determine how the scanner data is returned to the delegate. They are used by the [`transferMode`](ikscannerdeviceview/transfermode.md) property.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@frozen
enum IKScannerDeviceViewTransferMode
```

## Topics

### Constants
- [IKScannerDeviceViewTransferMode.fileBased](ikscannerdeviceviewtransfermode/filebased.md)
  The scanned content will be saved to the specified download directory.
- [IKScannerDeviceViewTransferMode.memoryBased](ikscannerdeviceviewtransfermode/memorybased.md)
  The scanned data is returned to the delegate as a `NSData` object.
### Initializers
- [init?(rawValue: Int)](ikscannerdeviceviewtransfermode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum IKScannerDeviceViewDisplayMode](ikscannerdeviceviewdisplaymode.md)
  These constants specify the display mode the scanner view will use. They are used by the [`mode`](ikscannerdeviceview/mode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceviewtransfermode)*