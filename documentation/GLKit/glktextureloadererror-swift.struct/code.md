# GLKTextureLoaderError.Code

**Framework**: GLKit  
**Kind**: enum  
**Role**: Enumeration

Values to be returned when a texture loader encounters an error.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
enum Code
```

```c
enum GLKTextureLoaderError : GLuint;
```

## Topics

### Initializers
- [init?(rawValue: GLuint)](./code/init%28rawvalue%29.md)
### Type Properties
- [GLKTextureLoaderError.Code.alphaPremultiplicationFailure](./code/alphapremultiplicationfailure.md)
  The texture source data does not allow the alpha to be premultiplied.
- [GLKTextureLoaderError.Code.compressedTextureUpload](./code/compressedtextureupload.md)
  A compressed texture could not be uploaded.
- [GLKTextureLoaderError.Code.cubeMapInvalidNumFiles](./code/cubemapinvalidnumfiles.md)
  The incorrect number of files were specified for the cube map.
- [GLKTextureLoaderError.Code.dataPreprocessingFailure](./code/datapreprocessingfailure.md)
  The data could not be preprocessed correctly.
- [static var errorDomain: String](./errordomain.md)
- [GLKTextureLoaderError.Code.fileOrURLNotFound](./code/fileorurlnotfound.md)
  A file could not be found at the path provided.
- [GLKTextureLoaderError.Code.incompatibleFormatSRGB](./code/incompatibleformatsrgb.md)
  The decoded data was in an incompatible format for an sRGB texture.
- [GLKTextureLoaderError.Code.invalidCGImage](./code/invalidcgimage.md)
  The image provided was invalid.
- [GLKTextureLoaderError.Code.invalidEAGLContext](./code/invalideaglcontext.md)
  The EAGL context was not a valid context.
- [GLKTextureLoaderError.Code.invalidNSData](./code/invalidnsdata.md)
  The data provided is not in a recognized image format.
- [GLKTextureLoaderError.Code.mipmapUnsupported](./code/mipmapunsupported.md)
  The texture source data does not allow mipmaps to be generated.
- [GLKTextureLoaderError.Code.pvrAtlasUnsupported](./code/pvratlasunsupported.md)
  Cube maps may not be compressed in PVRTC format.
- [GLKTextureLoaderError.Code.reorientationFailure](./code/reorientationfailure.md)
  The texture source data does not allow the image to be reoriented.
- [GLKTextureLoaderError.Code.uncompressedTextureUpload](./code/uncompressedtextureupload.md)
  An uncompressed texture could not be uploaded.
- [GLKTextureLoaderError.Code.unknownFileType](./code/unknownfiletype.md)
  The file was in an unrecognized format.
- [GLKTextureLoaderError.Code.unknownPathType](./code/unknownpathtype.md)
  The path type was unrecognized.
- [GLKTextureLoaderError.Code.unsupportedBitDepth](./code/unsupportedbitdepth.md)
  The data in the source image has an unsupported bit depth.
- [GLKTextureLoaderError.Code.unsupportedCubeMapDimensions](./code/unsupportedcubemapdimensions.md)
  The cube map’s dimensions are incorrect.
- [GLKTextureLoaderError.Code.unsupportedOrientation](./code/unsupportedorientation.md)
  The texture source data is stored with an unsupported origin position.
- [GLKTextureLoaderError.Code.unsupportedPVRFormat](./code/unsupportedpvrformat.md)
  The data in the PVRTC compressed format is in an unsupported format.
- [GLKTextureLoaderError.Code.unsupportedTextureTarget](./code/unsupportedtexturetarget.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [typealias GLKTextureLoaderCallback](../glktextureloadercallback.md)
  Signature for the block executed after an asynchronous texture loading operation completes.
- [Texture Loading Options](../texture-loading-options.md)
  Keys to specify in a `textureOperations` dictionary.
- [Texture Error Handling](../texture-error-handling.md)
  Strings used when handling error messages returned from a texture loading method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloadererror-swift.struct/code)*