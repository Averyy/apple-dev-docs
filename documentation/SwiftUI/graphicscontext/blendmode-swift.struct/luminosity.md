# luminosity

**Framework**: SwiftUI  
**Kind**: property

A mode that uses the hue and saturation of the background with the luminance of the source image.

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
static var luminosity: GraphicsContext.BlendMode { get }
```

#### Discussion

This mode creates an effect that is inverse to the effect created by the [`color`](graphicscontext/blendmode-swift.struct/color.md) mode.

## See Also

- [static var hue: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/hue.md)
  A mode that uses the luminance and saturation values of the background with the hue of the source image.
- [static var saturation: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/saturation.md)
  A mode that uses the luminance and hue values of the background with the saturation of the source image.
- [static var color: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/color.md)
  A mode that uses the luminance values of the background with the hue and saturation values of the source image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/luminosity)*