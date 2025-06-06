# destinationAtop

**Framework**: SwiftUI  
**Kind**: property

A mode that you use to paint the source image under the background, while erasing any of the background not matched by opaque pixels from the source image.

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
static var destinationAtop: GraphicsContext.BlendMode { get }
```

#### Discussion

This mode implements the equation `R = S*(1 - Da) + D*Sa` where

- `R` is the composite image.
- `S` is the source image.
- `D` is the background.
- `Sa` is the source image’s alpha value.
- `Da` is the source background’s alpha value.

## See Also

- [static var clear: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/clear.md)
  A mode that clears any pixels that the source image overwrites.
- [static var copy: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/copy.md)
  A mode that replaces background image samples with source image samples.
- [static var sourceIn: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/sourcein.md)
  A mode that you use to paint the source image, including its transparency, onto the opaque parts of the background.
- [static var sourceOut: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/sourceout.md)
  A mode that you use to paint the source image onto the transparent parts of the background, while erasing the background.
- [static var sourceAtop: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/sourceatop.md)
  A mode that you use to paint the opaque parts of the source image onto the opaque parts of the background.
- [static var destinationOver: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/destinationover.md)
  A mode that you use to paint the source image under the background.
- [static var destinationIn: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/destinationin.md)
  A mode that you use to erase any of the background that isn’t covered by opaque source pixels.
- [static var destinationOut: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/destinationout.md)
  A mode that you use to erase any of the background that is covered by opaque source pixels.
- [static var xor: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/xor.md)
  A mode that you use to clear pixels where both the source and background images are opaque.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/destinationatop)*