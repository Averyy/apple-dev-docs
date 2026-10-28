# headIndent

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The indentation of the paragraph’s lines other than the first.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var headIndent: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat headIndent;
```

## Discussion

This property contains the distance (in points) from the leading margin of a text container to the beginning of lines other than the first. This value is always nonnegative.

## See Also

### Setting style information
- [func setParagraphStyle(NSParagraphStyle)](./setparagraphstyle%28_%29.md)
  Replaces the subattributes of the paragraph with those in the specified paragraph style object.
- [var alignment: NSTextAlignment](./alignment.md)
  The text alignment of the paragraph.
- [var firstLineHeadIndent: CGFloat](./firstlineheadindent.md)
  The indentation of the first line of the paragraph.
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
  The space after the end of the paragraph.
- [var paragraphSpacingBefore: CGFloat](./paragraphspacingbefore.md)
  The distance between the paragraph’s top and the beginning of its text content.
- [var baseWritingDirection: NSWritingDirection](./basewritingdirection.md)
  The base writing direction for the paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/headindent)*