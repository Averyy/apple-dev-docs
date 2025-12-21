# headroom

**Framework**: SwiftUI  
**Kind**: property

The content headroom of the color.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var headroom: Float? { get set }
```

#### Discussion

This is the ratio of nominal peak luminance (“peak white”) to nominal diffuse luminance (“reference white” or “diffuse white”). Headroom is a linear quantity, i.e. there is no gamma function applied to it.

## See Also

- [var red: Float](color/resolvedhdr/red.md)
  The amount of red in the color in the extended sRGB color space.
- [var green: Float](color/resolvedhdr/green.md)
  The amount of green in the color in the extended sRGB color space.
- [var blue: Float](color/resolvedhdr/blue.md)
  The amount of blue in the color in the extended sRGB color space.
- [var linearRed: Float](color/resolvedhdr/linearred.md)
  The amount of red in the color in the extended sRGB color space variant with linear gamma.
- [var linearGreen: Float](color/resolvedhdr/lineargreen.md)
  The amount of green in the color in the extended sRGB color space variant with linear gamma.
- [var linearBlue: Float](color/resolvedhdr/linearblue.md)
  The amount of blue in the color in the extended sRGB color space variant with linear gamma.
- [var opacity: Float](color/resolvedhdr/opacity.md)
  The opacity of the color, in the range `0` to `1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/resolvedhdr/headroom)*