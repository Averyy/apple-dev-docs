# alignment

**Framework**: AppKit  
**Kind**: property

The text alignment of the paragraph.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var alignment: NSTextAlignment { get }
```

#### Discussion

The framework displays natural text alignment as left or right alignment depending on the line sweep direction of the first script contained in the paragraph.

## See Also

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
- [var lineSpacing: CGFloat](nsparagraphstyle/linespacing.md)
  The distance in points between the bottom of one line fragment and the top of the next.
- [var paragraphSpacing: CGFloat](nsparagraphstyle/paragraphspacing.md)
  Distance between the bottom of this paragraph and top of next.
- [var paragraphSpacingBefore: CGFloat](nsparagraphstyle/paragraphspacingbefore.md)
  The distance between the paragraph’s top and the beginning of its text content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/alignment)*