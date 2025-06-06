# draw(with:options:)

**Framework**: Foundation  
**Kind**: method

Draws the attributed string with the specified options within the specified rectangle in the current graphics context.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func draw(with rect: NSRect, options: NSString.DrawingOptions = [])
```

#### Discussion

The `rect` argument’s origin field specifies the rendering origin. The point is interpreted as the baseline origin by default. With `NSStringDrawingUsesLineFragmentOrigin`, it is interpreted as the upper left corner of the line fragment rect. The size field specifies the text container size. The width part of the size field specifies the maximum line fragment width if larger than `0.0`. The height defines the maximum size that can be occupied with text if larger than `0.0` and `NSStringDrawingUsesLineFragmentOrigin` is specified. If `NSStringDrawingUsesLineFragmentOrigin` is not specified, height is ignored and considered to be single-line rendering (`NSLineBreakByWordWrapping` and `NSLineBreakByCharWrapping` are treated as `NSLineBreakByClipping`).

You should only invoke this method when there is a current graphics context.

## Parameters

- `rect`: The rectangle specifies the rendering origin in the current graphics context.
- `options`: The string drawing options. See   for the available options.

## See Also

- [func url(at: Int, effectiveRange: NSRangePointer) -> URL?](nsattributedstring/url(at:effectiverange:).md)
  Returns a URL, either from a link attribute or from text at the specified location that appears to be a URL string, for use in automatic link detection.
- [func boundingRect(with: NSSize, options: NSString.DrawingOptions) -> NSRect](nsattributedstring/boundingrect(with:options:).md)
  Calculates and returns a bounding rectangle for the attributed string using the options specified within the specified rectangle in the current graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/draw(with:options:))*