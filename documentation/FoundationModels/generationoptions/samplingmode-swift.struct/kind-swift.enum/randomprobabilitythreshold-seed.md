# GenerationOptions.SamplingMode.Kind.randomProbabilityThreshold(_:seed:)

**Framework**: Foundation Models  
**Kind**: case

A strategy that samples from the highest-probability tokens whose cumulative probability reaches a threshold.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
case randomProbabilityThreshold(Double, seed: UInt64?)
```

## See Also

- [GenerationOptions.SamplingMode.Kind.greedy](generationoptions/samplingmode-swift.struct/kind-swift.enum/greedy.md)
  A strategy that always chooses the most likely token.
- [GenerationOptions.SamplingMode.Kind.randomTopK(_:seed:)](generationoptions/samplingmode-swift.struct/kind-swift.enum/randomtopk(_:seed:).md)
  A strategy that samples from a fixed number of the highest-probability tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/samplingmode-swift.struct/kind-swift.enum/randomprobabilitythreshold(_:seed:))*