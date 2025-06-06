# bindTextureRepresentation(toCGLContext:textureUnit:normalizeCoordinates:)

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Binds the texture to a given texture unit and optionally scales or flips the texture.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func bindTextureRepresentation(toCGLContext cgl_ctx: CGLContextObj!, textureUnit unit: GLenum, normalizeCoordinates flag: Bool)
```

#### Discussion

When you no longer need the texture, call [`unbindTextureRepresentation(fromCGLContext:textureUnit:)`](qcplugininputimagesource/unbindtexturerepresentation(fromcglcontext:textureunit:).md).

## Parameters

- `cgl_ctx`: The CGL context to render to.)
- `unit`: The texture unit to bind to (such as,  )
- `flag`: To apply a texture matrix to scale coordinates (from   to  ) and flip them vertically (if necessary), pass  .

## See Also

- [func lockTextureRepresentation(with: CGColorSpace!, forBounds: NSRect) -> Bool](qcplugininputimagesource/locktexturerepresentation(with:forbounds:).md)
  Creates an OpenGL texture representation from a subregion of the image source using the provided color space.
- [func unlockTextureRepresentation()](qcplugininputimagesource/unlocktexturerepresentation.md)
  Releases the OpenGL texture representation of the image source.
- [func lockBufferRepresentation(withPixelFormat: String!, colorSpace: CGColorSpace!, forBounds: NSRect) -> Bool](qcplugininputimagesource/lockbufferrepresentation(withpixelformat:colorspace:forbounds:).md)
  Creates a memory buffer representation from a subregion of the image source using the provided pixel format and color space.
- [func unbindTextureRepresentation(fromCGLContext: CGLContextObj!, textureUnit: GLenum)](qcplugininputimagesource/unbindtexturerepresentation(fromcglcontext:textureunit:).md)
  Unbinds the texture from a texture unit.
- [func unlockBufferRepresentation()](qcplugininputimagesource/unlockbufferrepresentation.md)
  Releases the memory buffer representation of the image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/bindtexturerepresentation(tocglcontext:textureunit:normalizecoordinates:))*