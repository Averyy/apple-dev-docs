# paragraphSeparatorGlyphRange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current paragraph separator range that contains the current glyph range and extends from one paragraph separator character to the next.

**Availability**:
- macOS

## Declaration

```swift
var paragraphSeparatorGlyphRange: NSRange { get }
```

```objc
@property (readonly) NSRange paragraphSeparatorGlyphRange;
```

## See Also

### Accessing paragraph information
- [var attributedString: NSAttributedString?](./attributedstring.md)
  The backing store that contains the text on which this typesetter operates.
- [func setParagraphGlyphRange(NSRange, separatorGlyphRange: NSRange)](./setparagraphglyphrange%28_,separatorglyphrange%29.md)
  Sets the glyph range being processed and the paragraph separator glyph range (the range of the paragraph separator character or characters).
- [var paragraphGlyphRange: NSRange](./paragraphglyphrange.md)
  The current glyph range being processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/paragraphseparatorglyphrange)*