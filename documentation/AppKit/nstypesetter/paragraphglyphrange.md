# paragraphGlyphRange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the glyph range currently being processed.

**Availability**:
- macOS

## Declaration

```swift
var paragraphGlyphRange: NSRange { get }
```

```objc
@property (readonly) NSRange paragraphGlyphRange;
```

#### Return Value

The glyph range currently being processed.

## See Also

### Accessing paragraph typesetting information
- [var currentParagraphStyle: NSParagraphStyle?](./currentparagraphstyle.md)
  Returns the paragraph style object for the text being typeset.
- [var attributedString: NSAttributedString?](./attributedstring.md)
  Returns the text backing store, usually an instance of `NSTextStorage`.
- [func setParagraphGlyphRange(NSRange, separatorGlyphRange: NSRange)](./setparagraphglyphrange%28_,separatorglyphrange%29.md)
  Sets the current glyph range being processed.
- [var paragraphSeparatorGlyphRange: NSRange](./paragraphseparatorglyphrange.md)
  Returns the current paragraph separator range.
- [var paragraphCharacterRange: NSRange](./paragraphcharacterrange.md)
  Returns the character range currently being processed.
- [var paragraphSeparatorCharacterRange: NSRange](./paragraphseparatorcharacterrange.md)
  Returns the current paragraph separator character range.
- [var attributesForExtraLineFragment: [NSAttributedString.Key : Any]](./attributesforextralinefragment.md)
  Returns the attributes used to lay out the extra line fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/paragraphglyphrange)*