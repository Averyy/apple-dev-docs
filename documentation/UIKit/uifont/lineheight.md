# lineHeight

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The height, in points, of text lines.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var lineHeight: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat lineHeight;
```

## Discussion

This value is approximately equal to [`ascender`](./ascender.md) plus the absolute value of [`descender`](./descender.md) plus [`leading`](./leading.md). For an explanation of how these metrics relate to each other, see [`UIFont`](../uifont.md).

## See Also

### Getting Font Metrics
- [var pointSize: CGFloat](./pointsize.md)
  The font’s point size, or the effective vertical point size for a font with a nonstandard matrix.
- [var ascender: CGFloat](./ascender.md)
  The top y-coordinate, offset from the baseline, of the font’s longest ascender.
- [var descender: CGFloat](./descender.md)
  The bottom y-coordinate, offset from the baseline, of the font’s longest descender.
- [var leading: CGFloat](./leading.md)
  The font’s leading information.
- [var capHeight: CGFloat](./capheight.md)
  The font’s cap height information.
- [var xHeight: CGFloat](./xheight.md)
  The x-height of the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/lineheight)*