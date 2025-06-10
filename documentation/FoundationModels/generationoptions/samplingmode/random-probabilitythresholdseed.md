# random(probabilityThreshold:seed:)

**Framework**: Foundation Models  
**Kind**: method

A mode that considers a variable number of high-probability tokens based on the specified threshold.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func random(probabilityThreshold: Double, seed: UInt64? = nil) -> GenerationOptions.SamplingMode
```

#### Discussion

Also known as top-p or nucleus sampling.

With nucleus sampling, tokens are sorted by probability and added to a pool of candidates until the cumulative probability of the pool exceeds the specified threshold, and then a token is sampled from the pool.

Because the number of tokens isn’t predetermined, the selection pool size will be larger when the distribution is flat and smaller when it is spikey. This variability can lead to a wider variety of options to choose from, and potentially more creative responses.

> **Note**: Setting a random seed is not guaranteed to result in fully deterministic output. It is best effort.

## Parameters

- `probabilityThreshold`: A number between   and   that   increases sampling pool size.
- `seed`: An optional random seed used to make output more deterministic.

## See Also

- [static var greedy: GenerationOptions.SamplingMode](generationoptions/samplingmode/greedy.md)
  A sampling mode that always chooses the most likely token.
- [static func random(top: Int, seed: UInt64?) -> GenerationOptions.SamplingMode](generationoptions/samplingmode/random(top:seed:).md)
  A sampling mode that considers a fixed number of high-probability tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/samplingmode/random(probabilitythreshold:seed:))*