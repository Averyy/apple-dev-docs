# MTLPixelFormat.bgrg422

**Framework**: Metal  
**Kind**: case

A pixel format where the red and green components are subsampled horizontally.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case bgrg422
```

#### Discussion

Two pixels are stored in 32 bits, with shared red and blue values, and unique green values. The component arrangement is the same as it is in UYVY, 2vuy, and k2vuy pixel formats, except there is no implicit format conversion from a YUV to RGB color space. Only 2D non-mipmapped textures can be created with this pixel format, and the width must be a multiple of 2. Neither [`MTLTextureType.type2DArray`](mtltexturetype/type2darray.md) nor [`MTLTextureType.typeCube`](mtltexturetype/typecube.md) textures are supported. This format is a compressed format with a block size of 2x1 in a 32-bit block.

## See Also

- [MTLPixelFormat.gbgr422](mtlpixelformat/gbgr422.md)
  A pixel format where the red and green components are subsampled horizontally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/bgrg422)*