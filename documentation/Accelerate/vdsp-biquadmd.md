# vDSP_biquadmD

**Framework**: Accelerate  
**Kind**: func

Applies a double-precision multichannel biquadratic IIR filter.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_biquadmD(vDSP_biquadm_SetupD __Setup, const double * * __X, vDSP_Stride __IX, double * * __Y, vDSP_Stride __IY, vDSP_Length __N);
```

#### Discussion

For each channel, this function applies a cascaded biquad filter to the input values specified by the channel’s pointer in `X`, and places the results in the array specified by the corresponding pointer in `Y`.

This function supports interleaved channel data. In this case, define the stride as the number of channels, and the pointers to consecutive channels as consecutive locations in memory.

> **Note**:  This function achieves the best performance and energy efficiency with non-interleaved data and a stride of 1, or interleaved data and a stride equal to the number of channels.

## Parameters

- `__Setup`: The biquadratic filter setup object that defines the filter the function applies.
- `__X`: An array of pointers, each of which specifies an array of input data for a single channel.
- `__IX`: The stride for the input.
- `__Y`: On output, an array of pointers, each of which contains the output data for a single channel.
- `__IY`: The stride for the output.
- `__N`: The number of elements to filter.

## See Also

- [vDSP_biquadm](vdsp_biquadm.md)
  Applies a single-precision multichannel biquadratic IIR filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquadmd)*