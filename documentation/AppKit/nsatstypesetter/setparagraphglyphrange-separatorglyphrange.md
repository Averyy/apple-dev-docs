# setParagraphGlyphRange(_:separatorGlyphRange:)

**Framework**: AppKit  
**Kind**: method

Sets the glyph range being processed and the paragraph separator glyph range (the range of the paragraph separator character or characters).

**Availability**:
- macOS ?+

## Declaration

```swift
func setParagraphGlyphRange(_ paragraphRange: NSRange, separatorGlyphRange paragraphSeparatorRange: NSRange)
```

## Parameters

- `paragraphRange`: The glyph range that becomes current.
- `paragraphSeparatorRange`: The paragraph separator glyph range that becomes current.

## See Also

- [var attributedString: NSAttributedString?](nsatstypesetter/attributedstring.md)
  The backing store that contains the text on which this typesetter operates.
- [var paragraphGlyphRange: NSRange](nsatstypesetter/paragraphglyphrange.md)
  The current glyph range being processed.
- [var paragraphSeparatorGlyphRange: NSRange](nsatstypesetter/paragraphseparatorglyphrange.md)
  The current paragraph separator range that contains the current glyph range and extends from one paragraph separator character to the next.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/setparagraphglyphrange(_:separatorglyphrange:))*