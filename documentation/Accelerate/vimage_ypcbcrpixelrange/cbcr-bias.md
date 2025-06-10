# CbCr_bias

**Framework**: Accelerate  
**Kind**: property

The encoding for `{Cb, Cr} = 0.0` for this video format.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var CbCr_bias: Int32
```

#### Discussion

This value is usually the middle of the range of CbCr, not the low end.

## See Also

- [var Yp_bias: Int32](vimage_ypcbcrpixelrange/yp_bias.md)
  The encoding for `Y' = 0.0` for this video format (varies by bit depth).
- [var YpRangeMax: Int32](vimage_ypcbcrpixelrange/yprangemax.md)
  The encoding for `Y' = 1.0` for this video format.
- [var CbCrRangeMax: Int32](vimage_ypcbcrpixelrange/cbcrrangemax.md)
  The encoding for `{Cb, Cr} = 0.5` for this video format.
- [var YpMax: Int32](vimage_ypcbcrpixelrange/ypmax.md)
  The encoding for the maximum allowed Y’ value.
- [var YpMin: Int32](vimage_ypcbcrpixelrange/ypmin.md)
  The encoding of the minimum allowed Y’ value.
- [var CbCrMax: Int32](vimage_ypcbcrpixelrange/cbcrmax.md)
  The encoding of the maximum allowed `{Cb, Cr}` value.
- [var CbCrMin: Int32](vimage_ypcbcrpixelrange/cbcrmin.md)
  The encoding of the minimum allowed `{Cb, Cr}` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_ypcbcrpixelrange/cbcr_bias)*