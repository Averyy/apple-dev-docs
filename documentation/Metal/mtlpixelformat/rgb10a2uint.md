# MTLPixelFormat.rgb10a2Uint

**Framework**: Metal  
**Kind**: case

A 32-bit packed pixel format with four unsigned integer components: 10-bit red, 10-bit green, 10-bit blue, and 2-bit alpha.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case rgb10a2Uint
```

#### Discussion

Pixel data is stored in red, green, blue, and alpha order, from least significant bit to most significant bit.

![Bit layout diagram showing the pixel data storage arrangement of the rgb10a2Uint pixel format. The red component is stored in bits 0 to 9, the green component is stored in bits 10 to 19, the blue component is stored in bits 20 to 29, and the alpha component is stored in bits 30 to 31.](https://docs-assets.developer.apple.com/published/1480c4a8ab5793367e5dc130522ae2d1/media-2952463%402x.png)

## See Also

- [MTLPixelFormat.bgr10a2Unorm](mtlpixelformat/bgr10a2unorm.md)
  A 32-bit packed pixel format with four normalized unsigned integer components: 10-bit blue, 10-bit green, 10-bit red, and 2-bit alpha.
- [MTLPixelFormat.rgb10a2Unorm](mtlpixelformat/rgb10a2unorm.md)
  A 32-bit packed pixel format with four normalized unsigned integer components: 10-bit red, 10-bit green, 10-bit blue, and 2-bit alpha.
- [MTLPixelFormat.rg11b10Float](mtlpixelformat/rg11b10float.md)
  32-bit format with floating-point color components, 11 bits each for red and green and 10 bits for blue.
- [MTLPixelFormat.rgb9e5Float](mtlpixelformat/rgb9e5float.md)
  Packed 32-bit format with floating-point color components: 9 bits each for RGB and 5 bits for an exponent shared by RGB, packed into 32 bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/rgb10a2uint)*