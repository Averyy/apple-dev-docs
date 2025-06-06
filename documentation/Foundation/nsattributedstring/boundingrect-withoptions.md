# boundingRect(with:options:)

**Framework**: Foundation  
**Kind**: method

Calculates and returns a bounding rectangle for the attributed string using the options specified within the specified rectangle in the current graphics context.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func boundingRect(with size: NSSize, options: NSString.DrawingOptions = []) -> NSRect
```

#### Return Value

The bounding rectangle in the current graphics context.

#### Discussion

The origin of the rectangle returned from this method is the first glyph origin.

## Parameters

- `size`: The size of the rectangle to draw in.
- `options`: The string drawing options. See   for the possible values.

## See Also

- [func url(at: Int, effectiveRange: NSRangePointer) -> URL?](nsattributedstring/url(at:effectiverange:).md)
  Returns a URL, either from a link attribute or from text at the specified location that appears to be a URL string, for use in automatic link detection.
- [func draw(with: NSRect, options: NSString.DrawingOptions)](nsattributedstring/draw(with:options:).md)
  Draws the attributed string with the specified options within the specified rectangle in the current graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/boundingrect(with:options:))*