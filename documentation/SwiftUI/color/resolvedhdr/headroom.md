# headroom

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

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
@export(implementation)
var headroom: Float? { get set }
```

## Discussion

This is the ratio of nominal peak luminance (“peak white”) to nominal diffuse luminance (“reference white” or “diffuse white”). Headroom is a linear quantity, i.e. there is no gamma function applied to it.

## See Also

### Getting color properties
- [var red: Float](./red.md)
  The amount of red in the color in the extended sRGB color space.
- [var green: Float](./green.md)
  The amount of green in the color in the extended sRGB color space.
- [var blue: Float](./blue.md)
  The amount of blue in the color in the extended sRGB color space.
- [var linearRed: Float](./linearred.md)
  The amount of red in the color in the extended sRGB color space variant with linear gamma.
- [var linearGreen: Float](./lineargreen.md)
  The amount of green in the color in the extended sRGB color space variant with linear gamma.
- [var linearBlue: Float](./linearblue.md)
  The amount of blue in the color in the extended sRGB color space variant with linear gamma.
- [var opacity: Float](./opacity.md)
  The opacity of the color, in the range `0` to `1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/resolvedhdr/headroom)*