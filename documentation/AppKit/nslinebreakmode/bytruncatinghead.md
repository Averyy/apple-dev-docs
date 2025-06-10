# NSLineBreakMode.byTruncatingHead

**Framework**: AppKit  
**Kind**: case

The value that indicates that a line displays so that the end fits in the container and an ellipsis glyph indicates the missing text at the beginning of the line.

**Availability**:
- macOS 10.0+

## Declaration

```swift
case byTruncatingHead
```

#### Discussion

Although this mode works for multiline text, it’s more often used for single line text.

## See Also

- [NSLineBreakMode.byWordWrapping](nslinebreakmode/bywordwrapping.md)
  The value that indicates wrapping occurs at word boundaries, unless the word doesn’t fit on a single line.
- [NSLineBreakMode.byCharWrapping](nslinebreakmode/bycharwrapping.md)
  The value that indicates wrapping occurs before the first character that doesn’t fit.
- [NSLineBreakMode.byClipping](nslinebreakmode/byclipping.md)
  The value that indicates lines don’t extend past the edge of the text container.
- [NSLineBreakMode.byTruncatingTail](nslinebreakmode/bytruncatingtail.md)
  The value that indicates a line displays so that the beginning fits in the container and an ellipsis glyph indicates the missing text at the end of the line.
- [NSLineBreakMode.byTruncatingMiddle](nslinebreakmode/bytruncatingmiddle.md)
  The value that indicates that a line displays so that the beginning and end fit in the container and an ellipsis glyph indicates the missing text in the middle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslinebreakmode/bytruncatinghead)*