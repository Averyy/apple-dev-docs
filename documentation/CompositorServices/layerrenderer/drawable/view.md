# LayerRenderer.Drawable.View

**Framework**: Compositor Services  
**Kind**: struct

A type that provides information on how to render content into the frame’s textures.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct View
```

#### Overview

Compositor Services provides a view for each distinct render viewpoint. For example, a head-mounted display typically contains two views: one for each eye. Use the information in the views to set up your render pass descriptor, or to determine which part of a texture to fill with content.

## Topics

### Getting the view’s texture map
- [var textureMap: LayerRenderer.Drawable.View.TextureMap](layerrenderer/drawable/view/texturemap-swift.property.md)
  The texture map for a view.
- [LayerRenderer.Drawable.View.TextureMap](layerrenderer/drawable/view/texturemap-swift.struct.md)
  A type that provides details about the textures associated with a view.
### Getting the transformations
- [var transform: simd_float4x4](layerrenderer/drawable/view/transform.md)
  The transformation matrix that converts between the device’s coordinate space to the position of the view in that space.
- [var tangents: simd_float4](layerrenderer/drawable/view/tangents.md)
  The tangent values for the angles you use to determine the planes of the viewing frustum.
### Creating a view
- [init()](layerrenderer/drawable/view/init.md)
  Creates a view type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [LayerRenderer.Drawable](layerrenderer/drawable.md)
  A type that provides the textures and information you need to draw a frame of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/view)*