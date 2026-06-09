# LowLevelRenderer.Output

**Framework**: RealityKit  
**Kind**: struct

The per-frame output target configuration for a renderer.

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

### Creating an output
- [init(color: LowLevelRenderer.Output.Texture?, depth: LowLevelRenderer.Output.Texture?)](lowlevelrenderer/output-swift.struct/init(color:depth:).md)
  Creates an output configuration with the given color and depth texture targets.
- [LowLevelRenderer.Output.Texture](lowlevelrenderer/output-swift.struct/texture.md)
  A reference to a specific mip level, slice, and depth plane within a Metal texture.
### Configuring render targets
- [var renderTargetWidth: Int](lowlevelrenderer/output-swift.struct/rendertargetwidth.md)
  The width of the render target, in pixels.
- [var renderTargetHeight: Int](lowlevelrenderer/output-swift.struct/rendertargetheight.md)
  The height of the render target, in pixels.
- [var renderTargetArrayLength: Int](lowlevelrenderer/output-swift.struct/rendertargetarraylength.md)
  The number of active array slices in the render target textures.
- [var threadgroupMemoryLength: Int](lowlevelrenderer/output-swift.struct/threadgroupmemorylength.md)
  The per-tile size, in bytes, of the persistent threadgroup memory allocation, used when rendering.
### Setting the viewport
- [var viewports: [MTLViewport]?](lowlevelrenderer/output-swift.struct/viewports.md)
  Per-camera viewport rectangles within the render target.
- [var scissorRects: [MTLScissorRect]?](lowlevelrenderer/output-swift.struct/scissorrects.md)
  Per-camera scissor rectangles within the render target.
- [var rasterizationRateMap: (any MTLRasterizationRateMap)?](lowlevelrenderer/output-swift.struct/rasterizationratemap.md)
  The rasterization rate map to use when rendering.
### Clearing and resolving
- [var clearColor: MTLClearColor](lowlevelrenderer/output-swift.struct/clearcolor.md)
  The color to use when clearing the color attachment at the start of a render pass.
- [var clearDepth: Double](lowlevelrenderer/output-swift.struct/cleardepth.md)
  The depth value to use when clearing the depth attachment at the start of a render pass.
- [var depthResolveFilter: MTLMultisampleDepthResolveFilter](lowlevelrenderer/output-swift.struct/depthresolvefilter.md)
  The filter to use when resolving the depth attachment at the end of a multisampled render pass.
### Instance Properties
- [var color: LowLevelRenderer.Output.Texture?](lowlevelrenderer/output-swift.struct/color.md)
  The color output texture. Corresponds to `MTLRenderPassColorAttachmentDescriptor.texture`.
- [var depth: LowLevelRenderer.Output.Texture?](lowlevelrenderer/output-swift.struct/depth.md)
  The depth output texture. Corresponds to `MTLRenderPassDepthAttachmentDescriptor.texture`.

## See Also

- [var output: LowLevelRenderer.Output](lowlevelrenderer/output-swift.property.md)
  The per-frame output target configuration, including color and depth textures, viewports, and render target dimensions.
- [var renderTargetDescriptor: LowLevelRenderTarget.Descriptor](lowlevelrenderer/rendertargetdescriptor.md)
  The render target descriptor derived from the renderer’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct)*