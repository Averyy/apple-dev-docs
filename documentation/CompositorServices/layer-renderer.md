# Layer renderer

**Framework**: Compositor Services  
**Role**: API Collection

A type that provides the Metal types and timing information you need to draw your content.

## Overview

A layer renderer type creates a bridge between a SwiftUI scene and the Metal code you use to draw fully immersive experiences. When you present an immersive space with [`CompositorLayer`](./compositorlayer.md) content, the system creates a [`cp_layer_renderer_t`](./cp_layer_renderer_t.md) type and makes it available to the content’s closure. Use the information in the layer renderer to set up your app’s rendering loop, and to start drawing frames of content.

Each layer renderer has information that tells the system how to configure the Metal textures and data types your app needs. Compositor Services provides a default configuration for layer renderers, but you can customize the configuration as needed. Specify your custom configuration details using the [`CompositorLayerConfiguration`](./compositorlayerconfiguration.md) protocol and pass a type with those details to the initializer for your immersive space’s content. Use the layer renderer’s capability information to validate any configuration choices you make.

For information about how to create and configure a layer and use it to run your rendering loop, see [Drawing fully immersive content using Metal](./drawing-fully-immersive-content-using-metal.md).

## Topics

### Configuring the layer
- [Layer capabilities](./layer-capabilities.md)
  The color formats, depth formats, and features that you can use to configure your rendering engine.
- [Layer configuration](./layer-configuration.md)
  The pixel formats, depth mask, texture layout, and other drawing-related settings you use to configure your drawing code.
- [Layer properties](./layer-properties.md)
  Information about the textures and views that the system created for your drawing code.
### Getting the GPU device
- [var device: any MTLDevice](./layerrenderer/device.md)
  The GPU device that the layer renderer uses for drawing operations
### Managing the rendering loop
- [var state: LayerRenderer.State](./layerrenderer/state-swift.property.md)
  A value that indicates whether the layer renderer is currently visible and ready for you to draw content.
- [func waitUntilRunning()](./layerrenderer/waituntilrunning%28%29.md)
  Stops further execution of your code until the layer renderer leaves the paused state.
- [LayerRenderer.State](./layerrenderer/state-swift.enum.md)
  The states of the layer renderer, which tell you how to proceed with drawing operations.
### Drawing a frame of content
- [cp_layer_renderer_query_next_frame](./cp_layer_renderer_query_next_frame.md)
  Returns the next frame to use for drawing.
- [typealias LayerFrameIndex](./layerframeindex.md)
  A frame index in the layer’s timeline.
### Configuring the frame update rate
- [var minimumFrameRepeatCount: Int32](./layerrenderer/minimumframerepeatcount.md)
  The number of additional frames for which the system displays the same content.
- [cp_layer_renderer_set_minimum_frame_repeat_count](./cp_layer_renderer_set_minimum_frame_repeat_count.md)
  Sets the number of additional times the system displays a frame.
### Getting the layer type
- [cp_layer_renderer_t](./cp_layer_renderer_t.md)
  A type that provides the Metal types and timing information you need to draw your content.
- [class LayerRenderer](./layerrenderer.md)
  A type that provides the Metal types and timing information you need to draw your content.

## See Also

### Render-loop setup
- [Frames](./frames.md)
  A type that represents a single frame of content, manages the pace of animations, and provides access to the drawable environment.
- [Utilities](./utilities.md)
  Common types and utilities to manage your app’s rendering process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layer-renderer)*