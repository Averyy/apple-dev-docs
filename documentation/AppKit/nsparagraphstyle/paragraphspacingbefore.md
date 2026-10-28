# paragraphSpacingBefore

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The distance between the paragraph’s top and the beginning of its text content.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var paragraphSpacingBefore: CGFloat { get }
```

```objc
@property (readonly) CGFloat paragraphSpacingBefore;
```

## Discussion

This property contains the space (measured in points) between the current and previous paragraphs. The default value of this property is `0.0`.

## See Also

### Accessing style information
- [var alignment: NSTextAlignment](./alignment.md)
  The text alignment of the paragraph.
- [enum NSTextAlignment](../nstextalignment.md)
  Constants that specify text alignment.
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
  Distance between the bottom of this paragraph and top of next.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/paragraphspacingbefore)*