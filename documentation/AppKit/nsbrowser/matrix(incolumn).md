# matrix(inColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the matrix located in the specified column.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use the item-based `NSBrowser` instead.

## Declaration

```swift
func matrix(inColumn column: Int) -> NSMatrix?
```

```objc
- (NSMatrix *) matrixInColumn:(NSInteger) column;
```

#### Return Value

The matrix located in the column.

## Parameters

- `column`: The column index of the matrix to obtain.

## See Also

### Deprecated methods
- [func column(of: NSMatrix) -> Int](./column%28of%29.md)
  Returns the column number in which the given matrix is located.
- [func matrixClass() -> AnyClass](./matrixclass%28%29.md)
  Returns the matrix class used in the browser’s columns.
- [func setMatrixClass(AnyClass)](./setmatrixclass%28_%29.md)
  Sets the matrix class to be used in the browser’s columns.
- [- updateScroller](./updatescroller.md)
  Updates the horizontal scroller to reflect column positions.
- [- scrollViaScroller:](./scrollviascroller_.md)
  Scrolls columns left or right based on an `NSScroller`.
- [- displayAllColumns](./displayallcolumns.md)
  Updates the browser to display all loaded columns.
- [- displayColumn:](./displaycolumn_.md)
  Updates the browser to display the given column.
- [- acceptsArrowKeys](./acceptsarrowkeys.md)
  Indicates whether the browser allows navigation using the arrow keys.
- [- setAcceptsArrowKeys:](./setacceptsarrowkeys_.md)
  Specifies whether the browser allows navigation using the arrow keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/matrix(incolumn:))*