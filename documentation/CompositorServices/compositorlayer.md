# CompositorLayer

**Framework**: Compositor Services  
**Kind**: struct

A type that you use with an immersive space to display fully immersive content using Metal.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct CompositorLayer
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Overview

Use a [`CompositorLayer`](compositorlayer.md) to specify the content of an [`ImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace) when you want to render that content yourself using Metal. When you present a space with this content, Compositor Services creates a [`LayerRenderer`](layerrenderer.md) type for you to use with your rendering code. The layer renderer provides configuration details, timing information, and the Metal types and information you need to configure your rendering loop and manage the rendering process.

The following example shows a [`ImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace) that uses a [`CompositorLayer`](compositorlayer.md) to specify its content. Use the closure for the [`CompositorLayer`](compositorlayer.md) to set up and start your Metal rendering code. In this example, Compositor Services creates the layer using a default set of Metal configuration options. To customize the configuration of your Metal rendering environment, pass a custom [`CompositorLayerConfiguration`](compositorlayerconfiguration.md) type to your [`CompositorLayer`](compositorlayer.md) at initialization time.

```swift
ImmersiveSpace(id: "MyContent") {
    CompositorLayer { layerRenderer in
        // Set up and run the Metal render loop.
            let renderThread = Thread {
                let engine = my_engine_create(layerRenderer)
                my_engine_render_loop(engine)
            }
            renderThread.name = "Render Thread"
            renderThread.start()
        }
    }
}
```

For more information about how to set up and start your Metal rendering engine, see [`Drawing fully immersive content using Metal`](drawing-fully-immersive-content-using-metal.md).

## Topics

### Initializers
- [init(configuration: any CompositorLayerConfiguration, renderer: (LayerRenderer) -> Void)](compositorlayer/init(configuration:renderer:).md)
- [init(configuration: any CompositorLayerConfiguration, renderer: (LayerRenderer) -> Void, Void)](compositorlayer/init(configuration:renderer:_:).md)

## Relationships

### Conforms To
- [ImmersiveSpaceContent](../SwiftUI/ImmersiveSpaceContent.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)
  Create a fully immersive experience in visionOS using a custom Metal-based rendering engine.
- [Interacting with virtual content blended with passthrough](interacting-with-virtual-content-blended-with-passthrough.md)
  Present a mixed immersion style space to draw content in a person’s surroundings, and choose how upper limbs appear with respect to rendered content.
- [protocol CompositorLayerConfiguration](compositorlayerconfiguration.md)
  An interface for specifying the texture configurations and rendering behaviors to use with your Metal rendering engine.
- [struct DefaultCompositorLayerConfiguration](defaultcompositorlayerconfiguration.md)
  A type that configures the layer with the default texture configurations and rendering behaviors for the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/compositorlayer)*