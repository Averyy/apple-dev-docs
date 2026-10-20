# paragraphGlyphRange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current glyph range being processed.

**Availability**:
- macOS

## Declaration

```swift
var paragraphGlyphRange: NSRange { get }
```

```objc
@property (readonly) NSRange paragraphGlyphRange;
```

## See Also

### Accessing paragraph information
- [var attributedString: NSAttributedString?](./attributedstring.md)
  The backing store that contains the text on which this typesetter operates.
- [func setParagraphGlyphRange(NSRange, separatorGlyphRange: NSRange)](./setparagraphglyphrange%28_,separatorglyphrange%29.md)
  Sets the glyph range being processed and the paragraph separator glyph range (the range of the paragraph separator character or characters).
- [var paragraphSeparatorGlyphRange: NSRange](./paragraphseparatorglyphrange.md)
  The current paragraph separator range that contains the current glyph range and extends from one paragraph separator character to the next.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/paragraphglyphrange)*