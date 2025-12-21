# Color.ResolvedHDR

**Framework**: SwiftUI  
**Kind**: struct

A concrete color value, including HDR headroom information.

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
@frozen
struct ResolvedHDR
```

#### Overview

`Color.ResolvedHDR` is a set of RGBA values that represent a color that can be shown. The color components are stored in the extended sRGB color space and may contain a “headroom” value describing how the color is rendered for displays with different dynamic ranges. This is a low-level type, most colors are represented by the `Color` type.

> **Note**: `Color.Resolved`, `Color`.

## Topics

### Creating a concrete color value
- [init(Color.Resolved, headroom: Float?)](color/resolvedhdr/init(_:headroom:).md)
  Initializes a new resolved color value.
### Getting color properties
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
- [var headroom: Float?](color/resolvedhdr/headroom.md)
  The content headroom of the color.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [ShapeStyle](shapestyle.md)

## See Also

- [func resolveHDR(in: EnvironmentValues) -> Color.ResolvedHDR](color/resolvehdr(in:).md)
  Evaluates this color to a resolved color with content headroom, given a set of environment values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/resolvedhdr)*