# color(_:white:opacity:)

**Framework**: SwiftUI  
**Kind**: method

Returns a shading instance that fills with a monochrome color in the given color space.

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
static func color(_ colorSpace: Color.RGBColorSpace = .sRGB, white: Double, opacity: Double = 1) -> GraphicsContext.Shading
```

#### Return Value

A shading instance filled with a color.

## Parameters

- `colorSpace`: The RGB color space used to define the color. The   default is  .
- `white`: The value to use for each of the red, green, and blue   components of the color.
- `opacity`: The opacity of the color. The default is  , which   means fully opaque.

## See Also

- [static func color(Color) -> GraphicsContext.Shading](graphicscontext/shading/color(_:).md)
  Returns a shading instance that fills with a color.
- [static func color(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity: Double) -> GraphicsContext.Shading](graphicscontext/shading/color(_:red:green:blue:opacity:).md)
  Returns a shading instance that fills with a color in the given color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shading/color(_:white:opacity:))*