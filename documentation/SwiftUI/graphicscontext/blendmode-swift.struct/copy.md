# copy

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A mode that replaces background image samples with source image samples.

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
static var copy: GraphicsContext.BlendMode { get }
```

#### Discussion

Unlike the [`normal`](./normal.md) mode, the source image completely replaces the background, so that even transparent pixels in the source image replace opaque pixels in the background, rather than letting the background show through.

This mode implements the equation `R = S` where

- `R` is the composite image.
- `S` is the source image.

## See Also

### Accessing Porter-Duff modes
- [static var clear: GraphicsContext.BlendMode](./clear.md)
  A mode that clears any pixels that the source image overwrites.
- [static var sourceIn: GraphicsContext.BlendMode](./sourcein.md)
  A mode that you use to paint the source image, including its transparency, onto the opaque parts of the background.
- [static var sourceOut: GraphicsContext.BlendMode](./sourceout.md)
  A mode that you use to paint the source image onto the transparent parts of the background, while erasing the background.
- [static var sourceAtop: GraphicsContext.BlendMode](./sourceatop.md)
  A mode that you use to paint the opaque parts of the source image onto the opaque parts of the background.
- [static var destinationOver: GraphicsContext.BlendMode](./destinationover.md)
  A mode that you use to paint the source image under the background.
- [static var destinationIn: GraphicsContext.BlendMode](./destinationin.md)
  A mode that you use to erase any of the background that isn’t covered by opaque source pixels.
- [static var destinationOut: GraphicsContext.BlendMode](./destinationout.md)
  A mode that you use to erase any of the background that is covered by opaque source pixels.
- [static var destinationAtop: GraphicsContext.BlendMode](./destinationatop.md)
  A mode that you use to paint the source image under the background, while erasing any of the background not matched by opaque pixels from the source image.
- [static var xor: GraphicsContext.BlendMode](./xor.md)
  A mode that you use to clear pixels where both the source and background images are opaque.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/copy)*