# currentParagraphStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the paragraph style object for the text being typeset.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var currentParagraphStyle: NSParagraphStyle? { get }
```

```objc
@property (copy, readonly, nullable) NSParagraphStyle * currentParagraphStyle;
```

#### Return Value

The paragraph style object for the text being typeset. This value is valid only while the typesetter is performing layout.

## See Also

### Accessing paragraph typesetting information
- [var attributedString: NSAttributedString?](./attributedstring.md)
  Returns the text backing store, usually an instance of `NSTextStorage`.
- [func setParagraphGlyphRange(NSRange, separatorGlyphRange: NSRange)](./setparagraphglyphrange%28_,separatorglyphrange%29.md)
  Sets the current glyph range being processed.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/currentparagraphstyle)*