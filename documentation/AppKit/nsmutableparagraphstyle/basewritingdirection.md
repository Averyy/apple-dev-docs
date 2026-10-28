# baseWritingDirection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The base writing direction for the paragraph.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var baseWritingDirection: NSWritingDirection { get set }
```

```objc
@property NSWritingDirection baseWritingDirection;
```

## Discussion

If you specify [`NSWritingDirection.natural`](../nswritingdirection/natural.md), the receiver resolves the writing direction to either [`NSWritingDirection.leftToRight`](../nswritingdirection/lefttoright.md) or [`NSWritingDirection.rightToLeft`](../nswritingdirection/righttoleft.md), depending on the direction for the user’s language preference setting.

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
- [var tailIndent: CGFloat](./tailindent.md)
  The trailing indentation of the paragraph.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/basewritingdirection)*