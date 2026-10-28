# paragraphSeparatorGlyphRange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the current paragraph separator range.

**Availability**:
- macOS

## Declaration

```swift
var paragraphSeparatorGlyphRange: NSRange { get }
```

```objc
@property (readonly) NSRange paragraphSeparatorGlyphRange;
```

## Return Value

The current paragraph separator range, which is the full range that contains the current glyph range and that extends from one paragraph separator character to the next.

## See Also

### Accessing paragraph typesetting information
- [var currentParagraphStyle: NSParagraphStyle?](./currentparagraphstyle.md)
  Returns the paragraph style object for the text being typeset.
- [var attributedString: NSAttributedString?](./attributedstring.md)
  Returns the text backing store, usually an instance of `NSTextStorage`.
- [func setParagraphGlyphRange(NSRange, separatorGlyphRange: NSRange)](./setparagraphglyphrange%28_,separatorglyphrange%29.md)
  Sets the current glyph range being processed.
- [var paragraphGlyphRange: NSRange](./paragraphglyphrange.md)
  Returns the glyph range currently being processed.
- [var paragraphCharacterRange: NSRange](./paragraphcharacterrange.md)
  Returns the character range currently being processed.
- [var paragraphSeparatorCharacterRange: NSRange](./paragraphseparatorcharacterrange.md)
  Returns the current paragraph separator character range.
- [var attributesForExtraLineFragment: [NSAttributedString.Key : Any]](./attributesforextralinefragment.md)
  Returns the attributes used to lay out the extra line fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/paragraphseparatorglyphrange)*