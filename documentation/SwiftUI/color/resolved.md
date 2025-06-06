# Color.Resolved

**Framework**: SwiftUI  
**Kind**: struct

A concrete color value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@frozen
struct Resolved
```

#### Overview

`Color.Resolved` is a set of RGBA values that represent a color that can be shown. The values are in Linear sRGB color space, extended range. This is a low-level type, most colors are represented by the `Color` type.

> **Note**: `Color`

`Color`

## Topics

### Initializers
- [init(colorSpace: Color.RGBColorSpace, red: Float, green: Float, blue: Float, opacity: Float)](color/resolved/init(colorspace:red:green:blue:opacity:).md)
  Creates a resolved color from red, green, and blue component values.
### Instance Properties
- [var blue: Float](color/resolved/blue.md)
  The amount of blue in the color in the sRGB color space.
- [var cgColor: CGColor](color/resolved/cgcolor.md)
  A Core Graphics representation of the color.
- [var green: Float](color/resolved/green.md)
  The amount of green in the color in the sRGB color space.
- [var linearBlue: Float](color/resolved/linearblue.md)
  The amount of blue in the color in the sRGB linear color space.
- [var linearGreen: Float](color/resolved/lineargreen.md)
  The amount of green in the color in the sRGB linear color space.
- [var linearRed: Float](color/resolved/linearred.md)
  The amount of red in the color in the sRGB linear color space.
- [var opacity: Float](color/resolved/opacity.md)
  The degree of opacity in the color, given in the range `0` to `1`.
- [var red: Float](color/resolved/red.md)
  The amount of red in the color in the sRGB color space.

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
- [ShapeStyle](shapestyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/resolved)*