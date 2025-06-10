# MTLPixelFormat.rg11b10Float

**Framework**: Metal  
**Kind**: case

32-bit format with floating-point color components, 11 bits each for red and green and 10 bits for blue.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case rg11b10Float
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Discussion

The components have no sign bit. The 10-bit float has 5 bits of mantissa and 5 bits of exponent. The 11-bit floats have 6 bits of mantissa and 5 bits of exponent.

## See Also

- [MTLPixelFormat.bgr10a2Unorm](mtlpixelformat/bgr10a2unorm.md)
  A 32-bit packed pixel format with four normalized unsigned integer components: 10-bit blue, 10-bit green, 10-bit red, and 2-bit alpha.
- [MTLPixelFormat.rgb10a2Unorm](mtlpixelformat/rgb10a2unorm.md)
  A 32-bit packed pixel format with four normalized unsigned integer components: 10-bit red, 10-bit green, 10-bit blue, and 2-bit alpha.
- [MTLPixelFormat.rgb10a2Uint](mtlpixelformat/rgb10a2uint.md)
  A 32-bit packed pixel format with four unsigned integer components: 10-bit red, 10-bit green, 10-bit blue, and 2-bit alpha.
- [MTLPixelFormat.rgb9e5Float](mtlpixelformat/rgb9e5float.md)
  Packed 32-bit format with floating-point color components: 9 bits each for RGB and 5 bits for an exponent shared by RGB, packed into 32 bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/rg11b10float)*