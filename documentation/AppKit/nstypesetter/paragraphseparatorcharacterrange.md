# paragraphSeparatorCharacterRange

**Framework**: AppKit  
**Kind**: property

Returns the current paragraph separator character range.

**Availability**:
- macOS ?+

## Declaration

```swift
var paragraphSeparatorCharacterRange: NSRange { get }
```

#### Return Value

The current paragraph separator character range, which is the full range that contains the current character range and that extends from one paragraph separator character to the next.

## See Also

- [var currentParagraphStyle: NSParagraphStyle?](nstypesetter/currentparagraphstyle.md)
  Returns the paragraph style object for the text being typeset.
- [var attributedString: NSAttributedString?](nstypesetter/attributedstring.md)
  Returns the text backing store, usually an instance of `NSTextStorage`.
- [func setParagraphGlyphRange(NSRange, separatorGlyphRange: NSRange)](nstypesetter/setparagraphglyphrange(_:separatorglyphrange:).md)
  Sets the current glyph range being processed.
- [var paragraphGlyphRange: NSRange](nstypesetter/paragraphglyphrange.md)
  Returns the glyph range currently being processed.
- [var paragraphSeparatorGlyphRange: NSRange](nstypesetter/paragraphseparatorglyphrange.md)
  Returns the current paragraph separator range.
- [var paragraphCharacterRange: NSRange](nstypesetter/paragraphcharacterrange.md)
  Returns the character range currently being processed.
- [var attributesForExtraLineFragment: [NSAttributedString.Key : Any]](nstypesetter/attributesforextralinefragment.md)
  Returns the attributes used to lay out the extra line fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/paragraphseparatorcharacterrange)*