# cellClass

**Framework**: AppKit  
**Kind**: property

Returns the type of cell used by the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var cellClass: AnyClass? { get set }
```

#### Return Value

The class of the cell used to manage the receiver’s contents, or `nil` if no cell class has been set for the receiver or its superclasses (up to NSControl).

## See Also

- [var cell: NSCell?](nscontrol/cell.md)
  The receiver’s cell object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/cellclass)*