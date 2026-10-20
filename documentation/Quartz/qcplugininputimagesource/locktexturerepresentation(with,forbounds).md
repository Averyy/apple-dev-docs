# lockTextureRepresentation(with:forBounds:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates an OpenGL texture representation from a subregion of the image source using the provided color space.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Quartz Composer OpenGL API deprecated. (Define QC_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func lockTextureRepresentation(with colorSpace: CGColorSpace!, forBounds bounds: NSRect) -> Bool
```

```objc
- (BOOL) lockTextureRepresentationWithColorSpace:(CGColorSpaceRef) colorSpace forBounds:(NSRect) bounds;
```

#### Return Value

[`true`](../../Swift/true.md) is successful; [`false`](../../Swift/false.md) if texture can’t be created.

#### Discussion

Neither the content of the texture nor its states (for example, the wrap mode) must be modified; you can only draw with it. The texture is valid only in the plug-in context.

## Parameters

- `colorSpace`: A Quartz color space.
- `bounds`: The bounds of the subregion, expressed in pixels. They must be aligned to integer boundaries.

## See Also

### Converting an Image to a Representation
- [func unlockTextureRepresentation()](./unlocktexturerepresentation%28%29.md)
  Releases the OpenGL texture representation of the image source.
- [func lockBufferRepresentation(withPixelFormat: String!, colorSpace: CGColorSpace!, forBounds: NSRect) -> Bool](./lockbufferrepresentation%28withpixelformat,colorspace,forbounds%29.md)
  Creates a memory buffer representation from a subregion of the image source using the provided pixel format and color space.
- [func bindTextureRepresentation(toCGLContext: CGLContextObj!, textureUnit: GLenum, normalizeCoordinates: Bool)](./bindtexturerepresentation%28tocglcontext,textureunit,normalizecoordinates%29.md)
  Binds the texture to a given texture unit and optionally scales or flips the texture.
- [func unbindTextureRepresentation(fromCGLContext: CGLContextObj!, textureUnit: GLenum)](./unbindtexturerepresentation%28fromcglcontext,textureunit%29.md)
  Unbinds the texture from a texture unit.
- [func unlockBufferRepresentation()](./unlockbufferrepresentation%28%29.md)
  Releases the memory buffer representation of the image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/locktexturerepresentation(with:forbounds:))*