# hardwareFilter

**Framework**: Model I/O  
**Kind**: property

An object that describes filtering modes for sampling from the texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var hardwareFilter: MDLTextureFilter? { get set }
```

#### Discussion

Filtering modes specify the behavior of texture sampling at different sizes and texture coordinates.

## See Also

- [var texture: MDLTexture?](mdltexturesampler/texture.md)
  The texture object that provides image data for sampling.
- [var transform: MDLTransform?](mdltexturesampler/transform.md)
  The transformation to be applied to texture coordinate data before sampling from the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexturesampler/hardwarefilter)*