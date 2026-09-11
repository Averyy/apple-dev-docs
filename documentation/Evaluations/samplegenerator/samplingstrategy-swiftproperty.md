# samplingStrategy

**Framework**: Evaluations  
**Kind**: property

The strategy for selecting existing samples as examples in the prompt.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

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