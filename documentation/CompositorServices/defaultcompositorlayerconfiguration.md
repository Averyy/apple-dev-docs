# DefaultCompositorLayerConfiguration

**Framework**: Compositor Services  
**Kind**: struct

A type that configures the layer with the default texture configurations and rendering behaviors for the current device.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct DefaultCompositorLayerConfiguration
```

#### Overview

Use this type when your Metal rendering engine uses the default rendering options.

## Relationships

### Conforms To
- [CompositorLayerConfiguration](compositorlayerconfiguration.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)
  Create a fully immersive experience in visionOS using a custom Metal-based rendering engine.
- [Interacting with virtual content blended with passthrough](interacting-with-virtual-content-blended-with-passthrough.md)
  Present a mixed immersion style space to draw content in a person’s surroundings, and choose how upper limbs appear with respect to rendered content.
- [struct CompositorLayer](compositorlayer.md)
  A type that you use with an immersive space to display fully immersive content using Metal.
- [protocol CompositorLayerConfiguration](compositorlayerconfiguration.md)
  An interface for specifying the texture configurations and rendering behaviors to use with your Metal rendering engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/defaultcompositorlayerconfiguration)*