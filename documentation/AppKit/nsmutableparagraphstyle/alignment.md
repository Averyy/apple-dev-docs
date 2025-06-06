# alignment

**Framework**: AppKit  
**Kind**: property

The text alignment of the paragraph.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var alignment: NSTextAlignment { get set }
```

#### Discussion

Natural text alignment is realized as left or right alignment depending on the line sweep direction of the first script contained in the paragraph.

## See Also

- [func setParagraphStyle(NSParagraphStyle)](nsmutableparagraphstyle/setparagraphstyle(_:).md)
  Replaces the subattributes of the paragraph with those in the specified paragraph style object.
- [var firstLineHeadIndent: CGFloat](nsmutableparagraphstyle/firstlineheadindent.md)
  The indentation of the first line of the paragraph.
- [var headIndent: CGFloat](nsmutableparagraphstyle/headindent.md)
  The indentation of the paragraph’s lines other than the first.
- [var tailIndent: CGFloat](nsmutableparagraphstyle/tailindent.md)
  The trailing indentation of the paragraph.
- [var lineHeightMultiple: CGFloat](nsmutableparagraphstyle/lineheightmultiple.md)
  The line height multiple.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/alignment)*