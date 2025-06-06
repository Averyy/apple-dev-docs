# prototype

**Framework**: AppKit  
**Kind**: property

The prototype cell that’s copied whenever the matrix creates a new cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
@MainActor var prototype: NSCell? { get set }
```

#### Discussion

When the value of this property is `nil`, there is no prototype cell.

## See Also

- [init(frame: NSRect, mode: NSMatrix.Mode, prototype: NSCell, numberOfRows: Int, numberOfColumns: Int)](nsmatrix/init(frame:mode:prototype:numberofrows:numberofcolumns:).md)
  Initializes and returns a newly allocated matrix of the specified size using the given cell as a prototype.
- [func makeCell(atRow: Int, column: Int) -> NSCell](nsmatrix/makecell(atrow:column:).md)
  Creates a new cell at the location specified by the given row and column in the receiver.
- [var cellClass: AnyClass](nsmatrix/cellclass.md)
  The subclass of [`NSCell`](nscell.md) that the matrix uses when creating new (empty) cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/prototype)*