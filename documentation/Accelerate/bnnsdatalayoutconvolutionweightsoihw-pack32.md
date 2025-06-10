# BNNSDataLayoutConvolutionWeightsOIHW_Pack32

**Framework**: Accelerate  
**Kind**: var

A constant that represents a 4D array of packed convolution weights with 32-output channel packing and 128-byte array address alignment.

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
var BNNSDataLayoutConvolutionWeightsOIHW_Pack32: BNNSDataLayout { get }
```

#### Discussion

The Value `(kx, ky, InChannel, OutChannel)` is at index:

`OutChannelPositionInGroup + kw * 32 + ky * kernel_width * 32 + InChannel * kernel_height * kernel_width * 32 + OutChannelGroup * input_channels * kernel_height * kernel_width * 32`

Where:

- `kernel_width` is the kernel width.
- `kernel_height` is the kernel height.
- `input_channels` is the number of input channels.
- `output_channels` is the number of output channels.
- `OutChannelGroup = OutChannel / 32`.
- `OutChannelPositionInGroup = OutChannel % 32`.
- `kw` is `size[0]` and `kx` is between `0` to `kw-1`.
- `kh` is `size[1]` and `ky` is between `0` to `kh-1`.

## See Also

- [var BNNSDataLayoutConvolutionWeightsOIHW: BNNSDataLayout](bnnsdatalayoutconvolutionweightsoihw.md)
  A constant that represents a 4D array of convolution weights.
- [var BNNSDataLayoutConvolutionWeightsIOHrWr: BNNSDataLayout](bnnsdatalayoutconvolutionweightsiohrwr.md)
  A constant that represents a 4D array of rotated convolution weights.
- [var BNNSDataLayoutConvolutionWeightsOIHrWr: BNNSDataLayout](bnnsdatalayoutconvolutionweightsoihrwr.md)
  A constant that represents a 4D array of rotated convolution weights.
- [var BNNSDataLayout4DFirstMajor: BNNSDataLayout](bnnsdatalayout4dfirstmajor.md)
  A constant that represents a 4D first-major tensor.
- [var BNNSDataLayout4DLastMajor: BNNSDataLayout](bnnsdatalayout4dlastmajor.md)
  A constant that represents a 4D last-major tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdatalayoutconvolutionweightsoihw_pack32)*