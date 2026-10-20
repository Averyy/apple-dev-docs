# colorUsage

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The texture usage value to apply to the layer’s color textures.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var colorUsage: MTLTextureUsage { get set }
```

#### Discussion

Metal optimizes texture-related operations based on the value in this property. The usage value can be a combination of options. For more information, see [`MTLTextureUsage`](../../../Metal/mtltextureusage.md).

## See Also

### Configuring the color textures
- [var colorFormat: MTLPixelFormat](./colorformat.md)
  The pixel format to use for color textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/configuration-swift.struct/colorusage)*