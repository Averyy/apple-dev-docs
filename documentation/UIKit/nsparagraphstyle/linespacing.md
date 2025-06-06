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
var lineSpacing: CGFloat { get }
```

#### Discussion

This value is always nonnegative. The layout manager uses this value in the line fragment height.

## See Also

- [var alignment: NSTextAlignment](nsparagraphstyle/alignment.md)
  The text alignment of the paragraph.
- [enum NSTextAlignment](nstextalignment.md)
  Constants that specify text alignment.
- [var firstLineHeadIndent: CGFloat](nsparagraphstyle/firstlineheadindent.md)
  The indentation of the first line of the paragraph.
- [var headIndent: CGFloat](nsparagraphstyle/headindent.md)
  The indentation of the paragraph’s lines other than the first.
- [var tailIndent: CGFloat](nsparagraphstyle/tailindent.md)
  The trailing indentation of the paragraph.
- [var lineHeightMultiple: CGFloat](nsparagraphstyle/lineheightmultiple.md)
  The line height multiple.
- [var maximumLineHeight: CGFloat](nsparagraphstyle/maximumlineheight.md)
  The paragraph’s maximum line height.
- [var minimumLineHeight: CGFloat](nsparagraphstyle/minimumlineheight.md)
  The paragraph’s minimum line height.
- [var paragraphSpacing: CGFloat](nsparagraphstyle/paragraphspacing.md)
  Distance between the bottom of this paragraph and top of next.
- [var paragraphSpacingBefore: CGFloat](nsparagraphstyle/paragraphspacingbefore.md)
  The distance between the paragraph’s top and the beginning of its text content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsparagraphstyle/linespacing)*