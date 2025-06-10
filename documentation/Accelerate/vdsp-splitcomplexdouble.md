# vDSP_SplitComplexDouble

**Framework**: Accelerate  
**Kind**: struct

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
struct vDSP_SplitComplexDouble
```

## Topics

### Type Methods
- [static func destroySetup(OpaquePointer)](vdsp_splitcomplexdouble/destroysetup(_:).md)
  Releases an FFT setup object.
- [static func makeFFTSetup(log2n: vDSP_Length, radix: vDSP.Radix) -> OpaquePointer?](vdsp_splitcomplexdouble/makefftsetup(log2n:radix:).md)
  Returns a setup structure to perform a fast Fourier transform.
- [static func transform(fftSetup: OpaquePointer, log2n: vDSP_Length, source: UnsafePointer<vDSP_SplitComplexDouble.SplitComplex>, destination: UnsafeMutablePointer<vDSP_SplitComplexDouble.SplitComplex>, direction: vDSP.FourierTransformDirection)](vdsp_splitcomplexdouble/transform(fftsetup:log2n:source:destination:direction:).md)
  Performs a 1D fast Fourier transform.
- [static func transform2D(fftSetup: OpaquePointer, width: Int, height: Int, source: UnsafePointer<vDSP_SplitComplexDouble.SplitComplex>, destination: UnsafeMutablePointer<vDSP_SplitComplexDouble.SplitComplex>, direction: vDSP.FourierTransformDirection)](vdsp_splitcomplexdouble/transform2d(fftsetup:width:height:source:destination:direction:).md)
  Performs a 2D fast Fourier transform.

## Relationships

### Conforms To
- [vDSP_FourierTransformFunctions](vdsp_fouriertransformfunctions.md)

## See Also

- [struct Biquad](vdsp/biquad.md)
  A single- or double-precision biquadratic filter.
- [struct VectorizableDouble](vdsp/vectorizabledouble.md)
  A structure that represents a double-precision real value for biquadratic filtering and discrete Fourier transforms.
- [struct VectorizableFloat](vdsp/vectorizablefloat.md)
  A structure that represents a single-precision real value for biquadratic filtering and discrete Fourier transforms.
- [struct DFTDoublePrecisionInterleavedFunctions](vdsp/dftdoubleprecisioninterleavedfunctions.md)
- [struct DFTDoublePrecisionSplitComplexFunctions](vdsp/dftdoubleprecisionsplitcomplexfunctions.md)
- [struct DFTSinglePrecisionInterleavedFunctions](vdsp/dftsingleprecisioninterleavedfunctions.md)
- [struct DFTSinglePrecisionSplitComplexFunctions](vdsp/dftsingleprecisionsplitcomplexfunctions.md)
- [struct vDSP_SplitComplexFloat](vdsp_splitcomplexfloat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_splitcomplexdouble)*