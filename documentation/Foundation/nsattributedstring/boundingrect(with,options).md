# boundingRect(with:options:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Calculates and returns a bounding rectangle for the attributed string using the options specified within the specified rectangle in the current graphics context.

**Availability**:
- macOS 10.0+ - Deprecated in 27.2

> **Deprecated**: Use [`boundingRect(with:options:context:)`](./boundingrect%28with,options,context%29.md) instead.

## Declaration

```swift
func boundingRect(with size: NSSize, options: NSString.DrawingOptions = []) -> NSRect
```

```objc
- (NSRect) boundingRectWithSize:(NSSize) size options:(NSStringDrawingOptions) options;
```

## Return Value

The bounding rectangle in the current graphics context.

## Discussion

The origin of the rectangle returned from this method is the first glyph origin.

## Parameters

- `size`: The size of the rectangle to draw in.
- `options`: The string drawing options. See [`NSStringDrawingOptions`](../../UIKit/nsstringdrawingoptions.md) for the possible values.

## See Also

### Deprecated Instance Methods
- [func url(at: Int, effectiveRange: NSRangePointer) -> URL?](./url%28at,effectiverange%29.md)
  Returns a URL, either from a link attribute or from text at the specified location that appears to be a URL string, for use in automatic link detection.
- [func draw(with: NSRect, options: NSString.DrawingOptions)](./draw%28with,options%29.md)
  Draws the attributed string with the specified options within the specified rectangle in the current graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/boundingrect(with:options:))*