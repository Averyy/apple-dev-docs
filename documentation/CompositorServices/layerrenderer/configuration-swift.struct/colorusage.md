# colorUsage

**Framework**: Compositor Services  
**Kind**: property

The texture usage value to apply to the layer’s color textures.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
var colorUsage: MTLTextureUsage { get set }
```

#### Discussion

Metal optimizes texture-related operations based on the value in this property. The usage value can be a combination of options. For more information, see [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage).

## See Also

- [var colorFormat: MTLPixelFormat](layerrenderer/configuration-swift.struct/colorformat.md)
  The pixel format to use for color textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/configuration-swift.struct/colorusage)*