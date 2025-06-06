# mode

**Framework**: AppKit  
**Kind**: property

The selection mode of the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var mode: NSMatrix.Mode { get set }
```

#### Discussion

See [`NSMatrix.Mode`](nsmatrix/mode-swift.enum.md) for possible values.

## See Also

- [init(frame: NSRect, mode: NSMatrix.Mode, cellClass: AnyClass?, numberOfRows: Int, numberOfColumns: Int)](nsmatrix/init(frame:mode:cellclass:numberofrows:numberofcolumns:).md)
  Initializes and returns a newly allocated matrix of the specified size using cells of the given class.
- [init(frame: NSRect, mode: NSMatrix.Mode, prototype: NSCell, numberOfRows: Int, numberOfColumns: Int)](nsmatrix/init(frame:mode:prototype:numberofrows:numberofcolumns:).md)
  Initializes and returns a newly allocated matrix of the specified size using the given cell as a prototype.
- [var allowsEmptySelection: Bool](nsmatrix/allowsemptyselection.md)
  A Boolean that indicates whether a radio-mode matrix supports an empty selection.
- [var isSelectionByRect: Bool](nsmatrix/isselectionbyrect.md)
  A Boolean that indicates whether the user can select a rectangle of cells in the receiver by dragging the cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/mode-swift.property)*