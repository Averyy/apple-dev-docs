# setMatrixClass(_:)

**Framework**: AppKit  
**Kind**: method

Sets the matrix class to be used in the browser’s columns.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func setMatrixClass(_ factoryId: AnyClass)
```

## Parameters

- `factoryId`: The matrix class (  or an   subclass) used in the browser’s columns.

## See Also

- [func column(of: NSMatrix) -> Int](nsbrowser/column(of:).md)
  Returns the column number in which the given matrix is located.
- [func matrix(inColumn: Int) -> NSMatrix?](nsbrowser/matrix(incolumn:).md)
  Returns the matrix located in the specified column.
- [func matrixClass() -> AnyClass](nsbrowser/matrixclass.md)
  Returns the matrix class used in the browser’s columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/setmatrixclass(_:))*