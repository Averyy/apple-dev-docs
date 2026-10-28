# firstLineHeadIndent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The indentation of the first line of the paragraph.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var firstLineHeadIndent: CGFloat { get }
```

```objc
@property (readonly) CGFloat firstLineHeadIndent;
```

## Discussion

This property contains the distance (in points) from the leading margin of a text container to the beginning of the paragraph’s first line. This value is always nonnegative.

## See Also

### Accessing style information
- [var alignment: NSTextAlignment](./alignment.md)
  The text alignment of the paragraph.
- [enum NSTextAlignment](../nstextalignment.md)
  Constants that specify text alignment.
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
- [var paragraphSpacingBefore: CGFloat](./paragraphspacingbefore.md)
  The distance between the paragraph’s top and the beginning of its text content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/firstlineheadindent)*