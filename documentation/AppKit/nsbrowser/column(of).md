# column(of:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the column number in which the given matrix is located.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use the item-based `NSBrowser` instead.

## Declaration

```swift
func column(of matrix: NSMatrix) -> Int
```

```objc
- (NSInteger) columnOfMatrix:(NSMatrix *) matrix;
```

#### Return Value

The index of the column in which the specified matrix appears.

## Parameters

- `matrix`: The matrix for which to return the column number.

## See Also

### Deprecated methods
- [func matrix(inColumn: Int) -> NSMatrix?](./matrix%28incolumn%29.md)
  Returns the matrix located in the specified column.
- [func matrixClass() -> AnyClass](./matrixclass%28%29.md)
  Returns the matrix class used in the browser’s columns.
- [func setMatrixClass(AnyClass)](./setmatrixclass%28_%29.md)
  Sets the matrix class to be used in the browser’s columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/column(of:))*