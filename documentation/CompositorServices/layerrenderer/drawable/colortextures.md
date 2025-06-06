# colorTextures

**Framework**: Compositor Services  
**Kind**: property

An array of color textures to use to render the current frame.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var colorTextures: [any MTLTexture] { get }
```

#### Discussion

The layer’s texture topology determines the total number of textures in the array, and the layout and content for each texture. Use the drawable’s views to map your content into specific portions of the textures.

## See Also

- [var depthTextures: [any MTLTexture]](layerrenderer/drawable/depthtextures.md)
  An array of depth textures to use to render the current frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/colortextures)*