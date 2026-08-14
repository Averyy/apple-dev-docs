# LowLevelRenderer.Configuration

**Framework**: RealityKit  
**Kind**: struct

The configuration for a renderer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init(output: LowLevelRenderer.Configuration.Output, rasterSampleCount: Int, enableTonemap: Bool, enableColorMatch: Bool, alphaPremultiply: Bool, maxCameraCount: Int)](lowlevelrenderer/configuration/init(output:rastersamplecount:enabletonemap:enablecolormatch:alphapremultiply:maxcameracount:).md)
  Creates a configuration with the given output format, MSAA sample count, and flags.
### Specifying the output
- [var output: LowLevelRenderer.Configuration.Output](lowlevelrenderer/configuration/output-swift.property.md)
  The pixel format configuration for this renderer’s output attachments.
- [LowLevelRenderer.Configuration.Output](lowlevelrenderer/configuration/output-swift.struct.md)
  The pixel format configuration for a renderer’s output attachments.
- [var renderTargetDescriptor: LowLevelRenderTarget.Descriptor](lowlevelrenderer/configuration/rendertargetdescriptor.md)
  The render target descriptor derived from this configuration’s [`output`](lowlevelrenderer/configuration/output-swift.property.md).
### Configuring pixel formats
- [var colorAttachmentPixelFormats: [MTLPixelFormat]](lowlevelrenderer/configuration/colorattachmentpixelformats.md)
  The pixel formats of the color attachments in the render pass the renderer encodes into.
- [var depthAttachmentPixelFormat: MTLPixelFormat](lowlevelrenderer/configuration/depthattachmentpixelformat.md)
  The pixel format of the depth attachment in the render pass the renderer encodes into.
- [var stencilAttachmentPixelFormat: MTLPixelFormat](lowlevelrenderer/configuration/stencilattachmentpixelformat.md)
  The pixel format of the stencil attachment in the render pass the renderer encodes into.
### Tuning rendering options
- [var rasterSampleCount: Int](lowlevelrenderer/configuration/rastersamplecount.md)
  The number of samples per pixel for MSAA.
- [var enableTonemap: Bool](lowlevelrenderer/configuration/enabletonemap.md)
  A Boolean value that indicates whether output values are tone-mapped to the target pixel format’s range before being written to the output texture.
- [var enableColorMatch: Bool](lowlevelrenderer/configuration/enablecolormatch.md)
  A Boolean value that indicates whether the renderer applies a gamut conversion matrix during resolve, converting from the renderer’s working color space to the output display’s color space.
- [var alphaPremultiply: Bool](lowlevelrenderer/configuration/alphapremultiply.md)
  A Boolean value that indicates whether the renderer divides content by alpha before applying tonemap and color match, then multiplies by alpha before final texture output.
- [var maxCameraCount: Int](lowlevelrenderer/configuration/maxcameracount.md)
  The maximum number of simultaneous cameras supported.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [convenience init(configuration: LowLevelRenderer.Configuration, renderContext: any LowLevelRenderContext) async throws](lowlevelrenderer/init(configuration:rendercontext:).md)
  Creates a renderer, asynchronously compiling all required GPU resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/configuration)*