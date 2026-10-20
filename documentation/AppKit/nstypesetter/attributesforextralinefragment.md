# attributesForExtraLineFragment

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the attributes used to lay out the extra line fragment.

**Availability**:
- macOS

## Declaration

```swift
var attributesForExtraLineFragment: [NSAttributedString.Key : Any] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,id> * attributesForExtraLineFragment;
```

#### Return Value

A dictionary of attributes used to lay out the extra line fragment.

#### Discussion

The default implementation tries to use the `NSTextView` method [`typingAttributes`](../nstextview/typingattributes.md) if possible; otherwise, it uses the attributes for the last character.

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
- [var paragraphSeparatorGlyphRange: NSRange](./paragraphseparatorglyphrange.md)
  Returns the current paragraph separator range.
- [var paragraphCharacterRange: NSRange](./paragraphcharacterrange.md)
  Returns the character range currently being processed.
- [var paragraphSeparatorCharacterRange: NSRange](./paragraphseparatorcharacterrange.md)
  Returns the current paragraph separator character range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/attributesforextralinefragment)*