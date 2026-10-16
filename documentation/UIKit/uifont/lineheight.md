# lineHeight

**Framework**: UIKit  
**Kind**: property

The height, in points, of text lines.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var lineHeight: CGFloat { get }
```

#### Discussion

This value is approximately equal to [`ascender`](uifont/ascender.md) plus the absolute value of [`descender`](uifont/descender.md) plus [`leading`](uifont/leading.md). For an explanation of how these metrics relate to each other, see [`UIFont`](uifont.md).

## See Also

- [var pointSize: CGFloat](uifont/pointsize.md)
  The font’s point size, or the effective vertical point size for a font with a nonstandard matrix.
- [var ascender: CGFloat](uifont/ascender.md)
  The top y-coordinate, offset from the baseline, of the font’s longest ascender.
- [var descender: CGFloat](uifont/descender.md)
  The bottom y-coordinate, offset from the baseline, of the font’s longest descender.
- [var leading: CGFloat](uifont/leading.md)
  The font’s leading information.
- [var capHeight: CGFloat](uifont/capheight.md)
  The font’s cap height information.
- [var xHeight: CGFloat](uifont/xheight.md)
  The x-height of the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/lineheight)*