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
- [static var allowFP16Conv2DWinogradTransformIntermediate: MPSGraphReducedPrecisionFastMath](mpsgraphreducedprecisionfastmath/allowfp16conv2dwinogradtransformintermediate.md)
  Execute winograd transform intermediate as FP16.
- [static var allowFP16Intermediates: MPSGraphReducedPrecisionFastMath](mpsgraphreducedprecisionfastmath/allowfp16intermediates.md)
  Curated list allowing intermediates for multi-pass GPU kernels to be FP16.
- [static var none: MPSGraphReducedPrecisionFastMath](mpsgraphreducedprecisionfastmath/none.md)
  Full precision math with maximum accuracy.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphreducedprecisionfastmath)*