# makeSamples(_:targetCount:sessionProvider:validator:)

**Framework**: Swift  
**Kind**: method

Generates synthetic data based on this dataset and returns a stream of new samples.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func makeSamples<T>(_ prompt: Prompt, targetCount: Int, sessionProvider: (@Sendable () -> LanguageModelSession)? = nil, validator: (nonisolated(nonsending) @Sendable (ModelSample<T>) async throws -> Bool)? = nil) -> some AsyncSequence<ModelSample<T>, any Error> where Element == ModelSample<T>, T : Generable, T : Decodable, T : Encodable, T : Sendable
```

#### Return Value

An async throwing stream of newly generated samples.

#### Discussion

For more control over generation, create a `SampleGenerator` directly.

## Parameters

- `prompt`: The prompt the generator sends to the language model session.
- `targetCount`: The desired total number of samples, counting both the initial dataset and newly generated ones.
- `sessionProvider`: A closure that creates a new language model session, or `nil` to use the default.
- `validator`: A closure that decides whether a generated sample is valid, or `nil` to accept all samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/makesamples(_:targetcount:sessionprovider:validator:)-5j7t0)*