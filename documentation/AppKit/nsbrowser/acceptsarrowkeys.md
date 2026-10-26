# acceptsArrowKeys

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Indicates whether the browser allows navigation using the arrow keys.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: There is no replacement.

## Declaration

```objc
- (BOOL) acceptsArrowKeys;
```

#### Return Value

[`true`](../../Swift/true.md) if the arrow keys are enabled; otherwise, [`false`](../../Swift/false.md).

## See Also

### Deprecated methods
- [- updateScroller](./updatescroller.md)
  Updates the horizontal scroller to reflect column positions.
- [- scrollViaScroller:](./scrollviascroller_.md)
  Scrolls columns left or right based on an `NSScroller`.
- [- displayAllColumns](./displayallcolumns.md)
  Updates the browser to display all loaded columns.
- [- displayColumn:](./displaycolumn_.md)
  Updates the browser to display the given column.
- [func column(of: NSMatrix) -> Int](./column%28of%29.md)
  Returns the column number in which the given matrix is located.
- [func matrix(inColumn: Int) -> NSMatrix?](./matrix%28incolumn%29.md)
  Returns the matrix located in the specified column.
- [func matrixClass() -> AnyClass](./matrixclass%28%29.md)
  Returns the matrix class used in the browser’s columns.
- [func setMatrixClass(AnyClass)](./setmatrixclass%28_%29.md)
  Sets the matrix class to be used in the browser’s columns.
- [- setAcceptsArrowKeys:](./setacceptsarrowkeys_.md)
  Specifies whether the browser allows navigation using the arrow keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/acceptsarrowkeys)*