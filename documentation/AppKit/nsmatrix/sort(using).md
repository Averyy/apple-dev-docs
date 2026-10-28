# sort(using:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sorts the receiver’s cells in ascending order as defined by the comparison method.

**Availability**:
- macOS

## Declaration

```swift
func sort(using comparator: Selector)
```

```objc
- (void) sortUsingSelector:(SEL) comparator;
```

## Discussion

The comparator message is sent to each object in the matrix and has as its single argument another object in the array. The comparison method is used to compare two elements at a time and should return `NSOrderedAscending` if the receiver is smaller than the argument, `NSOrderedDescending` if the receiver is larger than the argument, and `NSOrderedSame` if they are equal.

## Parameters

- `comparator`: The comparison method.

## See Also

### Related Documentation
- [func sort(using: Selector)](../../Foundation/nsmutablearray/sort%28using%29-537vs.md)
  Sorts the receiver in ascending order, as determined by the comparison method specified by a given selector.
### Laying Out the Cells of the Matrix
- [func addColumn()](./addcolumn%28%29.md)
  Adds a new column of cells to the right of the last column.
- [func addColumn(with: [NSCell])](./addcolumn%28with%29.md)
  Adds a new column of cells to the right of the last column, using the given cells.
- [func addRow()](./addrow%28%29.md)
  Adds a new row of cells below the last row.
- [func addRow(with: [NSCell])](./addrow%28with%29.md)
  Adds a new row of cells below the last row, using the specified cells.
- [func cellFrame(atRow: Int, column: Int) -> NSRect](./cellframe%28atrow,column%29.md)
  Returns the frame rectangle of the cell that would be drawn at the specified location.
- [var cellSize: NSSize](./cellsize.md)
  The size of each cell in the matrix.
- [func getNumberOfRows(UnsafeMutablePointer<Int>?, columns: UnsafeMutablePointer<Int>?)](./getnumberofrows%28_,columns%29.md)
  Obtains the number of rows and columns in the receiver.
- [func insertColumn(Int)](./insertcolumn%28_%29.md)
  Inserts a new column of cells at the specified location.
- [func insertColumn(Int, with: [NSCell]?)](./insertcolumn%28_,with%29.md)
  Inserts a new column of cells before the specified column, using the given cells.
- [func insertRow(Int)](./insertrow%28_%29.md)
  Inserts a new row of cells before the specified row.
- [func insertRow(Int, with: [NSCell]?)](./insertrow%28_,with%29.md)
  Inserts a new row of cells before the specified row, using the given cells.
- [var intercellSpacing: NSSize](./intercellspacing.md)
  The vertical and horizontal spacing between cells in the matrix.
- [func makeCell(atRow: Int, column: Int) -> NSCell](./makecell%28atrow,column%29.md)
  Creates a new cell at the location specified by the given row and column in the receiver.
- [var numberOfColumns: Int](./numberofcolumns.md)
  The number of columns in the matrix.
- [var numberOfRows: Int](./numberofrows.md)
  The number of rows in the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/sort(using:))*