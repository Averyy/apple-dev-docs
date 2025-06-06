# layout

**Framework**: Compositor Services  
**Kind**: property

The layout being used by the layer.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var layout: LayerRenderer.Layout { get set }
```

#### Discussion

Layouts define how Compositor Services creates the color and depth textures it passes to your app. A layout might use separate textures for each view, or combine the content from multiple views into a single texture. The layout type also determines which Metal texture type to create. For more information about the supported layouts, see [`LayerRenderer.Layout`](layerrenderer/layout.md).

## See Also

- [LayerRenderer.Layout](layerrenderer/layout.md)
  Constants that specify the organization of the textures you use for drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/configuration-swift.struct/layout)*