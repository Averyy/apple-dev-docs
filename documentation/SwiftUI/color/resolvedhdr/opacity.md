# opacity

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The opacity of the color, in the range `0` to `1`.

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
var opacity: Float { get set }
```

#### Discussion

A value of `0` means 100% transparency, while a value of `1` means 100% opacity.

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
- [var headroom: Float?](./headroom.md)
  The content headroom of the color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/resolvedhdr/opacity)*