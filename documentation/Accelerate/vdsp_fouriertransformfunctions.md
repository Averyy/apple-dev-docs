# vDSP_FourierTransformFunctions

**Framework**: Accelerate  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines functions for fast Fourier transform operations.

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
protocol vDSP_FourierTransformFunctions
```

## Topics

### Associated Types
- [associatedtype SplitComplex](./vdsp_fouriertransformfunctions/splitcomplex.md)
### Type Methods
- [static func destroySetup(OpaquePointer)](./vdsp_fouriertransformfunctions/destroysetup%28_%29.md)
- [static func makeFFTSetup(log2n: vDSP_Length, radix: vDSP.Radix) -> OpaquePointer?](./vdsp_fouriertransformfunctions/makefftsetup%28log2n,radix%29.md)
- [static func transform(fftSetup: OpaquePointer, log2n: vDSP_Length, source: UnsafePointer<Self.SplitComplex>, destination: UnsafeMutablePointer<Self.SplitComplex>, direction: vDSP.FourierTransformDirection)](./vdsp_fouriertransformfunctions/transform%28fftsetup,log2n,source,destination,direction%29.md)
- [static func transform2D(fftSetup: OpaquePointer, width: Int, height: Int, source: UnsafePointer<Self.SplitComplex>, destination: UnsafeMutablePointer<Self.SplitComplex>, direction: vDSP.FourierTransformDirection)](./vdsp_fouriertransformfunctions/transform2d%28fftsetup,width,height,source,destination,direction%29.md)

## Relationships

### Conforming Types
- [vDSP_SplitComplexDouble](./vdsp_splitcomplexdouble.md)
- [vDSP_SplitComplexFloat](./vdsp_splitcomplexfloat.md)

## See Also

### Fourier Transform
- [protocol vDSP_DFTFunctions](./vdsp_dftfunctions.md)
  A protocol that defines functions for discrete Fourier transform operations.
- [protocol vDSP_FloatingPointDiscreteFourierTransformable](./vdsp_floatingpointdiscretefouriertransformable.md)
  Types that support discrete Fourier transform operations.
- [protocol vDSP_FourierTransformable](./vdsp_fouriertransformable.md)
  Types that support fast Fourier transform operations.
- [protocol vDSP_DiscreteFourierTransformable](./vdsp_discretefouriertransformable.md)
- [protocol vDSP_DiscreteTransformLifecycleFunctions](./vdsp_discretetransformlifecyclefunctions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fouriertransformfunctions)*