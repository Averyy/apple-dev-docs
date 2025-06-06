# transform

**Framework**: Model I/O  
**Kind**: property

The transformation to be applied to texture coordinate data before sampling from the texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var transform: MDLTransform? { get set }
```

#### Discussion

Use this property to translate, scale, or rotate a texture relative to the surfaces it’s rendered on.

## See Also

- [var texture: MDLTexture?](mdltexturesampler/texture.md)
  The texture object that provides image data for sampling.
- [var hardwareFilter: MDLTextureFilter?](mdltexturesampler/hardwarefilter.md)
  An object that describes filtering modes for sampling from the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexturesampler/transform)*