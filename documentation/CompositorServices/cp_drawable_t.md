# cp_drawable_t

**Framework**: Compositor Services  
**Kind**: typealias  
**Role**: Type Alias

A type that provides the textures and information you need to draw a frame of content.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
typedef struct cp_drawable * cp_drawable_t;
```

#### Discussion

When you draw a frame of content, the frame’s  [`cp_drawable_t`](./cp_drawable_t.md) type provides the actual textures and rendering information you need. Do as much work as possible in advance to prepare for rendering, and retrieve the [`cp_drawable_t`](./cp_drawable_t.md) only when you’re ready to start encoding commands into your Metal command buffers. The system recycles frames and their drawables for efficiency, so if you retrieve the drawable too early, it might not be ready to use.

Use the drawable’s [`LayerRenderer.Drawable.View`](./layerrenderer/drawable/view.md) instances to determine where to draw your content in the provided textures. After you finish encoding your content, call [`encodePresent(commandBuffer:)`](./layerrenderer/drawable/encodepresent%28commandbuffer%29.md) to add a presentation notification to your command buffer. This command tells Compositor Services when to display the frame, and is essential for displaying your frame on time.

## Topics

### Getting the views
- [cp_view_t](./cp_view_t.md)
  A type that provides information on how to render content into the frame’s textures.
### Enqueueing a command buffer
- [func encodePresent(commandBuffer: any MTLCommandBuffer)](./layerrenderer/drawable/encodepresent%28commandbuffer%29.md)
  Encodes a notification event to the specified command buffer to present the drawable’s content onscreen.
### Getting the projection matrix
- [enum AxisDirectionConvention](./axisdirectionconvention.md)
  Constants that indicate the axis and direction to use for a perspective projection matrix.
### Accessing pixel depth information
- [var depthRange: simd_float2](./layerrenderer/drawable/depthrange.md)
  The distances to the far and near clipping planes from the person viewing the content, in meters.
### Managing the state machine
- [var state: LayerRenderer.Drawable.State](./layerrenderer/drawable/state-swift.property.md)
  The current operational state of a drawable instance.
- [LayerRenderer.Drawable.State](./layerrenderer/drawable/state-swift.enum.md)
  The state of ownership for the drawable.
### Synchronizing the drawing operation
- [var frameTiming: LayerRenderer.Frame.Timing](./layerrenderer/drawable/frametiming.md)
  The timing information for the drawable’s frame.
- [var presentationFrameIndex: CompositorFrameIndex](./layerrenderer/drawable/presentationframeindex.md)
  The sequential index of a drawable’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_drawable_t)*