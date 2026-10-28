# Drawable

**Framework**: Compositor Services  
**Role**: API Collection

A type that provides information on how to render content into the frame’s textures.

## Overview

When you draw a frame of content, the frame’s  [`cp_drawable_t`](./cp_drawable_t.md) type provides the actual textures and rendering information you need. Do as much work as possible in advance to prepare for rendering, and retrieve the [`cp_drawable_t`](./cp_drawable_t.md) only when you’re ready to start encoding commands into your Metal command buffers. The system recycles frames and their drawables for efficiency, so if you retrieve the drawable too early, it might not be ready to use.

Use the drawable’s [`LayerRenderer.Drawable.View`](./layerrenderer/drawable/view.md) instances to determine where to draw your content in the provided textures. After you finish encoding your content, call [`encodePresent(commandBuffer:)`](./layerrenderer/drawable/encodepresent%28commandbuffer%29.md) to add a presentation notification to your command buffer. This command tells the system when to display the frame, and is essential for displaying your frame on time.

## Topics

### Getting the views
- [cp_drawable_get_view_count](./cp_drawable_get_view_count.md)
  Returns the number of separate views to draw for the frame.
- [cp_drawable_get_view](./cp_drawable_get_view.md)
  Returns the specified view from the drawable.
### Accessing the device orientation
- [cp_drawable_get_device_anchor](./cp_drawable_get_device_anchor.md)
  Returns the position and orientation you specified for the frame.
- [cp_drawable_set_device_anchor](./cp_drawable_set_device_anchor.md)
  Specifies the world position and orientation to apply to the current frame.
### Getting the render textures
- [cp_drawable_get_texture_count](./cp_drawable_get_texture_count.md)
  Returns the number of color and depth textures available in the drawable.
- [cp_drawable_get_depth_texture](./cp_drawable_get_depth_texture.md)
  Returns the depth texture at the specified index in the drawable.
- [cp_drawable_get_color_texture](./cp_drawable_get_color_texture.md)
  Returns the color texture at the specified index in the drawable.
### Enqueueing a command buffer
- [func encodePresent(commandBuffer: any MTLCommandBuffer)](./layerrenderer/drawable/encodepresent%28commandbuffer%29.md)
  Encodes a notification event to the specified command buffer to present the drawable’s content onscreen.
### Getting the rasterization rate map
- [cp_drawable_get_rasterization_rate_map_count](./cp_drawable_get_rasterization_rate_map_count.md)
  Returns the number of rasterization rate maps associated with the drawable.
- [cp_drawable_get_rasterization_rate_map](./cp_drawable_get_rasterization_rate_map.md)
  Returns the rasterization rate map at the specified index in the drawable.
- [cp_drawable_get_flipped_rasterization_rate_map](./cp_drawable_get_flipped_rasterization_rate_map.md)
  Returns the flipped rasterization rate map at the specified index in the drawable.
### Getting the projection matrix
- [enum AxisDirectionConvention](./axisdirectionconvention.md)
  Constants that indicate the axis and direction to use for a perspective projection matrix.
### Accessing pixel depth information
- [var depthRange: simd_float2](./layerrenderer/drawable/depthrange.md)
  The distances to the far and near clipping planes from the person viewing the content, in meters.
- [cp_drawable_set_depth_range](./cp_drawable_set_depth_range.md)
  Sets the distances to the near and far clipping planes for the current drawable.
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
- [typealias CompositorFrameIndex](./compositorframeindex.md)
  The sequential index for a frame in the compositor’s timeline.
### Getting the drawable type
- [cp_drawable_t](./cp_drawable_t.md)
  A type that provides the textures and information you need to draw a frame of content.

## See Also

### Drawing environment
- [View](./view.md)
  A type that manages the viewport and texture details for each portion of your frame’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/drawable)*