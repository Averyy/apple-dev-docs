# init(frame:mode:cellClass:numberOfRows:numberOfColumns:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns a newly allocated matrix of the specified size using cells of the given class.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init(frame frameRect: NSRect, mode: NSMatrix.Mode, cellClass factoryId: AnyClass?, numberOfRows rowsHigh: Int, numberOfColumns colsWide: Int)
```

#### Return Value

The initialized instance of [`NSMatrix`](nsmatrix.md).

#### Discussion

This method is the designated initializer for matrices that add cells by creating instances of an [`NSCell`](nscell.md) subclass.

## Parameters

- `frameRect`: The matrix’s frame.
- `mode`: The tracking mode for the matrix; this can be one of the modes described in  .
- `factoryId`: The class to use for any cells that the matrix creates and uses. This can be obtained by sending a   message to the desired subclass of  .
- `rowsHigh`: The number of rows in the matrix.
- `colsWide`: The number of columns in the matrix.

## See Also

- [convenience init(frame: NSRect)](nsmatrix/init(frame:).md)
  Initializes a newly allocated matrix with the specified frame.
- [init(frame: NSRect, mode: NSMatrix.Mode, prototype: NSCell, numberOfRows: Int, numberOfColumns: Int)](nsmatrix/init(frame:mode:prototype:numberofrows:numberofcolumns:).md)
  Initializes and returns a newly allocated matrix of the specified size using the given cell as a prototype.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/init(frame:mode:cellclass:numberofrows:numberofcolumns:))*