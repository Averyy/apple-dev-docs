# ascender

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The top y-coordinate, offset from the baseline, of the font’s longest ascender.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var ascender: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat ascender;
```

#### Discussion

The ascender value is measured in points. For an explanation of how this metric relates to a font’s other metrics, see [`UIFont`](../uifont.md).

## See Also

### Getting Font Metrics
- [var pointSize: CGFloat](./pointsize.md)
  The font’s point size, or the effective vertical point size for a font with a nonstandard matrix.
- [var descender: CGFloat](./descender.md)
  The bottom y-coordinate, offset from the baseline, of the font’s longest descender.
- [var leading: CGFloat](./leading.md)
  The font’s leading information.
- [var capHeight: CGFloat](./capheight.md)
  The font’s cap height information.
- [var xHeight: CGFloat](./xheight.md)
  The x-height of the font.
- [var lineHeight: CGFloat](./lineheight.md)
  The height, in points, of text lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/ascender)*