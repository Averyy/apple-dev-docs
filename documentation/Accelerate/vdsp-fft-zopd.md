# vDSP_fft_zopD

**Framework**: Accelerate  
**Kind**: func

Computes a forward or inverse out-of-place, double-precision complex FFT.

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
extern void vDSP_fft_zopD(FFTSetupD __Setup, const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, const DSPDoubleSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __Log2N, FFTDirection __Direction);
```

#### Discussion

> 💡 **Tip**:  To learn how the vDSP library scales and arranges the FFT output, see [`Understanding data packing for Fourier transforms`](understanding-data-packing-for-fourier-transforms.md).

## Parameters

- `__Setup`: The FFT setup structure for this transform. The setup’s structure   must be greater than or equal to this function’s  .
- `__A`: A pointer to the input data.
- `__IA`: The stride between the elements in  , set to 1 for best performance.
- `__C`: A pointer to the output data.
- `__IC`: The stride between the elements in  , set to 1 for best performance.
- `__Log2N`: The base 2 exponent of the number of elements to process. For example, to process 1024 elements, specify 10 for parameter  .
- `__Direction`: A flag that specifies the transform direction. Pass   to transform from the time domain to the frequency domain. Pass   to transform from the frequency domain to the time domain.

## See Also

- [vDSP_fft_zop](vdsp_fft_zop.md)
  Computes a forward or inverse out-of-place, single-precision complex FFT.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fft_zopd)*