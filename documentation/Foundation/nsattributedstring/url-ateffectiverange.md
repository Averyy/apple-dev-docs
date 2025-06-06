# url(at:effectiveRange:)

**Framework**: Foundation  
**Kind**: method

Returns a URL, either from a link attribute or from text at the specified location that appears to be a URL string, for use in automatic link detection.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func url(at location: Int, effectiveRange: NSRangePointer) -> URL?
```

#### Return Value

The URL found at `location`.

## Parameters

- `location`: The character index in the string at which the method checks for a link.
- `effectiveRange`: The actual range covered by the link attribute or URL string, or of non-URL text if no apparent URL is found.

## See Also

- [func draw(with: NSRect, options: NSString.DrawingOptions)](nsattributedstring/draw(with:options:).md)
  Draws the attributed string with the specified options within the specified rectangle in the current graphics context.
- [func boundingRect(with: NSSize, options: NSString.DrawingOptions) -> NSRect](nsattributedstring/boundingrect(with:options:).md)
  Calculates and returns a bounding rectangle for the attributed string using the options specified within the specified rectangle in the current graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/url(at:effectiverange:))*