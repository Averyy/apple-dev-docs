# bufferBaseAddress()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the base address of the image buffer.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func bufferBaseAddress() -> UnsafeRawPointer!
```

```objc
- (const void *) bufferBaseAddress;
```

#### Return Value

The base address of the buffer.

#### Discussion

The base address is guaranteed to be aligned on a 16-byte boundary.

## See Also

### Getting Image Buffer Information
- [func imageBounds() -> NSRect](./imagebounds%28%29.md)
  Returns the actual bounds of the image source expressed in pixels and aligned to integer boundaries.
- [func bufferPixelsWide() -> Int](./bufferpixelswide%28%29.md)
  Returns the width of the image buffer representation.
- [func bufferPixelsHigh() -> Int](./bufferpixelshigh%28%29.md)
  Returns the height of the image buffer representation.
- [func bufferPixelFormat() -> String!](./bufferpixelformat%28%29.md)
  Returns the pixel format of the image buffer representation.
- [func bufferColorSpace() -> Unmanaged<CGColorSpace>!](./buffercolorspace%28%29.md)
  Returns the color space of the image buffer representation.
- [func bufferBytesPerRow() -> Int](./bufferbytesperrow%28%29.md)
  Returns the  bytes per row of the buffer representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/bufferbaseaddress())*