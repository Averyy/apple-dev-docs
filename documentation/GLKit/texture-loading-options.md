# Texture Loading Options

**Framework**: GLKit

Keys to specify in a `textureOperations` dictionary.

## Topics

### Constants
- [let GLKTextureLoaderApplyPremultiplication: String](glktextureloaderapplypremultiplication.md)
  Whether image data should be premultiplied before being loaded into the sharegroup.
- [let GLKTextureLoaderGenerateMipmaps: String](glktextureloadergeneratemipmaps.md)
  Whether or not to create mipmaps for a texture.
- [let GLKTextureLoaderOriginBottomLeft: String](glktextureloaderoriginbottomleft.md)
  Whether or not to vertically flip image data to match OpenGL’s coordinate system.
- [let GLKTextureLoaderGrayscaleAsAlpha: String](glktextureloadergrayscaleasalpha.md)
  Whether or not to treat greyscale image data as alpha information.
- [let GLKTextureLoaderSRGB: String](glktextureloadersrgb.md)
  Whether or not to treat texture image data as sRGB data.

## See Also

- [typealias GLKTextureLoaderCallback](glktextureloadercallback.md)
  Signature for the block executed after an asynchronous texture loading operation completes.
- [Texture Error Handling](texture-error-handling.md)
  Strings used when handling error messages returned from a texture loading method.
- [GLKTextureLoaderError.Code](glktextureloadererror-swift.struct/code.md)
  Values to be returned when a texture loader encounters an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/texture-loading-options)*