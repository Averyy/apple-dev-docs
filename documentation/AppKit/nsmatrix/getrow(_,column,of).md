# getRow(_:column:of:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Searches the receiver for the specified cell and returns the row and column of the cell

**Availability**:
- macOS

## Declaration

```swift
func getRow(_ row: UnsafeMutablePointer<Int>, column col: UnsafeMutablePointer<Int>, of cell: NSCell) -> Bool
```

```objc
- (BOOL) getRow:(NSInteger *) row column:(NSInteger *) col ofCell:(NSCell *) cell;
```

#### Return Value

[`true`](../../Swift/true.md) if the cell is one of the cells in the receiver, [`false`](../../Swift/false.md) otherwise.

#### Discussion

.

## Parameters

- `row`: On return, the row in which the cell is located.
- `col`: On return, the column in which the cell is located.
- `cell`: The cell to locate within the matrix.

## See Also

### Finding Matrix Coordinates
- [func getRow(UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, for: NSPoint) -> Bool](./getrow%28_,column,for%29.md)
  Indicates whether the specified point lies within one of the cells of the matrix and returns the location of the cell within which the point lies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/getrow(_:column:of:))*