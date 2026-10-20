# color(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Returns a shading instance that fills with a color.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func color(_ color: Color) -> GraphicsContext.Shading
```

#### Return Value

A shading instance filled with a color.

## Parameters

- `color`: A [`Color`](../../color.md) instance that defines the color of the shading.

## See Also

### Colors
- [static func color(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity: Double) -> GraphicsContext.Shading](./color%28_,red,green,blue,opacity%29.md)
  Returns a shading instance that fills with a color in the given color space.
- [static func color(Color.RGBColorSpace, white: Double, opacity: Double) -> GraphicsContext.Shading](./color%28_,white,opacity%29.md)
  Returns a shading instance that fills with a monochrome color in the given color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shading/color(_:))*