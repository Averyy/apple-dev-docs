# lineHeightMultiple

**Framework**: AppKit  
**Kind**: property

The line height multiple.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var lineHeightMultiple: CGFloat { get set }
```

#### Discussion

The natural line height of the receiver is multiplied by this factor (if positive) before being constrained by minimum and maximum line height. The default value of this property is 0.0.

## See Also

- [func setParagraphStyle(NSParagraphStyle)](nsmutableparagraphstyle/setparagraphstyle(_:).md)
  Replaces the subattributes of the paragraph with those in the specified paragraph style object.
- [var alignment: NSTextAlignment](nsmutableparagraphstyle/alignment.md)
  The text alignment of the paragraph.
- [var firstLineHeadIndent: CGFloat](nsmutableparagraphstyle/firstlineheadindent.md)
  The indentation of the first line of the paragraph.
- [var headIndent: CGFloat](nsmutableparagraphstyle/headindent.md)
  The indentation of the paragraph’s lines other than the first.
- [var tailIndent: CGFloat](nsmutableparagraphstyle/tailindent.md)
  The trailing indentation of the paragraph.
- [var maximumLineHeight: CGFloat](nsmutableparagraphstyle/maximumlineheight.md)
  The paragraph’s maximum line height.
- [var minimumLineHeight: CGFloat](nsmutableparagraphstyle/minimumlineheight.md)
  The paragraph’s minimum line height.
- [var lineSpacing: CGFloat](nsmutableparagraphstyle/linespacing.md)
  The distance in points between the bottom of one line fragment and the top of the next.
- [var paragraphSpacing: CGFloat](nsmutableparagraphstyle/paragraphspacing.md)
  The space after the end of the paragraph.
- [var paragraphSpacingBefore: CGFloat](nsmutableparagraphstyle/paragraphspacingbefore.md)
  The distance between the paragraph’s top and the beginning of its text content.
- [var baseWritingDirection: NSWritingDirection](nsmutableparagraphstyle/basewritingdirection.md)
  The base writing direction for the paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/lineheightmultiple)*