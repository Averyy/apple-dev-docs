# vImageCVImageFormat.Format.format444YpCbCr10BiPlanarVideoRange

**Framework**: Accelerate  
**Kind**: case

A video-range, two-plane YpCbCr 4:4:4 pixel format with 10 bits per channel.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
case format444YpCbCr10BiPlanarVideoRange
```

#### Discussion

This format defines luminance and chrominance data in the range `64...940`, and stores 10 bits in the most significant bits of 16 bits.

## See Also

- [vImageCVImageFormat.Format.format444YpCbCr8](vimagecvimageformat/format/format444ypcbcr8.md)
  A video-range, component YpCbCr 4:4:4 pixel format with 8 bits per channel and ordered CrYpCb.
- [vImageCVImageFormat.Format.format444YpCbCr10](vimagecvimageformat/format/format444ypcbcr10.md)
  A component YpCbCr 4:4:4 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format444YpCbCr10BiPlanarFullRange](vimagecvimageformat/format/format444ypcbcr10biplanarfullrange.md)
  A full-range, two-plane YpCbCr 4:4:4 pixel format with 10 bits per channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/format/format444ypcbcr10biplanarvideorange)*