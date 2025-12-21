# defaultDepthRange

**Framework**: Compositor Services  
**Kind**: property

The distances to the far and near clipping planes that define the bounds of your content.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var defaultDepthRange: SIMD2<Float> { get set }
```

#### Discussion

The near and far planes reflect the distances from the person viewing the content. Compositor Services uses these values to compute the perspective projection matrix and to clip content that is between the camera and the near plane, or located beyond the far plane.

The distances in this property are in meters. The values are in reverse-z ordering, with the value for the far plane in the vector’s `x` property and the value for the near plane in the vector’s `y` property.

## See Also

- [var depthFormat: MTLPixelFormat](layerrenderer/configuration-swift.struct/depthformat.md)
  The pixel format to use for the layer’s depth textures.
- [var depthUsage: MTLTextureUsage](layerrenderer/configuration-swift.struct/depthusage.md)
  The texture usage value to apply to the layer’s depth textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/configuration-swift.struct/defaultdepthrange)*