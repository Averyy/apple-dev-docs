# currentParagraphStyle

**Framework**: AppKit  
**Kind**: property

Returns the paragraph style object for the text being typeset.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
var currentParagraphStyle: NSParagraphStyle? { get }
```

#### Return Value

The paragraph style object for the text being typeset. This value is valid only while the typesetter is performing layout.

## See Also

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
- [var paragraphSeparatorCharacterRange: NSRange](nstypesetter/paragraphseparatorcharacterrange.md)
  Returns the current paragraph separator character range.
- [var attributesForExtraLineFragment: [NSAttributedString.Key : Any]](nstypesetter/attributesforextralinefragment.md)
  Returns the attributes used to lay out the extra line fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/currentparagraphstyle)*