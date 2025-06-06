# cellClass

**Framework**: AppKit  
**Kind**: property

The subclass of [`NSCell`](nscell.md) that the matrix uses when creating new (empty) cells.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var cellClass: AnyClass { get set }
```

#### Discussion

The value of this property should be the id of a subclass of [`NSCell`](nscell.md), which can be obtained by sending the `class` message to either the [`NSCell`](nscell.md) subclass object or to an instance of that subclass. The default cell class is that set with the class method `setCellClass(_:)`, or [`NSActionCell`](nsactioncell.md) if no other default cell class has been specified.

You need to use this property only with matrices initialized with [`init(frame:)`](nsmatrix/init(frame:).md), because the other initializers allow you to specify an instance-specific cell class or cell prototype.

## See Also

- [func insertColumn(Int)](nsmatrix/insertcolumn(_:).md)
  Inserts a new column of cells at the specified location. .
- [func addRow()](nsmatrix/addrow.md)
  Adds a new row of cells below the last row.
- [func addColumn()](nsmatrix/addcolumn.md)
  Adds a new column of cells to the right of the last column.
- [func insertRow(Int)](nsmatrix/insertrow(_:).md)
  Inserts a new row of cells before the specified row.
- [func makeCell(atRow: Int, column: Int) -> NSCell](nsmatrix/makecell(atrow:column:).md)
  Creates a new cell at the location specified by the given row and column in the receiver.
- [var prototype: NSCell?](nsmatrix/prototype.md)
  The prototype cell that’s copied whenever the matrix creates a new cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/cellclass)*