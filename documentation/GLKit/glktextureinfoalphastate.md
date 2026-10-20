# GLKTextureInfoAlphaState

**Framework**: GLKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum GLKTextureInfoAlphaState : GLint;
```

## Topics

### Constants
- [GLKTextureInfoAlphaState.none](./glktextureinfoalphastate/none.md)
  Indicates that the texture has no alpha information.
- [GLKTextureInfoAlphaState.nonPremultiplied](./glktextureinfoalphastate/nonpremultiplied.md)
  Indicates that the color values in the texture were not premultiplied by the alpha value.
- [GLKTextureInfoAlphaState.premultiplied](./glktextureinfoalphastate/premultiplied.md)
  Indicates that the color values in the texture have already been premultiplied by the alpha value.
### Initializers
- [init?(rawValue: GLint)](./glktextureinfoalphastate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum GLKTextureInfoOrigin](./glktextureinfoorigin.md)
  The location of the origin in the original source image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureinfoalphastate)*