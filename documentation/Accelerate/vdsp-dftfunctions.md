# vDSP_DFTFunctions

**Framework**: Accelerate  
**Kind**: protocol

A protocol that defines functions for discrete Fourier transform operations.

**Availability**:
- iOS 13.0+ - Deprecated
- iPadOS 13.0+ - Deprecated
- Mac Catalyst ?+
- macOS 10.15+ - Deprecated
- tvOS 13.0+ - Deprecated
- watchOS 6.0+ - Deprecated
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
protocol vDSP_DFTFunctions
```

## Topics

### Associated Types
- [associatedtype Scalar](vdsp_dftfunctions/scalar.md)
### Type Methods
- [static func destroySetup(OpaquePointer)](vdsp_dftfunctions/destroysetup(_:).md)
- [static func makeDFTSetup<T>(previous: vDSP.DFT<T>?, count: Int, direction: vDSP.FourierTransformDirection, transformType: vDSP.DFTTransformType) -> OpaquePointer?](vdsp_dftfunctions/makedftsetup(previous:count:direction:transformtype:).md)
- [static func transform<U, V>(dftSetup: OpaquePointer, inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V)](vdsp_dftfunctions/transform(dftsetup:inputreal:inputimaginary:outputreal:outputimaginary:).md)

## Relationships

### Conforming Types
- [vDSP.VectorizableDouble](vdsp/vectorizabledouble.md)
- [vDSP.VectorizableFloat](vdsp/vectorizablefloat.md)

## See Also

- [protocol vDSP_FloatingPointDiscreteFourierTransformable](vdsp_floatingpointdiscretefouriertransformable.md)
  Types that support discrete Fourier transform operations.
- [protocol vDSP_FourierTransformFunctions](vdsp_fouriertransformfunctions.md)
  A protocol that defines functions for fast Fourier transform operations.
- [protocol vDSP_FourierTransformable](vdsp_fouriertransformable.md)
  Types that support fast Fourier transform operations.
- [protocol vDSP_DiscreteFourierTransformable](vdsp_discretefouriertransformable.md)
- [protocol vDSP_DiscreteTransformLifecycleFunctions](vdsp_discretetransformlifecyclefunctions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dftfunctions)*