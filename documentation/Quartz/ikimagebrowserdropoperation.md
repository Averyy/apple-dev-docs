# IKImageBrowserDropOperation

**Framework**: Quartz  
**Kind**: struct

These constants specify the locations for dropping items onto the browser view. Used by the method [`setDrop(_:dropOperation:)`](ikimagebrowserview/setdrop(_:dropoperation:).md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
struct IKImageBrowserDropOperation
```

## Topics

### Constants
- [var IKImageBrowserDropOn: IKImageBrowserDropOperation](ikimagebrowserdropon.md)
  Drop the item on the cell.
- [var IKImageBrowserDropBefore: IKImageBrowserDropOperation](ikimagebrowserdropbefore.md)
  Drop the item before the cell.
### Initializers
- [init(UInt32)](ikimagebrowserdropoperation/init(_:).md)
- [init(rawValue: UInt32)](ikimagebrowserdropoperation/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](ikimagebrowserdropoperation/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct IKImageBrowserCellState](ikimagebrowsercellstate.md)
  The possible states for the browser cell. These values are used by the [`cellState()`](ikimagebrowsercell/cellstate().md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserdropoperation)*