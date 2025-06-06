# vImageCVImageFormat.Format.formatDisparityFloat16

**Framework**: Accelerate  
**Kind**: case

A 16-bit disparity pixel format that describes the normalized shift when comparing two images.

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
case formatDisparityFloat16
```

#### Discussion

Units are `1 / meters`, that is, `(pixelShift / (pixelFocalLength * baselineInMeters))`.

## See Also

- [vImageCVImageFormat.Format.formatDisparityFloat32](vimagecvimageformat/format/formatdisparityfloat32.md)
  A 32-bit disparity pixel format that describes the normalized shift when comparing two images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/format/formatdisparityfloat16)*