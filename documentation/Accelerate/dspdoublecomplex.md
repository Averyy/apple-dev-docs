# DSPDoubleComplex

**Framework**: Accelerate  
**Kind**: struct

A structure that represents a double-precision complex value.

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
struct DSPDoubleComplex
```

## Mentions

- [Performing Fourier transforms on interleaved-complex data](performing-fourier-transforms-on-interleaved-complex-data.md)

#### Overview

Double complex data are stored as ordered pairs of double-precision floating-point numbers. Because they are stored as ordered pairs, complex vectors require address strides that are multiples of two.

## Topics

### Initializers
- [init()](dspdoublecomplex/init.md)
- [init(real: Double, imag: Double)](dspdoublecomplex/init(real:imag:).md)
### Instance Properties
- [var imag: Double](dspdoublecomplex/imag.md)
  The imaginary part of the value.
- [var real: Double](dspdoublecomplex/real.md)
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
- [struct DSPComplex](dspcomplex.md)
  A structure that represents a single-precision complex value.
- [typealias COMPLEX_SPLIT](complex_split.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/dspdoublecomplex)*