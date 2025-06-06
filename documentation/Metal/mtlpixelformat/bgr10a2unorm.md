# MTLPixelFormat.bgr10a2Unorm

**Framework**: Metal  
**Kind**: case

A 32-bit packed pixel format with four normalized unsigned integer components: 10-bit blue, 10-bit green, 10-bit red, and 2-bit alpha.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case bgr10a2Unorm
```

#### Discussion

Pixel data is stored in blue, green, red, and alpha order, from least significant bit to most significant bit.

![Bit layout diagram showing the pixel data storage arrangement of the bgr10a2Unorm pixel format. The blue component is stored in bits 0 to 9, the green component is stored in bits 10 to 19, the red component is stored in bits 20 to 29, and the alpha component is stored in bits 30 to 31.](https://docs-assets.developer.apple.com/published/df2c56f95060e4a4fee5d0139555c97b/media-2952461%402x.png)

On devices with a wide color display, use this format instead of [`MTLPixelFormat.bgra8Unorm`](mtlpixelformat/bgra8unorm.md) to reduce banding artifacts in your displayed content.

## See Also

- [MTLPixelFormat.rgb10a2Unorm](mtlpixelformat/rgb10a2unorm.md)
  A 32-bit packed pixel format with four normalized unsigned integer components: 10-bit red, 10-bit green, 10-bit blue, and 2-bit alpha.
- [MTLPixelFormat.rgb10a2Uint](mtlpixelformat/rgb10a2uint.md)
  A 32-bit packed pixel format with four unsigned integer components: 10-bit red, 10-bit green, 10-bit blue, and 2-bit alpha.
- [MTLPixelFormat.rg11b10Float](mtlpixelformat/rg11b10float.md)
  32-bit format with floating-point color components, 11 bits each for red and green and 10 bits for blue.
- [MTLPixelFormat.rgb9e5Float](mtlpixelformat/rgb9e5float.md)
  Packed 32-bit format with floating-point color components: 9 bits each for RGB and 5 bits for an exponent shared by RGB, packed into 32 bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/bgr10a2unorm)*