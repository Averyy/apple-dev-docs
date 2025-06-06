# bufferBaseAddress()

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns the base address of the image buffer.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func bufferBaseAddress() -> UnsafeRawPointer!
```

#### Return Value

The base address of the buffer.

#### Discussion

The base address is guaranteed to be aligned on a 16-byte boundary.

## See Also

- [func imageBounds() -> NSRect](qcplugininputimagesource/imagebounds.md)
  Returns the actual bounds of the image source expressed in pixels and aligned to integer boundaries.
- [func bufferPixelsWide() -> Int](qcplugininputimagesource/bufferpixelswide.md)
  Returns the width of the image buffer representation.
- [func bufferPixelsHigh() -> Int](qcplugininputimagesource/bufferpixelshigh.md)
  Returns the height of the image buffer representation.
- [func bufferPixelFormat() -> String!](qcplugininputimagesource/bufferpixelformat.md)
  Returns the pixel format of the image buffer representation.
- [func bufferColorSpace() -> Unmanaged<CGColorSpace>!](qcplugininputimagesource/buffercolorspace.md)
  Returns the color space of the image buffer representation.
- [func bufferBytesPerRow() -> Int](qcplugininputimagesource/bufferbytesperrow.md)
  Returns the  bytes per row of the buffer representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/bufferbaseaddress())*