# lockBufferRepresentation(withPixelFormat:colorSpace:forBounds:)

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Creates a memory buffer representation from a subregion of the image source using the provided pixel format and color space.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func lockBufferRepresentation(withPixelFormat format: String!, colorSpace: CGColorSpace!, forBounds bounds: NSRect) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The content of the buffer is read-only. You should not attempt to modify it.

## Parameters

- `format`: A pixel format that is compatible with the color space.
- `colorSpace`: A Quartz color space that is compatible with the pixel format.
- `bounds`: The bounds of the subregion, expressed as pixels, and aligned to integer boundaries.

## See Also

- [func lockTextureRepresentation(with: CGColorSpace!, forBounds: NSRect) -> Bool](qcplugininputimagesource/locktexturerepresentation(with:forbounds:).md)
  Creates an OpenGL texture representation from a subregion of the image source using the provided color space.
- [func unlockTextureRepresentation()](qcplugininputimagesource/unlocktexturerepresentation.md)
  Releases the OpenGL texture representation of the image source.
- [func bindTextureRepresentation(toCGLContext: CGLContextObj!, textureUnit: GLenum, normalizeCoordinates: Bool)](qcplugininputimagesource/bindtexturerepresentation(tocglcontext:textureunit:normalizecoordinates:).md)
  Binds the texture to a given texture unit and optionally scales or flips the texture.
- [func unbindTextureRepresentation(fromCGLContext: CGLContextObj!, textureUnit: GLenum)](qcplugininputimagesource/unbindtexturerepresentation(fromcglcontext:textureunit:).md)
  Unbinds the texture from a texture unit.
- [func unlockBufferRepresentation()](qcplugininputimagesource/unlockbufferrepresentation.md)
  Releases the memory buffer representation of the image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/lockbufferrepresentation(withpixelformat:colorspace:forbounds:))*