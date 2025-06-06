# multiply

**Framework**: SwiftUI  
**Kind**: property

A mode that multiplies the source image samples with the background image samples.

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
static var multiply: GraphicsContext.BlendMode { get }
```

#### Discussion

Drawing in this mode results in colors that are at least as dark as either of the two contributing sample colors.

## See Also

- [static var darken: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/darken.md)
  A mode that creates composite image samples by choosing the darker samples from either the source image or the background.
- [static var colorBurn: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/colorburn.md)
  A mode that darkens background image samples to reflect the source image samples.
- [static var plusDarker: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/plusdarker.md)
  A mode that adds the inverse of the color components of the source and background images, and then inverts the result, producing a darkened composite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/multiply)*