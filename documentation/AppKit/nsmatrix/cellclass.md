# cellClass

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The subclass of [`NSCell`](../nscell.md) that the matrix uses when creating new (empty) cells.

**Availability**:
- macOS

## Declaration

```swift
var cellClass: AnyClass { get set }
```

```objc
@property (assign) Class cellClass;
```

#### Discussion

The value of this property should be the id of a subclass of [`NSCell`](../nscell.md), which can be obtained by sending the `class` message to either the [`NSCell`](../nscell.md) subclass object or to an instance of that subclass. The default cell class is that set with the class method `setCellClass(_:)`, or [`NSActionCell`](../nsactioncell.md) if no other default cell class has been specified.

You need to use this property only with matrices initialized with [`init(frame:)`](./init%28frame%29.md), because the other initializers allow you to specify an instance-specific cell class or cell prototype.

## See Also

### Related Documentation
- [func insertColumn(Int)](./insertcolumn%28_%29.md)
  Inserts a new column of cells at the specified location.
- [func addRow()](./addrow%28%29.md)
  Adds a new row of cells below the last row.
- [func addColumn()](./addcolumn%28%29.md)
  Adds a new column of cells to the right of the last column.
- [func insertRow(Int)](./insertrow%28_%29.md)
  Inserts a new row of cells before the specified row.
- [func makeCell(atRow: Int, column: Int) -> NSCell](./makecell%28atrow,column%29.md)
  Creates a new cell at the location specified by the given row and column in the receiver.
### Managing the Cell Class
- [var prototype: NSCell?](./prototype.md)
  The prototype cell that’s copied whenever the matrix creates a new cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/cellclass)*