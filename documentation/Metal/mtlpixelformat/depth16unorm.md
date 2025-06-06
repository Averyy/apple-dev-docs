# MTLPixelFormat.depth16Unorm

**Framework**: Metal  
**Kind**: case

A pixel format for a depth-render target that has a 16-bit normalized, unsigned-integer component.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case depth16Unorm
```

#### Discussion

If you need to apply depth bias, choose a different depth format. Setting a depth bias with this format, such as with [`setDepthBias(_:slopeScale:clamp:)`](mtlrendercommandencoder/setdepthbias(_:slopescale:clamp:).md), generates incorrect results for apps that run on a device with an Apple A8 or earlier GPU.

## See Also

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
- [MTLPixelFormat.x24_stencil8](mtlpixelformat/x24_stencil8.md)
  A stencil pixel format used to read the stencil value from a texture with a combined 24-bit depth and 8-bit stencil value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/depth16unorm)*