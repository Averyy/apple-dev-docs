# DSPComplex

**Framework**: Accelerate  
**Kind**: struct

A structure that represents a single-precision complex value.

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
struct DSPComplex
```

## Mentions

- [Controlling vDSP operations with stride](controlling-vdsp-operations-with-stride.md)
- [Performing Fourier transforms on interleaved-complex data](performing-fourier-transforms-on-interleaved-complex-data.md)

#### Overview

Complex data are stored as ordered pairs of floating-point numbers. Because they are stored as ordered pairs, complex vectors require address strides that are multiples of two.

## Topics

### Initializers
- [init()](dspcomplex/init.md)
- [init(real: Float, imag: Float)](dspcomplex/init(real:imag:).md)
### Instance Properties
- [var imag: Float](dspcomplex/imag.md)
  The imaginary part of the value.
- [var real: Float](dspcomplex/real.md)
  The real part of the value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [vDSP_DiscreteFourierTransformable](vdsp_discretefouriertransformable.md)

## See Also

- [typealias vDSP_Length](vdsp_length.md)
  An unsigned-integer value that represents the size of vectors and the indices of elements in vectors.
- [typealias vDSP_Stride](vdsp_stride.md)
  An integer value that represents the differences between indices of elements, including the lengths of strides.
- [typealias COMPLEX_SPLIT](complex_split.md)
- [struct DSPDoubleComplex](dspdoublecomplex.md)
  A structure that represents a double-precision complex value.
- [typealias DOUBLE_COMPLEX_SPLIT](double_complex_split.md)
- [struct DSPSplitComplex](dspsplitcomplex.md)
  A structure that represents a single-precision complex vector with the real and imaginary parts stored in separate arrays.
- [struct DSPDoubleSplitComplex](dspdoublesplitcomplex.md)
  A structure that represents a double-precision complex vector with the real and imaginary parts stored in separate arrays.
- [struct VectorizableDouble](vdsp/vectorizabledouble.md)
  A structure that represents a double-precision real value for biquadratic filtering and discrete Fourier transforms.
- [struct VectorizableFloat](vdsp/vectorizablefloat.md)
  A structure that represents a single-precision real value for biquadratic filtering and discrete Fourier transforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/dspcomplex)*