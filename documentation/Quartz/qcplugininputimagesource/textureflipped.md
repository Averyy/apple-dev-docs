# textureFlipped()

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns whether or not the contents of the texture are flipped vertically.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func textureFlipped() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the contents of the texture are flipped (upside-down); [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## See Also

- [func texturePixelsWide() -> Int](qcplugininputimagesource/texturepixelswide.md)
  Returns the width of the texture representation.
- [func texturePixelsHigh() -> Int](qcplugininputimagesource/texturepixelshigh.md)
  Returns the height of the texture representation.
- [func textureTarget() -> GLenum](qcplugininputimagesource/texturetarget.md)
  Returns the texture target.
- [func textureName() -> GLuint](qcplugininputimagesource/texturename.md)
  Returns the texture name.
- [func textureColorSpace() -> Unmanaged<CGColorSpace>!](qcplugininputimagesource/texturecolorspace.md)
  Returns the color space of the texture representation.
- [func textureMatrix() -> UnsafePointer<GLfloat>!](qcplugininputimagesource/texturematrix.md)
  Returns a texture matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/textureflipped())*