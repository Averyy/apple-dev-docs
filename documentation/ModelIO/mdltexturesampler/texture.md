# texture

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The texture object that provides image data for sampling.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var texture: MDLTexture? { get set }
```

```objc
@property (nonatomic, retain, nullable) MDLTexture * texture;
```

#### Discussion

A [`MDLTexture`](../mdltexture.md) object describes texture image data.

## See Also

### Working with Texture Parameters
- [var hardwareFilter: MDLTextureFilter?](./hardwarefilter.md)
  An object that describes filtering modes for sampling from the texture.
- [var transform: MDLTransform?](./transform.md)
  The transformation to be applied to texture coordinate data before sampling from the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexturesampler/texture)*