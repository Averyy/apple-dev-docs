# BNNSDataLayout4DFirstMajor

**Framework**: Accelerate  
**Kind**: var

A constant that represents a 4D first-major tensor.

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
var BNNSDataLayout4DFirstMajor: BNNSDataLayout { get }
```

#### Discussion

The value `(i, j, k, l)` is at index:

`l * stride[0] + k * stride[1] + j * stride[2] + i * stride[3]`

- `size[0]` is the size of the first dimension (`i`).
- `size[1]` is the size of the second dimension (`j`).
- `size[2]` is the size of the third dimension (`k`).
- `size[3]` is the size of the fourth dimension (`l`).

## See Also

- [var BNNSDataLayoutConvolutionWeightsOIHW: BNNSDataLayout](bnnsdatalayoutconvolutionweightsoihw.md)
  A constant that represents a 4D array of convolution weights.
- [var BNNSDataLayoutConvolutionWeightsIOHrWr: BNNSDataLayout](bnnsdatalayoutconvolutionweightsiohrwr.md)
  A constant that represents a 4D array of rotated convolution weights.
- [var BNNSDataLayoutConvolutionWeightsOIHrWr: BNNSDataLayout](bnnsdatalayoutconvolutionweightsoihrwr.md)
  A constant that represents a 4D array of rotated convolution weights.
- [var BNNSDataLayoutConvolutionWeightsOIHW_Pack32: BNNSDataLayout](bnnsdatalayoutconvolutionweightsoihw_pack32.md)
  A constant that represents a 4D array of packed convolution weights with 32-output channel packing and 128-byte array address alignment.
- [var BNNSDataLayout4DLastMajor: BNNSDataLayout](bnnsdatalayout4dlastmajor.md)
  A constant that represents a 4D last-major tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdatalayout4dfirstmajor)*