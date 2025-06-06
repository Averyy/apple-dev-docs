# maximumLineHeight

**Framework**: AppKit  
**Kind**: property

The paragraph’s maximum line height.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var maximumLineHeight: CGFloat { get }
```

#### Discussion

This property contains the maximum height in points that any line in the receiver occupies, regardless of the font size or size of any attached graphic. This value is always nonnegative. The default value is `0`.

Glyphs and graphics exceeding this height overlaps neighboring lines; however, a maximum height of `0` implies no line height limit. Although this limit applies to the line itself, line spacing adds extra space between adjacent lines.

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
- [var minimumLineHeight: CGFloat](nsparagraphstyle/minimumlineheight.md)
  The paragraph’s minimum line height.
- [var lineSpacing: CGFloat](nsparagraphstyle/linespacing.md)
  The distance in points between the bottom of one line fragment and the top of the next.
- [var paragraphSpacing: CGFloat](nsparagraphstyle/paragraphspacing.md)
  Distance between the bottom of this paragraph and top of next.
- [var paragraphSpacingBefore: CGFloat](nsparagraphstyle/paragraphspacingbefore.md)
  The distance between the paragraph’s top and the beginning of its text content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/maximumlineheight)*