# init(_:samples:targetCount:sessionProvider:samplingStrategy:validator:)

**Framework**: Evaluations  
**Kind**: init

Creates a generator for custom, generable evaluation samples.

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
init(_ prompt: Prompt, samples: [SampleType], targetCount: Int, sessionProvider: (@Sendable () -> LanguageModelSession)? = nil, samplingStrategy: SampleGenerator<SampleType>.SamplingStrategy? = .random(), validator: (nonisolated(nonsending) @Sendable (SampleType) async throws -> Bool)? = nil) where SampleType : Generable
```

## Parameters

- `prompt`: The prompt the generator sends to the language model session.
- `samples`: The initial set of evaluation samples that provide context.
- `targetCount`: The total number of samples in the resulting dataset.
- `sessionProvider`: A closure that creates a new language model session.
- `samplingStrategy`: The strategy for selecting example samples.
- `validator`: An optional closure that decides whether a generated sample is valid.

## See Also

- [init<T>(Prompt, samples: [SampleType], targetCount: Int, sessionProvider: (() -> LanguageModelSession)?, samplingStrategy: SampleGenerator<SampleType>.SamplingStrategy?, validator: ((SampleType) async throws -> Bool)?)](samplegenerator/init(_:samples:targetcount:sessionprovider:samplingstrategy:validator:)-8t01x.md)
  Creates a generator for sample values with a generable-expected value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/samplegenerator/init(_:samples:targetcount:sessionprovider:samplingstrategy:validator:)-2804x)*