# IKImageBrowserDropOperation

**Framework**: Quartz  
**Kind**: struct  
**Role**: Structure

These constants specify the locations for dropping items onto the browser view. Used by the method [`setDrop(_:dropOperation:)`](./ikimagebrowserview/setdrop%28_,dropoperation%29.md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
struct IKImageBrowserDropOperation
```

```c
typedef enum { ... } IKImageBrowserDropOperation;
```

## Topics

### Constants
- [var IKImageBrowserDropOn: IKImageBrowserDropOperation](./ikimagebrowserdropon.md)
  Drop the item on the cell.
- [var IKImageBrowserDropBefore: IKImageBrowserDropOperation](./ikimagebrowserdropbefore.md)
  Drop the item before the cell.
### Initializers
- [init(UInt32)](./ikimagebrowserdropoperation/init%28_%29.md)
- [init(rawValue: UInt32)](./ikimagebrowserdropoperation/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./ikimagebrowserdropoperation/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Informal Protocols
- [struct IKImageBrowserCellState](./ikimagebrowsercellstate.md)
  The possible states for the browser cell. These values are used by the [`cellState()`](./ikimagebrowsercell/cellstate%28%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserdropoperation)*