# paragraphCharacterRange

**Framework**: AppKit  
**Kind**: property

Returns the character range currently being processed.

**Availability**:
- macOS ?+

## Declaration

```swift
var paragraphCharacterRange: NSRange { get }
```

#### Return Value

The character range currently being processed.

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
- [var paragraphSeparatorCharacterRange: NSRange](nstypesetter/paragraphseparatorcharacterrange.md)
  Returns the current paragraph separator character range.
- [var attributesForExtraLineFragment: [NSAttributedString.Key : Any]](nstypesetter/attributesforextralinefragment.md)
  Returns the attributes used to lay out the extra line fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/paragraphcharacterrange)*