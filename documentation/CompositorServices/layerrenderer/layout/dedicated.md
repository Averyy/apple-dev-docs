# LayerRenderer.Layout.dedicated

**Framework**: Compositor Services  
**Kind**: case  
**Role**: Case

A layout that assigns a separate texture to each rendered view.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
case dedicated
```

```c
cp_layer_renderer_layout_dedicated
```

## Mentions

- [Drawing fully immersive content using Metal](../../drawing-fully-immersive-content-using-metal.md)

#### Discussion

Each view receives its own dedicated texture, and the type of each texture is [`MTLTextureType.type2D`](../../../Metal/mtltexturetype/type2d.md). Because each texture is separate, when there are multiple textures, you must perform a separate render pass for each texture.

## See Also

### Getting the texture layouts
- [LayerRenderer.Layout.shared](./shared.md)
  A layout that uses a single texture to store the content for all rendered views.
- [LayerRenderer.Layout.layered](./layered.md)
  A layout that specifies each view’s content as a slice of a single texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/layout/dedicated)*