# MPSGraphReducedPrecisionFastMath

**Framework**: Metal Performance Shaders Graph  
**Kind**: struct  
**Role**: Structure

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

```c
enum MPSGraphReducedPrecisionFastMath : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./mpsgraphreducedprecisionfastmath/init%28rawvalue%29.md)
### Type Properties
- [static var allowConvertingOperandsFromFP32ToFP19: MPSGraphReducedPrecisionFastMath](./mpsgraphreducedprecisionfastmath/allowconvertingoperandsfromfp32tofp19.md)
  Allow conversion of operands to FP19 or TF32 from FP32 when needed by dropping 13 mantissa bits.
- [static var allowFP16Conv2DWinogradTransformIntermediate: MPSGraphReducedPrecisionFastMath](./mpsgraphreducedprecisionfastmath/allowfp16conv2dwinogradtransformintermediate.md)
  Execute winograd transform intermediate as FP16.
- [static var allowFP16Intermediates: MPSGraphReducedPrecisionFastMath](./mpsgraphreducedprecisionfastmath/allowfp16intermediates.md)
  Curated list allowing intermediates for multi-pass GPU kernels to be FP16.
- [static var none: MPSGraphReducedPrecisionFastMath](./mpsgraphreducedprecisionfastmath/none.md)
  Full precision math with maximum accuracy.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphreducedprecisionfastmath)*