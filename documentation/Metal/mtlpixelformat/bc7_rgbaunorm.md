# MTLPixelFormat.bc7_rgbaUnorm

**Framework**: Metal  
**Kind**: case  
**Role**: Case

Compressed format with four normalized unsigned integer components.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```swift
case bc7_rgbaUnorm
```

```c
MTLPixelFormatBC7_RGBAUnorm
```

## See Also

### Compressed BC pixel formats
- [MTLPixelFormat.bc1_rgba](./bc1_rgba.md)
  Compressed format with two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormat.bc1_rgba_srgb](./bc1_rgba_srgb.md)
  Compressed format with two 16-bit color components and one 32-bit descriptor component, with conversion between sRGB and linear space.
- [MTLPixelFormat.bc2_rgba](./bc2_rgba.md)
  Compressed format with two 64-bit chunks. The first chunk contains two 8-bit alpha components and one 48-bit descriptor component. The second chunk contains two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormat.bc2_rgba_srgb](./bc2_rgba_srgb.md)
  Compressed format with two 64-bit chunks, with conversion between sRGB and linear space. The first chunk contains two 8-bit alpha components and one 48-bit descriptor component. The second chunk contains two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormat.bc3_rgba](./bc3_rgba.md)
  Compressed format with two 64-bit chunks. The first chunk contains two 8-bit alpha components and one 48-bit descriptor component. The second chunk contains two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormat.bc3_rgba_srgb](./bc3_rgba_srgb.md)
  Compressed format with two 64-bit chunks, with conversion between sRGB and linear space. The first chunk contains two 8-bit alpha components and one 48-bit descriptor component. The second chunk contains two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormat.bc4_rUnorm](./bc4_runorm.md)
  Compressed format with one normalized unsigned integer component.
- [MTLPixelFormat.bc4_rSnorm](./bc4_rsnorm.md)
  Compressed format with one normalized signed integer component.
- [MTLPixelFormat.bc5_rgUnorm](./bc5_rgunorm.md)
  Compressed format with two normalized unsigned integer components.
- [MTLPixelFormat.bc5_rgSnorm](./bc5_rgsnorm.md)
  Compressed format with two normalized signed integer components.
- [MTLPixelFormat.bc6H_rgbFloat](./bc6h_rgbfloat.md)
  Compressed format with four floating-point components.
- [MTLPixelFormat.bc6H_rgbuFloat](./bc6h_rgbufloat.md)
  Compressed format with four unsigned floating-point components.
- [MTLPixelFormat.bc7_rgbaUnorm_srgb](./bc7_rgbaunorm_srgb.md)
  Compressed format with four normalized unsigned integer components, with conversion between sRGB and linear space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/bc7_rgbaunorm)*