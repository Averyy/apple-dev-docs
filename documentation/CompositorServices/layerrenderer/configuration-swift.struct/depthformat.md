# depthFormat

**Framework**: Compositor Services  
**Kind**: property

The pixel format to use for the layer’s depth textures.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var depthFormat: MTLPixelFormat { get set }
```

#### Discussion

Use this value to determine the pixel format for depth textures in a frame. At configuration time, set the value to specify which pixel format you want.

## See Also

- [var depthUsage: MTLTextureUsage](layerrenderer/configuration-swift.struct/depthusage.md)
  The texture usage value to apply to the layer’s depth textures.
- [var defaultDepthRange: SIMD2<Float>](layerrenderer/configuration-swift.struct/defaultdepthrange.md)
  The distances to the far and near clipping planes that define the bounds of your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/configuration-swift.struct/depthformat)*