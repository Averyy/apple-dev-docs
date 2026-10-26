# cp_view_t

**Framework**: Compositor Services  
**Kind**: typealias  
**Role**: Type Alias

A type that provides information on how to render content into the frame’s textures.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
typedef struct cp_view * cp_view_t;
```

#### Discussion

Compositor Services provides a view for each distinct render viewpoint. For example, a head-mounted display typically contains two views: one for each eye. Use the information in the views to set up your render pass descriptor, or to determine which part of a texture to fill with content.

## Topics

### Getting the view’s texture map
- [var textureMap: LayerRenderer.Drawable.View.TextureMap](./layerrenderer/drawable/view/texturemap-swift.property.md)
  The texture map for a view.
- [cp_view_texture_map_t](./cp_view_texture_map_t.md)
  A type that provides details about the textures associated with a view.
### Getting the transformations
- [var transform: simd_float4x4](./layerrenderer/drawable/view/transform.md)
  The transformation matrix that converts between the device’s coordinate space to the position of the view in that space.
- [var tangents: simd_float4](./layerrenderer/drawable/view/tangents.md)
  The tangent values for the angles you use to determine the planes of the viewing frustum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_view_t)*