# IKImageBrowserCellState

**Framework**: Quartz  
**Kind**: struct  
**Role**: Structure

The possible states for the browser cell. These values are used by the [`cellState()`](./ikimagebrowsercell/cellstate%28%29.md) method.

**Availability**:
- macOS 10.4+

## Declaration

```swift
struct IKImageBrowserCellState
```

```c
typedef enum { ... } IKImageBrowserCellState;
```

## Topics

### Constants
- [var IKImageStateNoImage: IKImageBrowserCellState](./ikimagestatenoimage.md)
  Returned until a thumbnail has been created from the represented object.
- [var IKImageStateInvalid: IKImageBrowserCellState](./ikimagestateinvalid.md)
  The thumbnail is invalid. For example, an unsupported image is provided.
- [var IKImageStateReady: IKImageBrowserCellState](./ikimagestateready.md)
  The receiver’s represented object has been set and the cell is ready to display.
### Initializers
- [init(UInt32)](./ikimagebrowsercellstate/init%28_%29.md)
- [init(rawValue: UInt32)](./ikimagebrowsercellstate/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./ikimagebrowsercellstate/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Informal Protocols
- [struct IKImageBrowserDropOperation](./ikimagebrowserdropoperation.md)
  These constants specify the locations for dropping items onto the browser view. Used by the method [`setDrop(_:dropOperation:)`](./ikimagebrowserview/setdrop%28_,dropoperation%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercellstate)*