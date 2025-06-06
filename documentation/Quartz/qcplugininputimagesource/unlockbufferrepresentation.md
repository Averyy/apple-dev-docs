# unlockBufferRepresentation()

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Releases the memory buffer representation of the image source.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func unlockBufferRepresentation()
```

## See Also

- [func lockTextureRepresentation(with: CGColorSpace!, forBounds: NSRect) -> Bool](qcplugininputimagesource/locktexturerepresentation(with:forbounds:).md)
  Creates an OpenGL texture representation from a subregion of the image source using the provided color space.
- [func unlockTextureRepresentation()](qcplugininputimagesource/unlocktexturerepresentation.md)
  Releases the OpenGL texture representation of the image source.
- [func lockBufferRepresentation(withPixelFormat: String!, colorSpace: CGColorSpace!, forBounds: NSRect) -> Bool](qcplugininputimagesource/lockbufferrepresentation(withpixelformat:colorspace:forbounds:).md)
  Creates a memory buffer representation from a subregion of the image source using the provided pixel format and color space.
- [func bindTextureRepresentation(toCGLContext: CGLContextObj!, textureUnit: GLenum, normalizeCoordinates: Bool)](qcplugininputimagesource/bindtexturerepresentation(tocglcontext:textureunit:normalizecoordinates:).md)
  Binds the texture to a given texture unit and optionally scales or flips the texture.
- [func unbindTextureRepresentation(fromCGLContext: CGLContextObj!, textureUnit: GLenum)](qcplugininputimagesource/unbindtexturerepresentation(fromcglcontext:textureunit:).md)
  Unbinds the texture from a texture unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/unlockbufferrepresentation())*