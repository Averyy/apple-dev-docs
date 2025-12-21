# init(configuration:)

**Framework**: Compositor Services  
**Kind**: init

Creates a set of properties using the specified configuration values.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
init(configuration: LayerRenderer.Configuration) throws
```

#### Discussion

Prior to receiving the layer you use for drawing, you can create a [`LayerRenderer.Properties`](layerrenderer/properties-swift.struct.md) structure and use it to start the configuration of your Metal code.

## Parameters

- `configuration`: The options you use to configure your Metal rendering engine. Specify the same options you use during drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/properties-swift.struct/init(configuration:))*