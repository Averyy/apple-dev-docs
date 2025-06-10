# NSLineBreakMode.byTruncatingMiddle

**Framework**: AppKit  
**Kind**: case

The value that indicates that a line displays so that the beginning and end fit in the container and an ellipsis glyph indicates the missing text in the middle.

**Availability**:
- macOS 10.0+

## Declaration

```swift
case byTruncatingMiddle
```

#### Discussion

Use this mode for single-line layout; using it with multiline text truncates the text into a single line.

## See Also

- [NSLineBreakMode.byWordWrapping](nslinebreakmode/bywordwrapping.md)
  The value that indicates wrapping occurs at word boundaries, unless the word doesn’t fit on a single line.
- [NSLineBreakMode.byCharWrapping](nslinebreakmode/bycharwrapping.md)
  The value that indicates wrapping occurs before the first character that doesn’t fit.
- [NSLineBreakMode.byClipping](nslinebreakmode/byclipping.md)
  The value that indicates lines don’t extend past the edge of the text container.
- [NSLineBreakMode.byTruncatingHead](nslinebreakmode/bytruncatinghead.md)
  The value that indicates that a line displays so that the end fits in the container and an ellipsis glyph indicates the missing text at the beginning of the line.
- [NSLineBreakMode.byTruncatingTail](nslinebreakmode/bytruncatingtail.md)
  The value that indicates a line displays so that the beginning fits in the container and an ellipsis glyph indicates the missing text at the end of the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslinebreakmode/bytruncatingmiddle)*