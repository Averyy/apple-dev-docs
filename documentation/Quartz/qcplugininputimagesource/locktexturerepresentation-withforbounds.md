# lockTextureRepresentation(with:forBounds:)

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Creates an OpenGL texture representation from a subregion of the image source using the provided color space.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func lockTextureRepresentation(with colorSpace: CGColorSpace!, forBounds bounds: NSRect) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) is successful; [`false`](https://developer.apple.com/documentation/Swift/false) if texture can’t be created.

#### Discussion

Neither the content of the texture nor its states (for example, the wrap mode) must be modified; you can only draw with it. The texture is valid only in the plug-in context.

## Parameters

- `colorSpace`: A Quartz color space.
- `bounds`: The bounds of the subregion, expressed in pixels. They must be aligned to integer boundaries.

## See Also

- [func unlockTextureRepresentation()](qcplugininputimagesource/unlocktexturerepresentation.md)
  Releases the OpenGL texture representation of the image source.
- [func lockBufferRepresentation(withPixelFormat: String!, colorSpace: CGColorSpace!, forBounds: NSRect) -> Bool](qcplugininputimagesource/lockbufferrepresentation(withpixelformat:colorspace:forbounds:).md)
  Creates a memory buffer representation from a subregion of the image source using the provided pixel format and color space.
- [func bindTextureRepresentation(toCGLContext: CGLContextObj!, textureUnit: GLenum, normalizeCoordinates: Bool)](qcplugininputimagesource/bindtexturerepresentation(tocglcontext:textureunit:normalizecoordinates:).md)
  Binds the texture to a given texture unit and optionally scales or flips the texture.
- [func unbindTextureRepresentation(fromCGLContext: CGLContextObj!, textureUnit: GLenum)](qcplugininputimagesource/unbindtexturerepresentation(fromcglcontext:textureunit:).md)
  Unbinds the texture from a texture unit.
- [func unlockBufferRepresentation()](qcplugininputimagesource/unlockbufferrepresentation.md)
  Releases the memory buffer representation of the image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/locktexturerepresentation(with:forbounds:))*