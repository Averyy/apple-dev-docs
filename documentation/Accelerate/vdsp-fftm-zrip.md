# vDSP_fftm_zrip

**Framework**: Accelerate  
**Kind**: func

Computes a forward or inverse in-place, single-precision real FFT on multiple signals.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_fftm_zrip(FFTSetup __Setup, const DSPSplitComplex * __C, vDSP_Stride __IC, vDSP_Stride __IM, vDSP_Length __Log2N, vDSP_Length __M, FFTDirection __Direction);
```

## Mentions

- [Performing Fourier Transforms on Multiple Signals](performing-fourier-transforms-on-multiple-signals.md)

#### Discussion

The function performs discrete Fourier transforms on multiple signals using a single call. They will work for input signals of 4 points or greater. Each of the input signals processed by a given call must have the same length and address stride.

The functions compute in-place real discrete Fourier transforms of the input signals, either from the time domain to the frequency domain (forward) or from the frequency domain to the time domain (inverse).

> 💡 **Tip**:  To learn how the vDSP library scales and arranges the FFT output, see [`Understanding data packing for Fourier transforms`](understanding-data-packing-for-fourier-transforms.md).

## Parameters

- `__Setup`: The FFT setup structure for this transform. The setup’s structure   must be greater than or equal to this function’s  .
- `__C`: A pointer to the input-output data.
- `__IC`: The stride between the elements in  , set to 1 for best performance.
- `__IM`: The increment, in complex elements, between input signals. This parameter also specifies the length of each input signal in split-complex format.
- `__Log2N`: The base 2 exponent of the number of elements to process in a single input signal. For example, to process 512 elements, specify 9 for parameter  .
- `__M`: The number of input signals.
- `__Direction`: A flag that specifies the transform direction. Pass   to transform from the time domain to the frequency domain. Pass   to transform from the frequency domain to the time domain.

## See Also

- [vDSP_fftm_zripD](vdsp_fftm_zripd.md)
  Computes a forward or inverse in-place, double-precision real FFT on multiple signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fftm_zrip)*