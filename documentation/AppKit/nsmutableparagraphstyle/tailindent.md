# tailIndent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The trailing indentation of the paragraph.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var tailIndent: CGFloat { get set }
```

```objc
@property CGFloat tailIndent;
```

## Discussion

If positive, this value is the distance from the leading margin (for example, the left margin in left-to-right text). If 0 or negative, it’s the distance from the trailing margin.

For example, a paragraph style designed to fit exactly in a 2-inch wide container has a head indent of 0.0 and a tail indent of 0.0. One designed to fit with a quarter-inch margin has a head indent of 0.25 and a tail indent of –0.25.

## See Also

### Setting style information
- [func setParagraphStyle(NSParagraphStyle)](./setparagraphstyle%28_%29.md)
  Replaces the subattributes of the paragraph with those in the specified paragraph style object.
- [var alignment: NSTextAlignment](./alignment.md)
  The text alignment of the paragraph.
- [var firstLineHeadIndent: CGFloat](./firstlineheadindent.md)
  The indentation of the first line of the paragraph.
- [var headIndent: CGFloat](./headindent.md)
  The indentation of the paragraph’s lines other than the first.
- [var lineHeightMultiple: CGFloat](./lineheightmultiple.md)
  The line height multiple.
- [var maximumLineHeight: CGFloat](./maximumlineheight.md)
  The paragraph’s maximum line height.
- [var minimumLineHeight: CGFloat](./minimumlineheight.md)
  The paragraph’s minimum line height.
- [var lineSpacing: CGFloat](./linespacing.md)
  The distance in points between the bottom of one line fragment and the top of the next.
- [var paragraphSpacing: CGFloat](./paragraphspacing.md)
  The space after the end of the paragraph.
- [var paragraphSpacingBefore: CGFloat](./paragraphspacingbefore.md)
  The distance between the paragraph’s top and the beginning of its text content.
- [var baseWritingDirection: NSWritingDirection](./basewritingdirection.md)
  The base writing direction for the paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/tailindent)*