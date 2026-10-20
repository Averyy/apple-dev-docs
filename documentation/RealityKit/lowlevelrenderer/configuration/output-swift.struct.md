# LowLevelRenderer.Configuration.Output

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The pixel format configuration for a renderer’s output attachments.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Output
```

## Topics

### Creating an output configuration
- [init(colorPixelFormat: MTLPixelFormat?, depthPixelFormat: MTLPixelFormat?)](./output-swift.struct/init%28colorpixelformat,depthpixelformat%29.md)
  Creates an output configuration with the given color and depth pixel formats.
### Specifying pixel formats
- [var colorPixelFormat: MTLPixelFormat?](./output-swift.struct/colorpixelformat.md)
  The pixel format of the color attachment, or `nil` for depth-only passes.
- [var depthPixelFormat: MTLPixelFormat?](./output-swift.struct/depthpixelformat.md)
  The pixel format of the depth attachment, or `nil` to omit depth.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Specifying the output
- [var output: LowLevelRenderer.Configuration.Output](./output-swift.property.md)
  The pixel format configuration for this renderer’s output attachments.
- [var renderTargetDescriptor: LowLevelRenderTarget.Descriptor](./rendertargetdescriptor.md)
  The render target descriptor derived from this configuration’s [`output`](./output-swift.property.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/configuration/output-swift.struct)*