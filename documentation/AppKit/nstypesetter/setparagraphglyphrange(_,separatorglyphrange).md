# setParagraphGlyphRange(_:separatorGlyphRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the current glyph range being processed.

**Availability**:
- macOS

## Declaration

```swift
func setParagraphGlyphRange(_ paragraphRange: NSRange, separatorGlyphRange paragraphSeparatorRange: NSRange)
```

```objc
- (void) setParagraphGlyphRange:(NSRange) paragraphRange separatorGlyphRange:(NSRange) paragraphSeparatorRange;
```

## Parameters

- `paragraphRange`: The current glyph range being processed.
- `paragraphSeparatorRange`: The range of the paragraph separator character or characters.

## See Also

### Accessing paragraph typesetting information
- [var currentParagraphStyle: NSParagraphStyle?](./currentparagraphstyle.md)
  Returns the paragraph style object for the text being typeset.
- [var attributedString: NSAttributedString?](./attributedstring.md)
  Returns the text backing store, usually an instance of `NSTextStorage`.
- [var paragraphGlyphRange: NSRange](./paragraphglyphrange.md)
  Returns the glyph range currently being processed.
- [var paragraphSeparatorGlyphRange: NSRange](./paragraphseparatorglyphrange.md)
  Returns the current paragraph separator range.
- [var paragraphCharacterRange: NSRange](./paragraphcharacterrange.md)
  Returns the character range currently being processed.
- [var paragraphSeparatorCharacterRange: NSRange](./paragraphseparatorcharacterrange.md)
  Returns the current paragraph separator character range.
- [var attributesForExtraLineFragment: [NSAttributedString.Key : Any]](./attributesforextralinefragment.md)
  Returns the attributes used to lay out the extra line fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/setparagraphglyphrange(_:separatorglyphrange:))*