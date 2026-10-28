# GLKTextureInfoOrigin

**Framework**: GLKit  
**Kind**: enum  
**Role**: Enumeration

The location of the origin in the original source image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
enum GLKTextureInfoOrigin
```

```c
enum GLKTextureInfoOrigin : GLint;
```

## Overview

The origin’s position has no effect on how the texture is loaded into the context. If you need to flip the image before loading it, your app must explicitly add the GLKTextureOriginBottomLeft key to the options dictionary provided when loading the texture.

## Topics

### Constants
- [GLKTextureInfoOrigin.unknown](./glktextureinfoorigin/unknown.md)
  The origin of the texture is not supported.
- [GLKTextureInfoOrigin.topLeft](./glktextureinfoorigin/topleft.md)
  The origin of the texture is in the top-left corner.
- [GLKTextureInfoOrigin.bottomLeft](./glktextureinfoorigin/bottomleft.md)
  The origin of the texture is in the bottom-left corner.
### Initializers
- [init?(rawValue: GLint)](./glktextureinfoorigin/init%28rawvalue%29.md)

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
- [enum GLKTextureInfoAlphaState](./glktextureinfoalphastate.md)
  Values that describe the alpha information stored in a source image’s pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureinfoorigin)*