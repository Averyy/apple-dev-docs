# commandQueue

**Framework**: Compositor Services  
**Kind**: property

Returns the command queue that the layer uses for drawing operations.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var commandQueue: any MTL4CommandQueue { get }
```

#### Discussion

Should only be called with when supporting Metal4 through configuration. [`cp_layer_renderer_configuration_set_supports_mtl4`](cp_layer_renderer_configuration_set_supports_mtl4.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/commandqueue)*