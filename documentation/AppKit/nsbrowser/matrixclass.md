# matrixClass()

**Framework**: AppKit  
**Kind**: method

Returns the matrix class used in the browser’s columns.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func matrixClass() -> AnyClass
```

#### Return Value

The class of `NSMatrix` used in the browser’s columns.

## See Also

- [func column(of: NSMatrix) -> Int](nsbrowser/column(of:).md)
  Returns the column number in which the given matrix is located.
- [func matrix(inColumn: Int) -> NSMatrix?](nsbrowser/matrix(incolumn:).md)
  Returns the matrix located in the specified column.
- [func setMatrixClass(AnyClass)](nsbrowser/setmatrixclass(_:).md)
  Sets the matrix class to be used in the browser’s columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/matrixclass())*