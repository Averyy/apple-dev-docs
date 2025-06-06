# vImageCVImageFormat.Format.formatDisparityFloat32

**Framework**: Accelerate  
**Kind**: case

A 32-bit disparity pixel format that describes the normalized shift when comparing two images.

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
case formatDisparityFloat32
```

#### Discussion

Units are `1 / meters`, that is, `(pixelShift / (pixelFocalLength * baselineInMeters))`.

## See Also

- [vImageCVImageFormat.Format.formatDisparityFloat16](vimagecvimageformat/format/formatdisparityfloat16.md)
  A 16-bit disparity pixel format that describes the normalized shift when comparing two images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/format/formatdisparityfloat32)*