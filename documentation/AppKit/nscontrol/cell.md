# cell

**Framework**: AppKit  
**Kind**: property

The receiver’s cell object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var cell: NSCell? { get set }
```

#### Discussion

For controls with multiple cells (such as `NSMatrix` or `NSForm`), use the [`selectedCell()`](nscontrol/selectedcell().md) property to retrieve a specific cell.

## See Also

- [class var cellClass: AnyClass?](nscontrol/cellclass.md)
  Returns the type of cell used by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/cell)*