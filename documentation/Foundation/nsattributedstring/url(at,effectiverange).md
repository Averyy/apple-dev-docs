# url(at:effectiveRange:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a URL, either from a link attribute or from text at the specified location that appears to be a URL string, for use in automatic link detection.

**Availability**:
- macOS 10.5+ - Deprecated in 10.11

> **Deprecated**: Use an [`NSDataDetector`](../nsdatadetector.md) object instead.

## Declaration

```swift
func url(at location: Int, effectiveRange: NSRangePointer) -> URL?
```

```objc
- (NSURL *) URLAtIndex:(NSUInteger) location effectiveRange:(NSRangePointer) effectiveRange;
```

#### Return Value

The URL found at `location`.

## Parameters

- `location`: The character index in the string at which the method checks for a link.
- `effectiveRange`: The actual range covered by the link attribute or URL string, or of non-URL text if no apparent URL is found.

## See Also

### Deprecated Instance Methods
- [func draw(with: NSRect, options: NSString.DrawingOptions)](./draw%28with,options%29.md)
  Draws the attributed string with the specified options within the specified rectangle in the current graphics context.
- [func boundingRect(with: NSSize, options: NSString.DrawingOptions) -> NSRect](./boundingrect%28with,options%29.md)
  Calculates and returns a bounding rectangle for the attributed string using the options specified within the specified rectangle in the current graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/url(at:effectiverange:))*