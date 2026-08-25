# samplingStrategy

**Framework**: Evaluations  
**Kind**: property

The strategy for selecting existing samples as examples in the prompt.

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
var samplingStrategy: SampleGenerator<SampleType>.SamplingStrategy? { get }
```

#### Discussion

When `nil`, the generator shows no examples and doesn’t retry on repetition. When set, the strategy also controls retry behavior when the model repeats itself.

## See Also

- [var validator: ((SampleType) async throws -> Bool)?](samplegenerator/validator.md)
  An optional closure that decides whether a generated sample is valid.
- [SampleGenerator.SamplingStrategy](samplegenerator/samplingstrategy-swift.enum.md)
  The values that define how the generator selects existing samples as examples in the generation prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/samplegenerator/samplingstrategy-swift.property)*