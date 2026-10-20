# matrixClass()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the matrix class used in the browser’s columns.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use the item-based `NSBrowser` instead.

## Declaration

```swift
func matrixClass() -> AnyClass
```

```objc
- (Class) matrixClass;
```

#### Return Value

The class of `NSMatrix` used in the browser’s columns.

## See Also

### Deprecated methods
- [func column(of: NSMatrix) -> Int](./column%28of%29.md)
  Returns the column number in which the given matrix is located.
- [func matrix(inColumn: Int) -> NSMatrix?](./matrix%28incolumn%29.md)
  Returns the matrix located in the specified column.
- [func setMatrixClass(AnyClass)](./setmatrixclass%28_%29.md)
  Sets the matrix class to be used in the browser’s columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/matrixclass())*