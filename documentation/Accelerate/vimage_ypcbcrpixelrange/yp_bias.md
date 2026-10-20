# Yp_bias

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The encoding for `Y' = 0.0` for this video format (varies by bit depth).

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var Yp_bias: Int32
```

```c
int32_t Yp_bias;
```

## See Also

### Pixel Range Properties
- [var CbCr_bias: Int32](./cbcr_bias.md)
  The encoding for `{Cb, Cr} = 0.0` for this video format.
- [var YpRangeMax: Int32](./yprangemax.md)
  The encoding for `Y' = 1.0` for this video format.
- [var CbCrRangeMax: Int32](./cbcrrangemax.md)
  The encoding for `{Cb, Cr} = 0.5` for this video format.
- [var YpMax: Int32](./ypmax.md)
  The encoding for the maximum allowed Y’ value.
- [var YpMin: Int32](./ypmin.md)
  The encoding of the minimum allowed Y’ value.
- [var CbCrMax: Int32](./cbcrmax.md)
  The encoding of the maximum allowed `{Cb, Cr}` value.
- [var CbCrMin: Int32](./cbcrmin.md)
  The encoding of the minimum allowed `{Cb, Cr}` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_ypcbcrpixelrange/yp_bias)*