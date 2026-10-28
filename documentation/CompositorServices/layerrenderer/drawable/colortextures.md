# colorTextures

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

An array of color textures to use to render the current frame.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var colorTextures: [any MTLTexture] { get }
```

## Discussion

The layer’s texture topology determines the total number of textures in the array, and the layout and content for each texture. Use the drawable’s views to map your content into specific portions of the textures.

## See Also

### Getting the render textures
- [var depthTextures: [any MTLTexture]](./depthtextures.md)
  An array of depth textures to use to render the current frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/colortextures)*