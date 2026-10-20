# LayerRenderer.Layout.layered

**Framework**: Compositor Services  
**Kind**: case  
**Role**: Case

A layout that specifies each view’s content as a slice of a single texture.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
case layered
```

```c
cp_layer_renderer_layout_layered
```

## Mentions

- [Drawing fully immersive content using Metal](../../drawing-fully-immersive-content-using-metal.md)

#### Discussion

The layout uses a single texture to store the content for all rendered views. The type of the texture is [`MTLTextureType.type2DArray`](../../../Metal/mtltexturetype/type2darray.md). The texture map’s slice index indicates which array slot contains each view’s content.

## See Also

### Getting the texture layouts
- [LayerRenderer.Layout.dedicated](./dedicated.md)
  A layout that assigns a separate texture to each rendered view.
- [LayerRenderer.Layout.shared](./shared.md)
  A layout that uses a single texture to store the content for all rendered views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/layout/layered)*