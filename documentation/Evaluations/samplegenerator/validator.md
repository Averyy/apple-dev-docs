# validator

**Framework**: Evaluations  
**Kind**: property

An optional closure that decides whether a generated sample is valid.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
var validator: (nonisolated(nonsending) @Sendable (SampleType) async throws -> Bool)? { get }
```

#### Discussion

When provided, the generator collects rejected samples in [`invalidSamples`](samplegenerator/invalidsamples.md).

## See Also

- [var samplingStrategy: SampleGenerator<SampleType>.SamplingStrategy?](samplegenerator/samplingstrategy-swift.property.md)
  The strategy for selecting existing samples as examples in the prompt.
- [SampleGenerator.SamplingStrategy](samplegenerator/samplingstrategy-swift.enum.md)
  The values that define how the generator selects existing samples as examples in the generation prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/samplegenerator/validator)*