# vDSP_FourierTransformFunctions

**Framework**: Accelerate  
**Kind**: protocol

A protocol that defines functions for fast Fourier transform operations.

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
protocol vDSP_FourierTransformFunctions
```

## Topics

### Associated Types
- [associatedtype SplitComplex](vdsp_fouriertransformfunctions/splitcomplex.md)
### Type Methods
- [static func destroySetup(OpaquePointer)](vdsp_fouriertransformfunctions/destroysetup(_:).md)
- [static func makeFFTSetup(log2n: vDSP_Length, radix: vDSP.Radix) -> OpaquePointer?](vdsp_fouriertransformfunctions/makefftsetup(log2n:radix:).md)
- [static func transform(fftSetup: OpaquePointer, log2n: vDSP_Length, source: UnsafePointer<Self.SplitComplex>, destination: UnsafeMutablePointer<Self.SplitComplex>, direction: vDSP.FourierTransformDirection)](vdsp_fouriertransformfunctions/transform(fftsetup:log2n:source:destination:direction:).md)
- [static func transform2D(fftSetup: OpaquePointer, width: Int, height: Int, source: UnsafePointer<Self.SplitComplex>, destination: UnsafeMutablePointer<Self.SplitComplex>, direction: vDSP.FourierTransformDirection)](vdsp_fouriertransformfunctions/transform2d(fftsetup:width:height:source:destination:direction:).md)

## Relationships

### Conforming Types
- [vDSP_SplitComplexDouble](vdsp_splitcomplexdouble.md)
- [vDSP_SplitComplexFloat](vdsp_splitcomplexfloat.md)

## See Also

- [protocol vDSP_DFTFunctions](vdsp_dftfunctions.md)
  A protocol that defines functions for discrete Fourier transform operations.
- [protocol vDSP_FloatingPointDiscreteFourierTransformable](vdsp_floatingpointdiscretefouriertransformable.md)
  Types that support discrete Fourier transform operations.
- [protocol vDSP_FourierTransformable](vdsp_fouriertransformable.md)
  Types that support fast Fourier transform operations.
- [protocol vDSP_DiscreteFourierTransformable](vdsp_discretefouriertransformable.md)
- [protocol vDSP_DiscreteTransformLifecycleFunctions](vdsp_discretetransformlifecyclefunctions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fouriertransformfunctions)*