# matrix(inColumn:)

**Framework**: AppKit  
**Kind**: method

Returns the matrix located in the specified column.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func matrix(inColumn column: Int) -> NSMatrix?
```

#### Return Value

The matrix located in the column.

## Parameters

- `column`: The column index of the matrix to obtain.

## See Also

- [func column(of: NSMatrix) -> Int](nsbrowser/column(of:).md)
  Returns the column number in which the given matrix is located.
- [func matrixClass() -> AnyClass](nsbrowser/matrixclass.md)
  Returns the matrix class used in the browser’s columns.
- [func setMatrixClass(AnyClass)](nsbrowser/setmatrixclass(_:).md)
  Sets the matrix class to be used in the browser’s columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/matrix(incolumn:))*