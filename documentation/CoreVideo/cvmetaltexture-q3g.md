# CVMetalTexture

**Framework**: Core Video

A texture-based image buffer that supplies source image data for use with the Metal framework.

#### Overview

A Core Video Metal Texture is a texture-based image buffer that supplies source image data for use with the Metal framework.

## Topics

### Inspecting Textures
- [func CVMetalTextureGetTexture(CVMetalTexture) -> (any MTLTexture)?](cvmetaltexturegettexture(_:).md)
  Returns the Metal texture object for the image buffer.
- [func CVMetalTextureGetCleanTexCoords(CVMetalTexture, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>)](cvmetaltexturegetcleantexcoords(_:_:_:_:_:).md)
  Returns convenient normalized texture coordinates for the part of the image that should be displayed.
- [func CVMetalTextureIsFlipped(CVMetalTexture) -> Bool](cvmetaltextureisflipped(_:).md)
  Returns a Boolean value indicating whether the texture image is vertically flipped.
- [func CVMetalTextureGetTypeID() -> CFTypeID](cvmetaltexturegettypeid().md)
  Returns the Core Foundation type identifier for a CoreVideo Metal texture-based image buffer.
### Data Types
- [typealias CVMetalTexture](cvmetaltexture.md)
  A reference to a CoreVideo Metal texture-based image buffer.

## See Also

- [CVMetalTextureCache](cvmetaltexturecache-q3j.md)
  A cache used to create and manage Metal texture objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetaltexture-q3g)*