# depthUsage

**Framework**: Compositor Services  
**Kind**: property

The texture usage value to apply to the layer’s depth textures.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var depthUsage: MTLTextureUsage { get set }
```

#### Discussion

Metal optimizes texture-related operations based on the value in this property. The usage value can be a combination of options. For more information, see [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage).

## See Also

- [var depthFormat: MTLPixelFormat](layerrenderer/configuration-swift.struct/depthformat.md)
  The pixel format to use for the layer’s depth textures.
- [var defaultDepthRange: SIMD2<Float>](layerrenderer/configuration-swift.struct/defaultdepthrange.md)
  The distances to the far and near clipping planes that define the bounds of your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/configuration-swift.struct/depthusage)*