# MPSGraphReducedPrecisionFastMath

**Framework**: Metal Performance Shaders Graph  
**Kind**: struct

MPSGraph could use these reduced precision paths to deliver faster math, but it is not guaranteed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct MPSGraphReducedPrecisionFastMath
```

## Topics

### Initializers
- [init(rawValue: UInt)](mpsgraphreducedprecisionfastmath/init(rawvalue:).md)
### Type Properties
- [static var allowConvertingOperandsFromFP32ToFP19: MPSGraphReducedPrecisionFastMath](mpsgraphreducedprecisionfastmath/allowconvertingoperandsfromfp32tofp19.md)
  Allow conversion of operands to FP19 or TF32 from FP32 when needed by dropping 13 mantissa bits.
- [static var allowFP16Conv2DWinogradTransformIntermediate: MPSGraphReducedPrecisionFastMath](mpsgraphreducedprecisionfastmath/allowfp16conv2dwinogradtransformintermediate.md)
  Execute winograd transform intermediate as FP16.
- [static var allowFP16Intermediates: MPSGraphReducedPrecisionFastMath](mpsgraphreducedprecisionfastmath/allowfp16intermediates.md)
  Curated list allowing intermediates for multi-pass GPU kernels to be FP16.
- [static var none: MPSGraphReducedPrecisionFastMath](mpsgraphreducedprecisionfastmath/none.md)
  Full precision math with maximum accuracy.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphreducedprecisionfastmath)*