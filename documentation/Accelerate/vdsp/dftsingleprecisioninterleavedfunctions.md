# vDSP.DFTSinglePrecisionInterleavedFunctions

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
struct DFTSinglePrecisionInterleavedFunctions
```

## Topics

### Type Methods
- [static func destroySetup(OpaquePointer)](./dftsingleprecisioninterleavedfunctions/destroysetup%28_%29.md)
- [static func makeDiscreteFourierTransform(previous: OpaquePointer?, count: Int, direction: vDSP.FourierTransformDirection, transformType: vDSP.DFTTransformType) throws -> OpaquePointer](./dftsingleprecisioninterleavedfunctions/makediscretefouriertransform%28previous,count,direction,transformtype%29.md)

## Relationships

### Conforms To
- [vDSP_DiscreteTransformLifecycleFunctions](../vdsp_discretetransformlifecyclefunctions.md)

## See Also

### Structures
- [struct Biquad](./biquad.md)
  A single- or double-precision biquadratic filter.
- [struct VectorizableDouble](./vectorizabledouble.md)
  A structure that represents a double-precision real value for biquadratic filtering and discrete Fourier transforms.
- [struct VectorizableFloat](./vectorizablefloat.md)
  A structure that represents a single-precision real value for biquadratic filtering and discrete Fourier transforms.
- [struct DFTDoublePrecisionInterleavedFunctions](./dftdoubleprecisioninterleavedfunctions.md)
- [struct DFTDoublePrecisionSplitComplexFunctions](./dftdoubleprecisionsplitcomplexfunctions.md)
- [struct DFTSinglePrecisionSplitComplexFunctions](./dftsingleprecisionsplitcomplexfunctions.md)
- [struct vDSP_SplitComplexDouble](../vdsp_splitcomplexdouble.md)
- [struct vDSP_SplitComplexFloat](../vdsp_splitcomplexfloat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/dftsingleprecisioninterleavedfunctions)*