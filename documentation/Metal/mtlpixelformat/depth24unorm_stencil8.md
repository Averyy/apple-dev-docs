# MTLPixelFormat.depth24Unorm_stencil8

**Framework**: Metal  
**Kind**: case

A 32-bit combined depth and stencil pixel format with a 24-bit normalized unsigned integer for depth and an 8-bit unsigned integer for stencil.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.11+

## Declaration

```swift
case depth24Unorm_stencil8
```

#### Discussion

To blit either the depth or stencil information to a Metal buffer, call the [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:)`](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationoffset:destinationbytesperrow:destinationbytesperimage:options:).md) method, specifying the blit options for which part you want to copy. You need to provide space for 4 bytes per pixel in your destination buffer. When Metal copies the data, it sets the bottom 3 bytes of each pixel to the depth data and sets the top byte to arbitrary data. Ignore any data stored in the top byte of each pixel.

## See Also

- [MTLPixelFormat.depth16Unorm](mtlpixelformat/depth16unorm.md)
  A pixel format for a depth-render target that has a 16-bit normalized, unsigned-integer component.
- [MTLPixelFormat.depth32Float](mtlpixelformat/depth32float.md)
  A pixel format with one 32-bit floating-point component, used for a depth render target.
- [MTLPixelFormat.stencil8](mtlpixelformat/stencil8.md)
  A pixel format with an 8-bit unsigned integer component, used for a stencil render target.
- [MTLPixelFormat.depth32Float_stencil8](mtlpixelformat/depth32float_stencil8.md)
  A 40-bit combined depth and stencil pixel format with a 32-bit floating-point value for depth and an 8-bit unsigned integer for stencil.
- [MTLPixelFormat.x32_stencil8](mtlpixelformat/x32_stencil8.md)
  A stencil pixel format used to read the stencil value from a texture with a combined 32-bit depth and 8-bit stencil value.
- [MTLPixelFormat.x24_stencil8](mtlpixelformat/x24_stencil8.md)
  A stencil pixel format used to read the stencil value from a texture with a combined 24-bit depth and 8-bit stencil value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/depth24unorm_stencil8)*