# vDSP_zaspecD

**Framework**: Accelerate  
**Kind**: func

Computes the autospectrum of a complex double-precision vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_zaspecD(const DSPDoubleSplitComplex * __A, double * __C, vDSP_Length __N);
```

#### Discussion

This function computes the autospectrum of the complex input vector and adds the result to the existing real values in the output vector. The function returns the product of each input element and its complex conjugate. Each element-wise product is a real value that’s the sum of the squares of the real and imaginary parts.

Because the function adds its result to the existing values in the output vector, the output vector must be initialized with known values or contain valid data from a previous operation.

The input and output vectors must have a stride of `1`.

## Parameters

- `__A`: A double-precision vector that contains the complex input values.
- `__C`: A double-precision vector that accumulates the real output values.
- `__N`: The number of elements.

## See Also

- [Finding the component frequencies in a composite sine wave](finding-the-component-frequencies-in-a-composite-sine-wave.md)
  Use 1D fast Fourier transform to compute the frequency components of a signal.
- [vDSP_zaspec](vdsp_zaspec.md)
  Computes the autospectrum of a complex single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zaspecd)*