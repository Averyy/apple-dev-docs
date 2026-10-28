# Color.Resolved

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

## Overview

`Color.Resolved` is a set of RGBA values that represent a color that can be shown. The values are stored in the Linear sRGB color space, using extended range. This is a low-level type, most colors are represented by the `Color` type.

> **See Also**: `Color.ResolvedHDR`, `Color`.

## Topics

### Initializers
- [init(colorSpace: Color.RGBColorSpace, red: Float, green: Float, blue: Float, opacity: Float)](./resolved/init%28colorspace,red,green,blue,opacity%29.md)
  Creates a resolved color from red, green, and blue component values.
### Instance Properties
- [var blue: Float](./resolved/blue.md)
  The amount of blue in the color in the sRGB color space.
- [var cgColor: CGColor](./resolved/cgcolor.md)
  A Core Graphics representation of the color.
- [var green: Float](./resolved/green.md)
  The amount of green in the color in the sRGB color space.
- [var linearBlue: Float](./resolved/linearblue.md)
  The amount of blue in the color in the sRGB linear color space.
- [var linearGreen: Float](./resolved/lineargreen.md)
  The amount of green in the color in the sRGB linear color space.
- [var linearRed: Float](./resolved/linearred.md)
  The amount of red in the color in the sRGB linear color space.
- [var opacity: Float](./resolved/opacity.md)
  The degree of opacity in the color, given in the range `0` to `1`.
- [var red: Float](./resolved/red.md)
  The amount of red in the color in the sRGB color space.

## Relationships

### Conforms To
- [Animatable](../animatable.md)
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [ShapeStyle](../shapestyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/resolved)*