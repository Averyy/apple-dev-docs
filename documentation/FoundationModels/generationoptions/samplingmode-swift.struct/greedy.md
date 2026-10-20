# greedy

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Type Property

A sampling mode that always chooses the most likely token.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
static var greedy: GenerationOptions.SamplingMode { get }
```

## Mentions

- [Analyzing images with multimodal prompting](../../analyzing-images-with-multimodal-prompting.md)

#### Discussion

This mode always produces the same output for a given input. Responses produced with greedy sampling are statistically likely, but may lack the human-like quality and variety of other sampling strategies.

> **See Also**: Sampling modes [`random(top:seed:)`](./random%28top,seed%29.md) and [`random(probabilityThreshold:seed:)`](./random%28probabilitythreshold,seed%29.md)

## See Also

### Sampling modes
- [static func random(probabilityThreshold: Double, seed: UInt64?) -> GenerationOptions.SamplingMode](./random%28probabilitythreshold,seed%29.md)
  A mode that considers a variable number of high-probability tokens based on the specified threshold.
- [static func random(top: Int, seed: UInt64?) -> GenerationOptions.SamplingMode](./random%28top,seed%29.md)
  A sampling mode that considers a fixed number of high-probability tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/samplingmode-swift.struct/greedy)*