# vImageCVImageFormat.Format.format422YpCbCr10BiPlanarVideoRange

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

A video-range, two-plane YpCbCr 4:2:2 pixel format with 10 bits per channel.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
case format422YpCbCr10BiPlanarVideoRange
```

#### Discussion

This format defines luminance and chrominance data in the range `64...940`, and stores 10 bits in the most significant bits of 16 bits.

## See Also

### 4:2:2 YpCbCr format constants
- [vImageCVImageFormat.Format.format422YpCbCr8](./format422ypcbcr8.md)
  A component YpCbCr 4:2:2 pixel format with 8 bits per channel and ordered CbYp₀CrYp₁.
- [vImageCVImageFormat.Format.format422YpCbCr8_yuvs](./format422ypcbcr8_yuvs.md)
  A component YpCbCr 4:2:2 pixel format with 8 bits per channel and ordered Yp₀CbYp₁Cr.
- [vImageCVImageFormat.Format.format422YpCbCr8FullRange](./format422ypcbcr8fullrange.md)
  A full-range, component YpCbCr 4:2:2 pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format422YpCbCr10](./format422ypcbcr10.md)
  A component YpCbCr 4:2:2 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format422YpCbCr10BiPlanarFullRange](./format422ypcbcr10biplanarfullrange.md)
  A full-range, two-plane YpCbCr 4:2:2 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format422YpCbCr16](./format422ypcbcr16.md)
  A video-range, two-plane YpCbCr 4:2:2 pixel format with 16 bits per channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/format/format422ypcbcr10biplanarvideorange)*