# unlockBufferRepresentation()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Releases the memory buffer representation of the image source.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func unlockBufferRepresentation()
```

```objc
- (void) unlockBufferRepresentation;
```

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
- [func unbindTextureRepresentation(fromCGLContext: CGLContextObj!, textureUnit: GLenum)](./unbindtexturerepresentation%28fromcglcontext,textureunit%29.md)
  Unbinds the texture from a texture unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/unlockbufferrepresentation())*