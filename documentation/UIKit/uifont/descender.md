# descender

**Framework**: UIKit  
**Kind**: property

The bottom y-coordinate, offset from the baseline, of the font’s longest descender.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var descender: CGFloat { get }
```

#### Discussion

The descender value is measured in points. This value may be positive or negative. For example, if the longest descender extends 2 points below the baseline, this method returns `-2.0` .

## See Also

- [var pointSize: CGFloat](uifont/pointsize.md)
  The font’s point size, or the effective vertical point size for a font with a nonstandard matrix.
- [var ascender: CGFloat](uifont/ascender.md)
  The top y-coordinate, offset from the baseline, of the font’s longest ascender.
- [var leading: CGFloat](uifont/leading.md)
  The font’s leading information.
- [var capHeight: CGFloat](uifont/capheight.md)
  The font’s cap height information.
- [var xHeight: CGFloat](uifont/xheight.md)
  The x-height of the font.
- [var lineHeight: CGFloat](uifont/lineheight.md)
  The height, in points, of text lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/descender)*