# GLKTextureLoaderSRGB

**Framework**: GLKit  
**Kind**: var

Whether or not to treat texture image data as sRGB data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.9+
- tvOS 9.0+

## Declaration

```swift
let GLKTextureLoaderSRGB: String
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object that specifies a boolean value. If [`false`](https://developer.apple.com/documentation/swift/false), the image data is treated as linear pixel data. If [`true`](https://developer.apple.com/documentation/swift/true), the image data is treated as sRGB pixel data. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [let GLKTextureLoaderApplyPremultiplication: String](glktextureloaderapplypremultiplication.md)
  Whether image data should be premultiplied before being loaded into the sharegroup.
- [let GLKTextureLoaderErrorDomain: String](glktextureloadererrordomain.md)
  The error domain used by GLKit when returning texture loading errors.
- [let GLKTextureLoaderErrorKey: String](glktextureloadererrorkey.md)
  A key used to retrieve an error string from an error object userinfo dictionary.
- [let GLKTextureLoaderGLErrorKey: String](glktextureloaderglerrorkey.md)
  A key used to retrieve additional information from an error object’s userinfo dictionary.
- [let GLKTextureLoaderGenerateMipmaps: String](glktextureloadergeneratemipmaps.md)
  Whether or not to create mipmaps for a texture.
- [let GLKTextureLoaderGrayscaleAsAlpha: String](glktextureloadergrayscaleasalpha.md)
  Whether or not to treat greyscale image data as alpha information.
- [let GLKTextureLoaderOriginBottomLeft: String](glktextureloaderoriginbottomleft.md)
  Whether or not to vertically flip image data to match OpenGL’s coordinate system.
- [var GLK_SSE3_INTRINSICS: Int32](glk_sse3_intrinsics.md)
- [let kGLKModelErrorDomain: String](kglkmodelerrordomain.md)
- [let kGLKModelErrorKey: String](kglkmodelerrorkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloadersrgb)*