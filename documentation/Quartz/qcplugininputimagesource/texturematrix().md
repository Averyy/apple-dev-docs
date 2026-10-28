# textureMatrix()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a texture matrix.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Quartz Composer OpenGL API deprecated. (Define QC_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func textureMatrix() -> UnsafePointer<GLfloat>!
```

```objc
- (const GLfloat *) textureMatrix;
```

## Return Value

A 4x4 texture matrix created by scaling (from [`0`, pixels] to [`0`,`1`]) and vertically flipping the texture coordinates;  `NULL` if coordinate  transformation is not required.

## Discussion

This method is provided as a convenience for 2D textures to take care of two issues:

- Coordinates for rectangular textures are expressed in pixels rather than the normalized units used for power-of-two textures. The coordinates need to be normalized before you can process the texture.
- Texture coordinates are typically flipped by OpenGL for processing on the GPU and need to be flipped to the original coordinates.

You can take care of these two issues simply by loading a the matrix returned by this method onto the OpenGL stack. If you are not sure that your texture needs either of these operations, you can load the matrix on the OpenGL stack anyway, as it acts as an identity matrix if it’s not needed.

## See Also

### Getting Texture Information
- [func texturePixelsWide() -> Int](./texturepixelswide%28%29.md)
  Returns the width of the texture representation.
- [func texturePixelsHigh() -> Int](./texturepixelshigh%28%29.md)
  Returns the height of the texture representation.
- [func textureTarget() -> GLenum](./texturetarget%28%29.md)
  Returns the texture target.
- [func textureName() -> GLuint](./texturename%28%29.md)
  Returns the texture name.
- [func textureColorSpace() -> Unmanaged<CGColorSpace>!](./texturecolorspace%28%29.md)
  Returns the color space of the texture representation.
- [func textureFlipped() -> Bool](./textureflipped%28%29.md)
  Returns whether or not the contents of the texture are flipped vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/texturematrix())*