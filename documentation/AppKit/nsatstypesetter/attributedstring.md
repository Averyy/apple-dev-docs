# attributedString

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The backing store that contains the text on which this typesetter operates.

**Availability**:
- macOS

## Declaration

```swift
unowned(unsafe) var attributedString: NSAttributedString? { get set }
```

```objc
@property (assign, nullable) NSAttributedString * attributedString;
```

## See Also

### Accessing paragraph information
- [func setParagraphGlyphRange(NSRange, separatorGlyphRange: NSRange)](./setparagraphglyphrange%28_,separatorglyphrange%29.md)
  Sets the glyph range being processed and the paragraph separator glyph range (the range of the paragraph separator character or characters).
- [var paragraphGlyphRange: NSRange](./paragraphglyphrange.md)
  The current glyph range being processed.
- [var paragraphSeparatorGlyphRange: NSRange](./paragraphseparatorglyphrange.md)
  The current paragraph separator range that contains the current glyph range and extends from one paragraph separator character to the next.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/attributedstring)*