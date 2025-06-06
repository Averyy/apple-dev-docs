# lineSpacing

**Framework**: UIKit  
**Kind**: property

The distance in points between the bottom of one line fragment and the top of the next.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var lineSpacing: CGFloat { get set }
```

#### Discussion

This value is always nonnegative. This value is included in the line fragment heights in the layout manager.

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
- [var lineHeightMultiple: CGFloat](nsmutableparagraphstyle/lineheightmultiple.md)
  The line height multiple.
- [var maximumLineHeight: CGFloat](nsmutableparagraphstyle/maximumlineheight.md)
  The paragraph’s maximum line height.
- [var minimumLineHeight: CGFloat](nsmutableparagraphstyle/minimumlineheight.md)
  The paragraph’s minimum line height.
- [var paragraphSpacing: CGFloat](nsmutableparagraphstyle/paragraphspacing.md)
  The space after the end of the paragraph.
- [var paragraphSpacingBefore: CGFloat](nsmutableparagraphstyle/paragraphspacingbefore.md)
  The distance between the paragraph’s top and the beginning of its text content.
- [var baseWritingDirection: NSWritingDirection](nsmutableparagraphstyle/basewritingdirection.md)
  The base writing direction for the paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/linespacing)*