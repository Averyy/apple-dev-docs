# greedy

**Framework**: Foundation Models  
**Kind**: property

A sampling mode that always chooses the most likely token.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var greedy: GenerationOptions.SamplingMode { get }
```

#### Discussion

Using this mode will always result in the same output for a given input. Responses produced with greedy sampling are statistically likely, but may lack the human-like quality and variety of other sampling strategies.

> **Note**: Sampling modes [`random(top:seed:)`](generationoptions/samplingmode/random(top:seed:).md) and [`random(probabilityThreshold:seed:)`](generationoptions/samplingmode/random(probabilitythreshold:seed:).md)

## See Also

- [static func random(probabilityThreshold: Double, seed: UInt64?) -> GenerationOptions.SamplingMode](generationoptions/samplingmode/random(probabilitythreshold:seed:).md)
  A mode that considers a variable number of high-probability tokens based on the specified threshold.
- [static func random(top: Int, seed: UInt64?) -> GenerationOptions.SamplingMode](generationoptions/samplingmode/random(top:seed:).md)
  A sampling mode that considers a fixed number of high-probability tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/samplingmode/greedy)*