# textureColorSpace()

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns the color space of the texture representation.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func textureColorSpace() -> Unmanaged<CGColorSpace>!
```

#### Return Value

The color space of the texture.

## See Also

- [func texturePixelsWide() -> Int](qcplugininputimagesource/texturepixelswide.md)
  Returns the width of the texture representation.
- [func texturePixelsHigh() -> Int](qcplugininputimagesource/texturepixelshigh.md)
  Returns the height of the texture representation.
- [func textureTarget() -> GLenum](qcplugininputimagesource/texturetarget.md)
  Returns the texture target.
- [func textureName() -> GLuint](qcplugininputimagesource/texturename.md)
  Returns the texture name.
- [func textureFlipped() -> Bool](qcplugininputimagesource/textureflipped.md)
  Returns whether or not the contents of the texture are flipped vertically.
- [func textureMatrix() -> UnsafePointer<GLfloat>!](qcplugininputimagesource/texturematrix.md)
  Returns a texture matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/texturecolorspace())*