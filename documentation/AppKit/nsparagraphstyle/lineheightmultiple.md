# lineHeightMultiple

**Framework**: AppKit  
**Kind**: property

The line height multiple.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var lineHeightMultiple: CGFloat { get }
```

#### Discussion

The framework multiplies the natural line height of the receiver by this factor (if positive), and constrains the resulting value by the minimum and maximum line height. The default value of this property is `0.0`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/lineheightmultiple)*