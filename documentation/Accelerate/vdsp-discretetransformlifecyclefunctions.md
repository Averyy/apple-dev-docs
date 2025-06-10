# vDSP_DiscreteTransformLifecycleFunctions

**Framework**: Accelerate  
**Kind**: protocol

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
protocol vDSP_DiscreteTransformLifecycleFunctions
```

## Topics

### Type Methods
- [static func destroySetup(OpaquePointer)](vdsp_discretetransformlifecyclefunctions/destroysetup(_:).md)
- [static func makeDiscreteFourierTransform(previous: OpaquePointer?, count: Int, direction: vDSP.FourierTransformDirection, transformType: vDSP.DFTTransformType) throws -> OpaquePointer](vdsp_discretetransformlifecyclefunctions/makediscretefouriertransform(previous:count:direction:transformtype:).md)

## Relationships

### Conforming Types
- [vDSP.DFTDoublePrecisionInterleavedFunctions](vdsp/dftdoubleprecisioninterleavedfunctions.md)
- [vDSP.DFTDoublePrecisionSplitComplexFunctions](vdsp/dftdoubleprecisionsplitcomplexfunctions.md)
- [vDSP.DFTSinglePrecisionInterleavedFunctions](vdsp/dftsingleprecisioninterleavedfunctions.md)
- [vDSP.DFTSinglePrecisionSplitComplexFunctions](vdsp/dftsingleprecisionsplitcomplexfunctions.md)

## See Also

- [protocol vDSP_DFTFunctions](vdsp_dftfunctions.md)
  A protocol that defines functions for discrete Fourier transform operations.
- [protocol vDSP_FloatingPointDiscreteFourierTransformable](vdsp_floatingpointdiscretefouriertransformable.md)
  Types that support discrete Fourier transform operations.
- [protocol vDSP_FourierTransformFunctions](vdsp_fouriertransformfunctions.md)
  A protocol that defines functions for fast Fourier transform operations.
- [protocol vDSP_FourierTransformable](vdsp_fouriertransformable.md)
  Types that support fast Fourier transform operations.
- [protocol vDSP_DiscreteFourierTransformable](vdsp_discretefouriertransformable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_discretetransformlifecyclefunctions)*