# DSPSplitComplex

**Framework**: Accelerate  
**Kind**: struct

A structure that represents a single-precision complex vector with the real and imaginary parts stored in separate arrays.

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
struct DSPSplitComplex
```

## Mentions

- [Finding the component frequencies in a composite sine wave](finding-the-component-frequencies-in-a-composite-sine-wave.md)
- [Controlling vDSP operations with stride](controlling-vdsp-operations-with-stride.md)
- [Performing Fourier transforms on interleaved-complex data](performing-fourier-transforms-on-interleaved-complex-data.md)
- [Performing Fourier Transforms on Multiple Signals](performing-fourier-transforms-on-multiple-signals.md)

## Topics

### Creating a Split Complex Structure
- [init(realp: UnsafeMutablePointer<Float>, imagp: UnsafeMutablePointer<Float>)](dspsplitcomplex/init(realp:imagp:).md)
  Creates a new split complex structure.
### Inspecting a Split Complex Structure’s Data
- [var imagp: UnsafeMutablePointer<Float>](dspsplitcomplex/imagp.md)
  An array of imaginary parts of the complex numbers.
- [var realp: UnsafeMutablePointer<Float>](dspsplitcomplex/realp.md)
  An array of real parts of the complex numbers.
### Initializers
- [init(fromInputArray: [Float], realParts: inout [Float], imaginaryParts: inout [Float])](dspsplitcomplex/init(frominputarray:realparts:imaginaryparts:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [vDSP_FourierTransformable](vdsp_fouriertransformable.md)

## See Also

- [typealias vDSP_Length](vdsp_length.md)
  An unsigned-integer value that represents the size of vectors and the indices of elements in vectors.
- [typealias vDSP_Stride](vdsp_stride.md)
  An integer value that represents the differences between indices of elements, including the lengths of strides.
- [struct DSPComplex](dspcomplex.md)
  A structure that represents a single-precision complex value.
- [typealias COMPLEX_SPLIT](complex_split.md)
- [struct DSPDoubleComplex](dspdoublecomplex.md)
  A structure that represents a double-precision complex value.
- [typealias DOUBLE_COMPLEX_SPLIT](double_complex_split.md)
- [struct DSPDoubleSplitComplex](dspdoublesplitcomplex.md)
  A structure that represents a double-precision complex vector with the real and imaginary parts stored in separate arrays.
- [struct VectorizableDouble](vdsp/vectorizabledouble.md)
  A structure that represents a double-precision real value for biquadratic filtering and discrete Fourier transforms.
- [struct VectorizableFloat](vdsp/vectorizablefloat.md)
  A structure that represents a single-precision real value for biquadratic filtering and discrete Fourier transforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/dspsplitcomplex)*