# vDSP_SplitComplexFloat

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
struct vDSP_SplitComplexFloat
```

## Topics

### Type Methods
- [static func destroySetup(OpaquePointer)](./vdsp_splitcomplexfloat/destroysetup%28_%29.md)
  Releases an FFT setup object.
- [static func makeFFTSetup(log2n: vDSP_Length, radix: vDSP.Radix) -> OpaquePointer?](./vdsp_splitcomplexfloat/makefftsetup%28log2n,radix%29.md)
  Returns a setup structure to perform a fast Fourier transform.
- [static func transform(fftSetup: OpaquePointer, log2n: vDSP_Length, source: UnsafePointer<vDSP_SplitComplexFloat.SplitComplex>, destination: UnsafeMutablePointer<vDSP_SplitComplexFloat.SplitComplex>, direction: vDSP.FourierTransformDirection)](./vdsp_splitcomplexfloat/transform%28fftsetup,log2n,source,destination,direction%29.md)
  Performs a 1D fast Fourier transform.
- [static func transform2D(fftSetup: OpaquePointer, width: Int, height: Int, source: UnsafePointer<vDSP_SplitComplexFloat.SplitComplex>, destination: UnsafeMutablePointer<vDSP_SplitComplexFloat.SplitComplex>, direction: vDSP.FourierTransformDirection)](./vdsp_splitcomplexfloat/transform2d%28fftsetup,width,height,source,destination,direction%29.md)
  Performs a 2D fast Fourier transform.

## Relationships

### Conforms To
- [vDSP_FourierTransformFunctions](./vdsp_fouriertransformfunctions.md)

## See Also

### Structures
- [struct Biquad](./vdsp/biquad.md)
  A single- or double-precision biquadratic filter.
- [struct VectorizableDouble](./vdsp/vectorizabledouble.md)
  A structure that represents a double-precision real value for biquadratic filtering and discrete Fourier transforms.
- [struct VectorizableFloat](./vdsp/vectorizablefloat.md)
  A structure that represents a single-precision real value for biquadratic filtering and discrete Fourier transforms.
- [struct DFTDoublePrecisionInterleavedFunctions](./vdsp/dftdoubleprecisioninterleavedfunctions.md)
- [struct DFTDoublePrecisionSplitComplexFunctions](./vdsp/dftdoubleprecisionsplitcomplexfunctions.md)
- [struct DFTSinglePrecisionInterleavedFunctions](./vdsp/dftsingleprecisioninterleavedfunctions.md)
- [struct DFTSinglePrecisionSplitComplexFunctions](./vdsp/dftsingleprecisionsplitcomplexfunctions.md)
- [struct vDSP_SplitComplexDouble](./vdsp_splitcomplexdouble.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_splitcomplexfloat)*