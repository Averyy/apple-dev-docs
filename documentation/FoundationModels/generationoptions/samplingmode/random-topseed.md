# random(top:seed:)

**Framework**: Foundation Models  
**Kind**: method

A sampling mode that considers a fixed number of high-probability tokens.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func random(top k: Int, seed: UInt64? = nil) -> GenerationOptions.SamplingMode
```

#### Discussion

Also known as top-k.

During the token-selection process, the vocabulary is sorted by probability a token is selected from among the top K candidates. Smaller values of K will ensure only the most probable tokens are candidates for selection, resulting in more deterministic and confident answers. Larger values of K will allow less probably tokens to be selected, raising non-determinism and creativity.

> **Note**: Setting a random seed is not guaranteed to result in fully deterministic output. It is best effort.

## Parameters

- `seed`: An optional random seed used to make output more deterministic.

## See Also

- [static var greedy: GenerationOptions.SamplingMode](generationoptions/samplingmode/greedy.md)
  A sampling mode that always chooses the most likely token.
- [static func random(probabilityThreshold: Double, seed: UInt64?) -> GenerationOptions.SamplingMode](generationoptions/samplingmode/random(probabilitythreshold:seed:).md)
  A mode that considers a variable number of high-probability tokens based on the specified threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/samplingmode/random(top:seed:))*