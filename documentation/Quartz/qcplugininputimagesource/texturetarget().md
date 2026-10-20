# textureTarget()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the texture target.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Quartz Composer OpenGL API deprecated. (Define QC_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func textureTarget() -> GLenum
```

```objc
- (GLenum) textureTarget;
```

#### Return Value

The texture target, either `GL_TEXTURE_2D` or `GL_TEXTURE_RECTANGLE_EXT`.

## See Also

### Getting Texture Information
- [func texturePixelsWide() -> Int](./texturepixelswide%28%29.md)
  Returns the width of the texture representation.
- [func texturePixelsHigh() -> Int](./texturepixelshigh%28%29.md)
  Returns the height of the texture representation.
- [func textureName() -> GLuint](./texturename%28%29.md)
  Returns the texture name.
- [func textureColorSpace() -> Unmanaged<CGColorSpace>!](./texturecolorspace%28%29.md)
  Returns the color space of the texture representation.
- [func textureFlipped() -> Bool](./textureflipped%28%29.md)
  Returns whether or not the contents of the texture are flipped vertically.
- [func textureMatrix() -> UnsafePointer<GLfloat>!](./texturematrix%28%29.md)
  Returns a texture matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/texturetarget())*