# GLKTextureInfoAlphaState

**Framework**: GLKit  
**Kind**: enum

Values that describe the alpha information stored in a source image’s pixel data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
enum GLKTextureInfoAlphaState
```

## Topics

### Constants
- [GLKTextureInfoAlphaState.none](glktextureinfoalphastate/none.md)
  Indicates that the texture has no alpha information.
- [GLKTextureInfoAlphaState.nonPremultiplied](glktextureinfoalphastate/nonpremultiplied.md)
  Indicates that the color values in the texture were not premultiplied by the alpha value.
- [GLKTextureInfoAlphaState.premultiplied](glktextureinfoalphastate/premultiplied.md)
  Indicates that the color values in the texture have already been premultiplied by the alpha value.
### Initializers
- [init?(rawValue: GLint)](glktextureinfoalphastate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum GLKTextureInfoOrigin](glktextureinfoorigin.md)
  The location of the origin in the original source image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureinfoalphastate)*