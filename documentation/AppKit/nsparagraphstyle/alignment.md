# alignment

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text alignment of the paragraph.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var alignment: NSTextAlignment { get }
```

```objc
@property (readonly) NSTextAlignment alignment;
```

## Discussion

The framework displays natural text alignment as left or right alignment depending on the line sweep direction of the first script contained in the paragraph.

## See Also

### Accessing style information
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
- [var paragraphSpacingBefore: CGFloat](./paragraphspacingbefore.md)
  The distance between the paragraph’s top and the beginning of its text content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/alignment)*