# LayerRenderer.Drawable

**Framework**: Compositor Services  
**Kind**: struct

A type that provides the textures and information you need to draw a frame of content.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Drawable
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Overview

When you draw a frame of content, the frame’s  [`LayerRenderer.Drawable`](layerrenderer/drawable.md) type provides the actual textures and rendering information you need. Do as much work as possible in advance to prepare for rendering, and retrieve the [`LayerRenderer.Drawable`](layerrenderer/drawable.md) only when you’re ready to start encoding commands into your Metal command buffers. The system recycles frames and their drawables for efficiency, so if you retrieve the drawable too early, it might not be ready to use.

Use the drawable’s [`LayerRenderer.Drawable.View`](layerrenderer/drawable/view.md) instances to determine where to draw your content in the provided textures. After you finish encoding your content, call [`encodePresent(commandBuffer:)`](layerrenderer/drawable/encodepresent(commandbuffer:).md) to add a presentation notification to your command buffer. This command tells Compositor Services when to display the frame, and is essential for displaying your frame on time.

## Topics

### Getting the views
- [var views: [LayerRenderer.Drawable.View]](layerrenderer/drawable/views.md)
  An array of viewports that tell you how to draw to the drawable’s textures
- [LayerRenderer.Drawable.View](layerrenderer/drawable/view.md)
  A type that provides information on how to render content into the frame’s textures.
### Accessing the device orientation
- [var deviceAnchor: DeviceAnchor?](layerrenderer/drawable/deviceanchor.md)
  The device position and orientation you used to render the frame.
### Getting the render textures
- [var colorTextures: [any MTLTexture]](layerrenderer/drawable/colortextures.md)
  An array of color textures to use to render the current frame.
- [var depthTextures: [any MTLTexture]](layerrenderer/drawable/depthtextures.md)
  An array of depth textures to use to render the current frame.
### Enqueueing a command buffer
- [func encodePresent(commandBuffer: any MTLCommandBuffer)](layerrenderer/drawable/encodepresent(commandbuffer:).md)
  Encodes a notification event to the specified command buffer to present the drawable’s content onscreen.
### Getting the rasterization rate map
- [var rasterizationRateMaps: [any MTLRasterizationRateMap]](layerrenderer/drawable/rasterizationratemaps.md)
  The rasterization rate maps to use when rendering the frame.
- [var flippedRasterizationRateMaps: [any MTLRasterizationRateMap]](layerrenderer/drawable/flippedrasterizationratemaps.md)
  The rasterization rate maps that are flipped around the y-axis.
### Getting the projection matrix
- [enum AxisDirectionConvention](axisdirectionconvention.md)
  Constants that indicate the axis and direction to use for a perspective projection matrix.
### Accessing pixel depth information
- [var depthRange: simd_float2](layerrenderer/drawable/depthrange.md)
  The distances to the far and near clipping planes from the person viewing the content, in meters.
### Managing the state machine
- [var state: LayerRenderer.Drawable.State](layerrenderer/drawable/state-swift.property.md)
  The current operational state of a drawable instance.
- [LayerRenderer.Drawable.State](layerrenderer/drawable/state-swift.enum.md)
  The state of ownership for the drawable.
### Synchronizing the drawing operation
- [var frameTiming: LayerRenderer.Frame.Timing](layerrenderer/drawable/frametiming.md)
  The timing information for the drawable’s frame.
- [var presentationFrameIndex: CompositorFrameIndex](layerrenderer/drawable/presentationframeindex.md)
  The sequential index of a drawable’s frame.
### Creating a drawable
- [init()](layerrenderer/drawable/init.md)
  Creates an uninitialized drawable.
### Instance Methods
- [func computeProjection(convention: AxisDirectionConvention, viewIndex: Int) -> matrix_float4x4](layerrenderer/drawable/computeprojection(convention:viewindex:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [LayerRenderer.Drawable.View](layerrenderer/drawable/view.md)
  A type that provides information on how to render content into the frame’s textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable)*