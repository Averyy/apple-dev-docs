# cp_layer_renderer_capabilities_t

**Framework**: Compositor Services  
**Kind**: typealias  
**Role**: Type Alias

A type that stores the texture formats and options the layer supports.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
typedef CP_OBJECT_cp_layer_renderer_capabilities * cp_layer_renderer_capabilities_t;
```

#### Discussion

A [`cp_layer_renderer_capabilities_t`](./cp_layer_renderer_capabilities_t.md) type  stores information about what options the layer currently supports. When specifying the configuration details for your layer, use the information in this type to verify your configuration is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_t)*