# MTLPixelFormat.x24_stencil8

**Framework**: Metal  
**Kind**: case

A stencil pixel format used to read the stencil value from a texture with a combined 24-bit depth and 8-bit stencil value.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.12+

## Declaration

```swift
case x24_stencil8
```

#### Discussion

You can’t directly read the stencil value of a texture with the [`MTLPixelFormat.depth24Unorm_stencil8`](mtlpixelformat/depth24unorm_stencil8.md) format. To read stencil values from a texture with the [`MTLPixelFormat.depth24Unorm_stencil8`](mtlpixelformat/depth24unorm_stencil8.md) format, create a texture view of that texture using the [`MTLPixelFormat.x24_stencil8`](mtlpixelformat/x24_stencil8.md) format, and sample the texture view instead.

## See Also

- [MTLPixelFormat.depth16Unorm](mtlpixelformat/depth16unorm.md)
  A pixel format for a depth-render target that has a 16-bit normalized, unsigned-integer component.
- [MTLPixelFormat.depth32Float](mtlpixelformat/depth32float.md)
  A pixel format with one 32-bit floating-point component, used for a depth render target.
- [MTLPixelFormat.stencil8](mtlpixelformat/stencil8.md)
  A pixel format with an 8-bit unsigned integer component, used for a stencil render target.
- [MTLPixelFormat.depth24Unorm_stencil8](mtlpixelformat/depth24unorm_stencil8.md)
  A 32-bit combined depth and stencil pixel format with a 24-bit normalized unsigned integer for depth and an 8-bit unsigned integer for stencil.
- [MTLPixelFormat.depth32Float_stencil8](mtlpixelformat/depth32float_stencil8.md)
  A 40-bit combined depth and stencil pixel format with a 32-bit floating-point value for depth and an 8-bit unsigned integer for stencil.
- [MTLPixelFormat.x32_stencil8](mtlpixelformat/x32_stencil8.md)
  A stencil pixel format used to read the stencil value from a texture with a combined 32-bit depth and 8-bit stencil value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/x24_stencil8)*