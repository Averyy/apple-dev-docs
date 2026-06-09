# LowLevelRenderer.Configuration.Output

**Framework**: RealityKit  
**Kind**: struct

The pixel format configuration for a renderer’s output attachments.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Output
```

## Topics

### Creating an output configuration
- [init(colorPixelFormat: MTLPixelFormat?, depthPixelFormat: MTLPixelFormat?)](lowlevelrenderer/configuration/output-swift.struct/init(colorpixelformat:depthpixelformat:).md)
  Creates an output configuration with the given color and depth pixel formats.
### Specifying pixel formats
- [var colorPixelFormat: MTLPixelFormat?](lowlevelrenderer/configuration/output-swift.struct/colorpixelformat.md)
  The pixel format of the color attachment, or `nil` for depth-only passes.
- [var depthPixelFormat: MTLPixelFormat?](lowlevelrenderer/configuration/output-swift.struct/depthpixelformat.md)
  The pixel format of the depth attachment, or `nil` to omit depth.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var output: LowLevelRenderer.Configuration.Output](lowlevelrenderer/configuration/output-swift.property.md)
  The pixel format configuration for this renderer’s output attachments.
- [var renderTargetDescriptor: LowLevelRenderTarget.Descriptor](lowlevelrenderer/configuration/rendertargetdescriptor.md)
  The render target descriptor derived from this configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/configuration/output-swift.struct)*