# bufferPixelFormat()

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns the pixel format of the image buffer representation.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func bufferPixelFormat() -> String!
```

#### Return Value

A string that specifies the pixel format. The supported formats are ARGB8 (8-bit alpha, red, green, blue), BGRA8 (8-bit blue, green, red, and alpha), RGBAf (floating-point, red, green, blue, alpha), I8 (8-bit intensity), and If (floating-point intensity).

## See Also

- [func imageBounds() -> NSRect](qcplugininputimagesource/imagebounds.md)
  Returns the actual bounds of the image source expressed in pixels and aligned to integer boundaries.
- [func bufferPixelsWide() -> Int](qcplugininputimagesource/bufferpixelswide.md)
  Returns the width of the image buffer representation.
- [func bufferPixelsHigh() -> Int](qcplugininputimagesource/bufferpixelshigh.md)
  Returns the height of the image buffer representation.
- [func bufferColorSpace() -> Unmanaged<CGColorSpace>!](qcplugininputimagesource/buffercolorspace.md)
  Returns the color space of the image buffer representation.
- [func bufferBaseAddress() -> UnsafeRawPointer!](qcplugininputimagesource/bufferbaseaddress.md)
  Returns the base address of the image buffer.
- [func bufferBytesPerRow() -> Int](qcplugininputimagesource/bufferbytesperrow.md)
  Returns the  bytes per row of the buffer representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/bufferpixelformat())*