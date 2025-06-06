# tailIndent

**Framework**: AppKit  
**Kind**: property

The trailing indentation of the paragraph.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var tailIndent: CGFloat { get }
```

#### Discussion

If positive, this value is the distance from the leading margin (for example, the left margin in left-to-right text). If `0` or negative, it’s the distance from the trailing margin.

For example, a paragraph style designed to fit exactly in a two-inch wide container has a head indent of `0.0` and a tail indent of `0.0`. One designed to fit with a quarter-inch margin has a head indent of `0.25` and a tail indent of `–0.25`.

## See Also

- [var alignment: NSTextAlignment](nsparagraphstyle/alignment.md)
  The text alignment of the paragraph.
- [enum NSTextAlignment](nstextalignment.md)
  Constants that specify text alignment.
- [var firstLineHeadIndent: CGFloat](nsparagraphstyle/firstlineheadindent.md)
  The indentation of the first line of the paragraph.
- [var headIndent: CGFloat](nsparagraphstyle/headindent.md)
  The indentation of the paragraph’s lines other than the first.
- [var lineHeightMultiple: CGFloat](nsparagraphstyle/lineheightmultiple.md)
  The line height multiple.
- [var maximumLineHeight: CGFloat](nsparagraphstyle/maximumlineheight.md)
  The paragraph’s maximum line height.
- [var minimumLineHeight: CGFloat](nsparagraphstyle/minimumlineheight.md)
  The paragraph’s minimum line height.
- [var lineSpacing: CGFloat](nsparagraphstyle/linespacing.md)
  The distance in points between the bottom of one line fragment and the top of the next.
- [var paragraphSpacing: CGFloat](nsparagraphstyle/paragraphspacing.md)
  Distance between the bottom of this paragraph and top of next.
- [var paragraphSpacingBefore: CGFloat](nsparagraphstyle/paragraphspacingbefore.md)
  The distance between the paragraph’s top and the beginning of its text content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/tailindent)*