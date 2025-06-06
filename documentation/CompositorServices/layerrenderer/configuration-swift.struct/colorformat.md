# colorFormat

**Framework**: Compositor Services  
**Kind**: property

The pixel format to use for color textures.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var colorFormat: MTLPixelFormat { get set }
```

#### Discussion

Use this value to determine the pixel format for color textures in a frame. At configuration time, set the value to specify which pixel format you want.

> **Note**:  Apple Vision Pro uses the P3 color space for pixel color values.

 Apple Vision Pro uses the P3 color space for pixel color values.

## See Also

- [var colorUsage: MTLTextureUsage](layerrenderer/configuration-swift.struct/colorusage.md)
  The texture usage value to apply to the layer’s color textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/configuration-swift.struct/colorformat)*