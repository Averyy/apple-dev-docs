# init(frame:mode:prototype:numberOfRows:numberOfColumns:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a newly allocated matrix of the specified size using the given cell as a prototype.

**Availability**:
- macOS

## Declaration

```swift
init(frame frameRect: NSRect, mode: NSMatrix.Mode, prototype cell: NSCell, numberOfRows rowsHigh: Int, numberOfColumns colsWide: Int)
```

```objc
- (instancetype) initWithFrame:(NSRect) frameRect mode:(NSMatrixMode) mode prototype:(NSCell *) cell numberOfRows:(NSInteger) rowsHigh numberOfColumns:(NSInteger) colsWide;
```

#### Discussion

This method is the designated initializer for matrices that add cells by copying an instance of an [`NSCell`](../nscell.md) subclass.

## Parameters

- `frameRect`: The matrix’s frame.
- `mode`: The tracking mode for the matrix; this can be one of the modes described in [`NSMatrix.Mode`](./mode-swift.enum.md).
- `cell`: An instance of a subclass of [`NSCell`](../nscell.md), which the new matrix copies when it creates new cells.
- `rowsHigh`: The number of rows in the matrix.
- `colsWide`: The number of columns in the matrix.

## See Also

### Initializing an NSMatrix Object
- [convenience init(frame: NSRect)](./init%28frame%29.md)
  Initializes a newly allocated matrix with the specified frame.
- [init(frame: NSRect, mode: NSMatrix.Mode, cellClass: AnyClass?, numberOfRows: Int, numberOfColumns: Int)](./init%28frame,mode,cellclass,numberofrows,numberofcolumns%29.md)
  Initializes and returns a newly allocated matrix of the specified size using cells of the given class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/init(frame:mode:prototype:numberofrows:numberofcolumns:))*