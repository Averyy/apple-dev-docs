# column(of:)

**Framework**: AppKit  
**Kind**: method

Returns the column number in which the given matrix is located.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func column(of matrix: NSMatrix) -> Int
```

#### Return Value

The index of the column in which the specified matrix appears.

## Parameters

- `matrix`: The matrix for which to return the column number.

## See Also

- [func matrix(inColumn: Int) -> NSMatrix?](nsbrowser/matrix(incolumn:).md)
  Returns the matrix located in the specified column.
- [func matrixClass() -> AnyClass](nsbrowser/matrixclass.md)
  Returns the matrix class used in the browser’s columns.
- [func setMatrixClass(AnyClass)](nsbrowser/setmatrixclass(_:).md)
  Sets the matrix class to be used in the browser’s columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/column(of:))*