# bufferPixelsHigh()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the height of the image buffer representation.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func bufferPixelsHigh() -> Int
```

```objc
- (NSUInteger) bufferPixelsHigh;
```

#### Return Value

The height, expressed in pixels.

## See Also

### Getting Image Buffer Information
- [func imageBounds() -> NSRect](./imagebounds%28%29.md)
  Returns the actual bounds of the image source expressed in pixels and aligned to integer boundaries.
- [func bufferPixelsWide() -> Int](./bufferpixelswide%28%29.md)
  Returns the width of the image buffer representation.
- [func bufferPixelFormat() -> String!](./bufferpixelformat%28%29.md)
  Returns the pixel format of the image buffer representation.
- [func bufferColorSpace() -> Unmanaged<CGColorSpace>!](./buffercolorspace%28%29.md)
  Returns the color space of the image buffer representation.
- [func bufferBaseAddress() -> UnsafeRawPointer!](./bufferbaseaddress%28%29.md)
  Returns the base address of the image buffer.
- [func bufferBytesPerRow() -> Int](./bufferbytesperrow%28%29.md)
  Returns the  bytes per row of the buffer representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/bufferpixelshigh())*