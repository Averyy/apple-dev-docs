# BNNSDataLayoutConvolutionWeightsOIHrWr

**Framework**: Accelerate  
**Kind**: var

A constant that represents a 4D array of rotated convolution weights.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var BNNSDataLayoutConvolutionWeightsOIHrWr: BNNSDataLayout { get }
```

#### Discussion

The value `(kx, ky, InChannel, OutChannel)` is at index:

`(kw - 1 - kx) * stride[0] + (kh - 1 - ky) * stride[1] + OutChannel * stride[2] + InChannel * stride[3]`.

- `size[0]` is the convolution kernel width in pixels.
- `size[1]` is the convolution kernel height in pixels.
- `size[2]` is the number of output channels.
- `size[3]` is the number of input channels.
- `kw` is `size[0]` and `kx` is between `0` to `kw-1`.
- `kh` is `size[1]` and `ky` is between `0` to `kh-1`.

## See Also

- [var BNNSDataLayoutConvolutionWeightsOIHW: BNNSDataLayout](bnnsdatalayoutconvolutionweightsoihw.md)
  A constant that represents a 4D array of convolution weights.
- [var BNNSDataLayoutConvolutionWeightsIOHrWr: BNNSDataLayout](bnnsdatalayoutconvolutionweightsiohrwr.md)
  A constant that represents a 4D array of rotated convolution weights.
- [var BNNSDataLayoutConvolutionWeightsOIHW_Pack32: BNNSDataLayout](bnnsdatalayoutconvolutionweightsoihw_pack32.md)
  A constant that represents a 4D array of packed convolution weights with 32-output channel packing and 128-byte array address alignment.
- [var BNNSDataLayout4DFirstMajor: BNNSDataLayout](bnnsdatalayout4dfirstmajor.md)
  A constant that represents a 4D first-major tensor.
- [var BNNSDataLayout4DLastMajor: BNNSDataLayout](bnnsdatalayout4dlastmajor.md)
  A constant that represents a 4D last-major tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdatalayoutconvolutionweightsoihrwr)*