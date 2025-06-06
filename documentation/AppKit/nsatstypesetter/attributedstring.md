# attributedString

**Framework**: AppKit  
**Kind**: property

The backing store that contains the text on which this typesetter operates.

**Availability**:
- macOS ?+

## Declaration

```swift
unowned(unsafe) var attributedString: NSAttributedString? { get set }
```

## See Also

- [func setParagraphGlyphRange(NSRange, separatorGlyphRange: NSRange)](nsatstypesetter/setparagraphglyphrange(_:separatorglyphrange:).md)
  Sets the glyph range being processed and the paragraph separator glyph range (the range of the paragraph separator character or characters).
- [var paragraphGlyphRange: NSRange](nsatstypesetter/paragraphglyphrange.md)
  The current glyph range being processed.
- [var paragraphSeparatorGlyphRange: NSRange](nsatstypesetter/paragraphseparatorglyphrange.md)
  The current paragraph separator range that contains the current glyph range and extends from one paragraph separator character to the next.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/attributedstring)*