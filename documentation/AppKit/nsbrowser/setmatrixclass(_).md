# setMatrixClass(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the matrix class to be used in the browser’s columns.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use the item-based `NSBrowser` instead.

## Declaration

```swift
func setMatrixClass(_ factoryId: AnyClass)
```

```objc
- (void) setMatrixClass:(Class) factoryId;
```

## Parameters

- `factoryId`: The matrix class (`NSMatrix` or an `NSMatrix` subclass) used in the browser’s columns.

## See Also

### Deprecated methods
- [func column(of: NSMatrix) -> Int](./column%28of%29.md)
  Returns the column number in which the given matrix is located.
- [func matrix(inColumn: Int) -> NSMatrix?](./matrix%28incolumn%29.md)
  Returns the matrix located in the specified column.
- [func matrixClass() -> AnyClass](./matrixclass%28%29.md)
  Returns the matrix class used in the browser’s columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/setmatrixclass(_:))*