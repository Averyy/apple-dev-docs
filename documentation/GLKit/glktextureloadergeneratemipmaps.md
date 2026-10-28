# GLKTextureLoaderGenerateMipmaps

**Framework**: GLKit  
**Kind**: var  
**Role**: Global Variable

Whether or not to create mipmaps for a texture.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
let GLKTextureLoaderGenerateMipmaps: String
```

```c
extern NSString * const GLKTextureLoaderGenerateMipmaps;
```

## Discussion

The value for this key is an [`NSNumber`](../Foundation/nsnumber.md) object that specifies a boolean value. If [`false`](../Swift/false.md), only the texture is loaded. If [`true`](../Swift/true.md), a full set of mipmap levels are generated for the texture when the texture is created. The `GL_TEXTURE_MIN_FILTER` parameter for the texture is changed to `GL_LINEAR_MIPMAP_LINEAR` when mipmaps are generated. If the key is not specified, the default value is [`false`](../Swift/false.md).

## See Also

### Constants
- [let GLKTextureLoaderApplyPremultiplication: String](./glktextureloaderapplypremultiplication.md)
  Whether image data should be premultiplied before being loaded into the sharegroup.
- [let GLKTextureLoaderErrorDomain: String](./glktextureloadererrordomain.md)
  The error domain used by GLKit when returning texture loading errors.
- [let GLKTextureLoaderErrorKey: String](./glktextureloadererrorkey.md)
  A key used to retrieve an error string from an error object userinfo dictionary.
- [let GLKTextureLoaderGLErrorKey: String](./glktextureloaderglerrorkey.md)
  A key used to retrieve additional information from an error object’s userinfo dictionary.
- [let GLKTextureLoaderGrayscaleAsAlpha: String](./glktextureloadergrayscaleasalpha.md)
  Whether or not to treat greyscale image data as alpha information.
- [let GLKTextureLoaderOriginBottomLeft: String](./glktextureloaderoriginbottomleft.md)
  Whether or not to vertically flip image data to match OpenGL’s coordinate system.
- [let GLKTextureLoaderSRGB: String](./glktextureloadersrgb.md)
  Whether or not to treat texture image data as sRGB data.
- [var GLK_SSE3_INTRINSICS: Int32](./glk_sse3_intrinsics.md)
- [let kGLKModelErrorDomain: String](./kglkmodelerrordomain.md)
- [let kGLKModelErrorKey: String](./kglkmodelerrorkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloadergeneratemipmaps)*