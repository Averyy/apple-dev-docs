# vDSP.DFTSinglePrecisionInterleavedFunctions

**Framework**: Accelerate  
**Kind**: struct

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
struct DFTSinglePrecisionInterleavedFunctions
```

## Topics

### Type Methods
- [static func destroySetup(OpaquePointer)](vdsp/dftsingleprecisioninterleavedfunctions/destroysetup(_:).md)
- [static func makeDiscreteFourierTransform(previous: OpaquePointer?, count: Int, direction: vDSP.FourierTransformDirection, transformType: vDSP.DFTTransformType) throws -> OpaquePointer](vdsp/dftsingleprecisioninterleavedfunctions/makediscretefouriertransform(previous:count:direction:transformtype:).md)

## Relationships

### Conforms To
- [vDSP_DiscreteTransformLifecycleFunctions](vdsp_discretetransformlifecyclefunctions.md)

## See Also

- [struct Biquad](vdsp/biquad.md)
  A single- or double-precision biquadratic filter.
- [struct VectorizableDouble](vdsp/vectorizabledouble.md)
  A structure that represents a double-precision real value for biquadratic filtering and discrete Fourier transforms.
- [struct VectorizableFloat](vdsp/vectorizablefloat.md)
  A structure that represents a single-precision real value for biquadratic filtering and discrete Fourier transforms.
- [struct DFTDoublePrecisionInterleavedFunctions](vdsp/dftdoubleprecisioninterleavedfunctions.md)
- [struct DFTDoublePrecisionSplitComplexFunctions](vdsp/dftdoubleprecisionsplitcomplexfunctions.md)
- [struct DFTSinglePrecisionSplitComplexFunctions](vdsp/dftsingleprecisionsplitcomplexfunctions.md)
- [struct vDSP_SplitComplexDouble](vdsp_splitcomplexdouble.md)
- [struct vDSP_SplitComplexFloat](vdsp_splitcomplexfloat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/dftsingleprecisioninterleavedfunctions)*