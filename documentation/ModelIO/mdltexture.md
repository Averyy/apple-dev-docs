# MDLTexture

**Framework**: Model I/O  
**Kind**: class

A source of texel data to be used in rendering material surface appearances.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLTexture
```

#### Overview

You use the [`MDLTexture`](mdltexture.md) class or one of its subclasses to identify, load, or create texture data, and then associate textures with materials using the [`MDLTextureSampler`](mdltexturesampler.md) and [`MDLMaterialProperty`](mdlmaterialproperty.md) classes. When you load 3D objects from an asset file (in a format that supports texturing) with the [`MDLAsset`](mdlasset.md) class, Model I/O automatically creates texture objects and material objects and associates them with the [`MDLSubmesh`](mdlsubmesh.md) objects in the asset.

## Topics

### Loading Textures from a Bundle
- [convenience init?(named: String)](mdltexture/init(named:).md)
  Loads the texture with the specified filename from the app’s main bundle.
- [convenience init?(named: String, bundle: Bundle?)](mdltexture/init(named:bundle:).md)
  Loads the texture with the specified filename from the specified bundle.
- [convenience init?(cubeWithImagesNamed: [String])](mdltexture/init(cubewithimagesnamed:).md)
  Loads a cube texture from the specified image files in the app’s main bundle.
- [convenience init?(cubeWithImagesNamed: [String], bundle: Bundle?)](mdltexture/init(cubewithimagesnamed:bundle:).md)
  Loads a cube texture from the specified image files in the specified bundle.
### Creating Textures
- [init(data: Data?, topLeftOrigin: Bool, name: String?, dimensions: vector_int2, rowStride: Int, channelCount: Int, channelEncoding: MDLTextureChannelEncoding, isCube: Bool)](mdltexture/init(data:topleftorigin:name:dimensions:rowstride:channelcount:channelencoding:iscube:).md)
  Initializes a texture object with the specified image data and properties.
### Exporting Textures
- [func write(to: URL) -> Bool](mdltexture/write(to:).md)
  Exports the texture data to an image file at the specified URL.
- [func write(to: URL, type: CFString) -> Bool](mdltexture/write(to:type:).md)
  Exports the texture data to an image file at the specified URL, of the specified type.
- [func imageFromTexture() -> Unmanaged<CGImage>?](mdltexture/imagefromtexture.md)
  Exports the texture data as a CoreGraphics image.
### Accessing Texture Data
- [func texelDataWithTopLeftOrigin() -> Data?](mdltexture/texeldatawithtopleftorigin.md)
  Returns the texture’s image data, organized such that its first pixel represents the top-left corner of the image.
- [func texelDataWithBottomLeftOrigin() -> Data?](mdltexture/texeldatawithbottomleftorigin.md)
  Returns the texture’s image data, organized such that its first pixel represents the bottom-left corner of the image.
- [func texelDataWithTopLeftOrigin(atMipLevel: Int, create: Bool) -> Data?](mdltexture/texeldatawithtopleftorigin(atmiplevel:create:).md)
  Returns the texture’s image data for the specified mipmap level, organized such that its first pixel represents the top-left corner of the image.
- [func texelDataWithBottomLeftOrigin(atMipLevel: Int, create: Bool) -> Data?](mdltexture/texeldatawithbottomleftorigin(atmiplevel:create:).md)
  Returns the texture’s image data for the specified mipmap level, organized such that its first pixel represents the bottom-left corner of the image.
### Examining Texture Attributes
- [var dimensions: vector_int2](mdltexture/dimensions.md)
  The width and height, in texels, of the texture image.
- [var rowStride: Int](mdltexture/rowstride.md)
  The number of bytes between the first texel in a row of image data and the first texel in the next row.
- [var channelCount: Int](mdltexture/channelcount.md)
  The number of channels per texel.
- [var channelEncoding: MDLTextureChannelEncoding](mdltexture/channelencoding.md)
  The data format for each channel value per texel.
- [var isCube: Bool](mdltexture/iscube.md)
  A Boolean value that indicates whether the texture is a cube textures.
- [var mipLevelCount: Int](mdltexture/miplevelcount.md)
  The number of mipmap levels contained in the texture image data.
### Creating Irradiance Textures
- [class func irradianceTextureCube(with: MDLTexture, name: String?, dimensions: vector_int2) -> Self](mdltexture/irradiancetexturecube(with:name:dimensions:).md)
  Generates an irradiance texture from the specified reflectance cube texture.
- [class func irradianceTextureCube(with: MDLTexture, name: String?, dimensions: vector_int2, roughness: Float) -> Self](mdltexture/irradiancetexturecube(with:name:dimensions:roughness:).md)
  Generates an irradiance texture from the specified reflectance cube texture, assuming a surface of the specified roughness.
### Constants
- [enum MDLTextureChannelEncoding](mdltexturechannelencoding.md)
  Options for the data size and type of texel channel values, used by the [`channelEncoding`](mdltexture/channelencoding.md) property.
### Initializers
- [init()](mdltexture/init.md)
- [convenience init?(named: String, assetResolver: any MDLAssetResolver)](mdltexture/init(named:assetresolver:).md)
### Instance Properties
- [var hasAlphaValues: Bool](mdltexture/hasalphavalues.md)
### Instance Methods
- [func imageFromTexture(atLevel: Int) -> Unmanaged<CGImage>?](mdltexture/imagefromtexture(atlevel:).md)
- [func write(to: URL, level: Int) -> Bool](mdltexture/write(to:level:).md)
- [func write(to: URL, type: CFString, level: Int) -> Bool](mdltexture/write(to:type:level:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MDLCheckerboardTexture](mdlcheckerboardtexture.md)
- [MDLColorSwatchTexture](mdlcolorswatchtexture.md)
- [MDLNoiseTexture](mdlnoisetexture.md)
- [MDLNormalMapTexture](mdlnormalmaptexture.md)
- [MDLSkyCubeTexture](mdlskycubetexture.md)
- [MDLURLTexture](mdlurltexture.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLNamed](mdlnamed.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLCheckerboardTexture](mdlcheckerboardtexture.md)
  A generator of texel data that creates a checkerboard pattern with two specified colors.
- [class MDLColorSwatchTexture](mdlcolorswatchtexture.md)
  A generator of texel data that creates a gradient between two specified colors.
- [class MDLNoiseTexture](mdlnoisetexture.md)
  A generator of texel data that creates a field of random noise.
- [class MDLNormalMapTexture](mdlnormalmaptexture.md)
  A generator of texel data that computes a normal map from a supplied texture.
- [class MDLSkyCubeTexture](mdlskycubetexture.md)
  A generator of texel data that creates cube textures using a physically realistic simulation of the sunlit sky.
- [class MDLURLTexture](mdlurltexture.md)
  A lightweight reference to a URL from which to load texture data.
- [class MDLTextureFilter](mdltexturefilter.md)
  A description of filtering modes for a renderer to use when sampling from a texture.
- [class MDLTextureSampler](mdltexturesampler.md)
  An object that pairs a source of texture data with sampling parameters to be used in rendering the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture)*