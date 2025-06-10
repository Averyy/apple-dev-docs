# vDSP_fft_zip

**Framework**: Accelerate  
**Kind**: func

Computes a forward or inverse in-place, single-precision complex FFT.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_fft_zip(FFTSetup __Setup, const DSPSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __Log2N, FFTDirection __Direction);
```

## Mentions

- [Understanding data packing for Fourier transforms](understanding-data-packing-for-fourier-transforms.md)

#### Discussion

> 💡 **Tip**:  To learn how the vDSP library scales and arranges the FFT output, see [`Understanding data packing for Fourier transforms`](understanding-data-packing-for-fourier-transforms.md).

## Parameters

- `__Setup`: The FFT setup structure for this transform. The setup’s structure   must be greater than or equal to this function’s  .
- `__C`: A pointer to the input-output data.
- `__IC`: The stride between the elements in  , set to 1 for best performance.
- `__Log2N`: The base 2 exponent of the number of elements to process. For example, to process 1024 elements, specify   for parameter  .
- `__Direction`: A flag that specifies the transform direction. Pass   to transform from the time domain to the frequency domain. Pass   to transform from the frequency domain to the time domain.

## See Also

- [vDSP_fft_zipD](vdsp_fft_zipd.md)
  Computes a forward or inverse in-place, double-precision complex FFT.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fft_zip)*