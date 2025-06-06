# textureTarget()

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns the texture target.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func textureTarget() -> GLenum
```

#### Return Value

The texture target, either `GL_TEXTURE_2D` or `GL_TEXTURE_RECTANGLE_EXT`.

## See Also

- [func texturePixelsWide() -> Int](qcplugininputimagesource/texturepixelswide.md)
  Returns the width of the texture representation.
- [func texturePixelsHigh() -> Int](qcplugininputimagesource/texturepixelshigh.md)
  Returns the height of the texture representation.
- [func textureName() -> GLuint](qcplugininputimagesource/texturename.md)
  Returns the texture name.
- [func textureColorSpace() -> Unmanaged<CGColorSpace>!](qcplugininputimagesource/texturecolorspace.md)
  Returns the color space of the texture representation.
- [func textureFlipped() -> Bool](qcplugininputimagesource/textureflipped.md)
  Returns whether or not the contents of the texture are flipped vertically.
- [func textureMatrix() -> UnsafePointer<GLfloat>!](qcplugininputimagesource/texturematrix.md)
  Returns a texture matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/texturetarget())*