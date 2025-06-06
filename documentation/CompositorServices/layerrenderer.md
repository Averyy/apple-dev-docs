# LayerRenderer

**Framework**: Compositor Services  
**Kind**: class

A type that provides the Metal types and timing information you need to draw your content.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
class LayerRenderer
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Overview

A layer renderer type creates a bridge between a SwiftUI scene and the Metal code you use to draw fully immersive experiences. When you present an immersive space with [`CompositorLayer`](compositorlayer.md) content, the system creates a [`LayerRenderer`](layerrenderer.md) type and makes it available to the content’s closure. Use the information in the layer renderer to set up your app’s rendering loop, and to start drawing frames of content.

Each layer renderer has information that tells the system how to configure the Metal textures and data types your app needs. Compositor Services provides a default configuration for layers, but you can customize the configuration as needed. Specify your custom configuration details using the [`CompositorLayerConfiguration`](compositorlayerconfiguration.md) protocol and pass a type with those details to the initializer for your immersive space’s content. Use the layer renderer’s capability information to validate any configuration choices you make.

For information about how to create and configure a layer renderer and use it to run your rendering loop, see [`Drawing fully immersive content using Metal`](drawing-fully-immersive-content-using-metal.md).

## Topics

### Configuring the layer renderer
- [var configuration: LayerRenderer.Configuration](layerrenderer/configuration-swift.property.md)
  The configuration details for the specified layer.
- [LayerRenderer.Configuration](layerrenderer/configuration-swift.struct.md)
  A type that stores the texture formats, layout information, and other details you use to configure your rendering loop code.
- [LayerRenderer.Capabilities](layerrenderer/capabilities.md)
  The color formats, depth formats, and features that you can use to configure your rendering engine.
### Getting the layer renderer properties
- [var properties: LayerRenderer.Properties](layerrenderer/properties-swift.property.md)
  The configured properties of the layer renderer.
- [LayerRenderer.Properties](layerrenderer/properties-swift.struct.md)
  A type that describes the organization of the layer renderer’s textures and the relationships between those textures and the views you use for drawing.
### Getting the GPU device
- [var device: any MTLDevice](layerrenderer/device.md)
  The GPU device that the layer renderer uses for drawing operations
### Managing the rendering loop
- [var state: LayerRenderer.State](layerrenderer/state-swift.property.md)
  A value that indicates whether the layer renderer is currently visible and ready for you to draw content.
- [func waitUntilRunning()](layerrenderer/waituntilrunning.md)
  Stops further execution of your code until the layer renderer leaves the paused state.
- [LayerRenderer.State](layerrenderer/state-swift.enum.md)
  The states of the layer renderer, which tell you how to proceed with drawing operations.
- [LayerRenderer.Clock](layerrenderer/clock.md)
  A type that supports operations that require a precise time measurement.
### Drawing a frame of content
- [func queryNextFrame() -> LayerRenderer.Frame?](layerrenderer/querynextframe.md)
  Returns the next frame to use for drawing.
- [LayerRenderer.Frame](layerrenderer/frame.md)
  A type that provides access to the timing information and data types you need to render a single frame of content.
- [LayerRenderer.Drawable](layerrenderer/drawable.md)
  A type that provides the textures and information you need to draw a frame of content.
### Handling events
- [var onSpatialEvent: (SpatialEventCollection) -> Void](layerrenderer/onspatialevent.md)
  A closure that receives spatial event updates from the layer renderer.
### Configuring the frame update rate
- [var minimumFrameRepeatCount: Int32](layerrenderer/minimumframerepeatcount.md)
  The number of additional frames for which the system displays the same content.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [LayerRenderer.Frame](layerrenderer/frame.md)
  A type that provides access to the timing information and data types you need to render a single frame of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer)*