# cp_layer_renderer_configuration_t

**Framework**: Compositor Services  
**Kind**: typealias  
**Role**: Type Alias

A type that stores the texture formats, layout information, and other details you use to configure your rendering loop code.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
typedef CP_OBJECT_cp_layer_renderer_configuration * cp_layer_renderer_configuration_t;
```

#### Discussion

A [`cp_layer_renderer_configuration_t`](./cp_layer_renderer_configuration_t.md) type stores the configuration options for your app’s `cp_layer_t` object. When configuring the content for your app’s immersive space, use this type to specify information about the texture layouts, pixel formats, and rendering options you want. The system uses the provided information to initialize the `cp_layer_t` object. It also uses the information to create the Metal textures and other data structures that you use for each frame of content.

You don’t create this type directly. When implementing the `makeConfiguration` method of your `CompositorConfiguration` type, the system passes a set of default configuration values for you to modify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_t)*