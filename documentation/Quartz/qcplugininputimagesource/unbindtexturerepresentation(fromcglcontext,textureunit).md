# unbindTextureRepresentation(fromCGLContext:textureUnit:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Unbinds the texture from a texture unit.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Quartz Composer OpenGL API deprecated. (Define QC_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func unbindTextureRepresentation(fromCGLContext cgl_ctx: CGLContextObj!, textureUnit unit: GLenum)
```

```objc
- (void) unbindTextureRepresentationFromCGLContext:(CGLContextObj) cgl_ctx textureUnit:(GLenum) unit;
```

## Parameters

- `cgl_ctx`: A CGL context.)
- `unit`: The texture unit to unbind from (such as, `GL_TEXTURE0`)

## See Also

### Converting an Image to a Representation
- [func lockTextureRepresentation(with: CGColorSpace!, forBounds: NSRect) -> Bool](./locktexturerepresentation%28with,forbounds%29.md)
  Creates an OpenGL texture representation from a subregion of the image source using the provided color space.
- [func unlockTextureRepresentation()](./unlocktexturerepresentation%28%29.md)
  Releases the OpenGL texture representation of the image source.
- [func lockBufferRepresentation(withPixelFormat: String!, colorSpace: CGColorSpace!, forBounds: NSRect) -> Bool](./lockbufferrepresentation%28withpixelformat,colorspace,forbounds%29.md)
  Creates a memory buffer representation from a subregion of the image source using the provided pixel format and color space.
- [func bindTextureRepresentation(toCGLContext: CGLContextObj!, textureUnit: GLenum, normalizeCoordinates: Bool)](./bindtexturerepresentation%28tocglcontext,textureunit,normalizecoordinates%29.md)
  Binds the texture to a given texture unit and optionally scales or flips the texture.
- [func unlockBufferRepresentation()](./unlockbufferrepresentation%28%29.md)
  Releases the memory buffer representation of the image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/unbindtexturerepresentation(fromcglcontext:textureunit:))*