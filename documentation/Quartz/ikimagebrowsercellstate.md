# IKImageBrowserCellState

**Framework**: Quartz  
**Kind**: struct

The possible states for the browser cell. These values are used by the [`cellState()`](ikimagebrowsercell/cellstate().md) method.

**Availability**:
- macOS 10.4+

## Declaration

```swift
struct IKImageBrowserCellState
```

## Topics

### Constants
- [var IKImageStateNoImage: IKImageBrowserCellState](ikimagestatenoimage.md)
  Returned until a thumbnail has been created from the represented object.
- [var IKImageStateInvalid: IKImageBrowserCellState](ikimagestateinvalid.md)
  The thumbnail is invalid. For example, an unsupported image is provided.
- [var IKImageStateReady: IKImageBrowserCellState](ikimagestateready.md)
  The receiver’s represented object has been set and the cell is ready to display.
### Initializers
- [init(UInt32)](ikimagebrowsercellstate/init(_:).md)
- [init(rawValue: UInt32)](ikimagebrowsercellstate/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](ikimagebrowsercellstate/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct IKImageBrowserDropOperation](ikimagebrowserdropoperation.md)
  These constants specify the locations for dropping items onto the browser view. Used by the method [`setDrop(_:dropOperation:)`](ikimagebrowserview/setdrop(_:dropoperation:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercellstate)*