# darken

**Framework**: SwiftUI  
**Kind**: property

A mode that creates composite image samples by choosing the darker samples from either the source image or the background.

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
static var darken: GraphicsContext.BlendMode { get }
```

#### Discussion

When you draw in this mode, source image samples that are darker than the background replace the background. Otherwise, the background image samples remain unchanged.

## See Also

- [static var multiply: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/multiply.md)
  A mode that multiplies the source image samples with the background image samples.
- [static var colorBurn: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/colorburn.md)
  A mode that darkens background image samples to reflect the source image samples.
- [static var plusDarker: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/plusdarker.md)
  A mode that adds the inverse of the color components of the source and background images, and then inverts the result, producing a darkened composite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/darken)*