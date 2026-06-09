# makeSamples(_:targetCount:sessionProvider:validator:)

**Framework**: Swift  
**Kind**: method

Generates synthetic data based on this dataset and returns a stream of new samples.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func makeSamples<T>(_ prompt: Prompt, targetCount: Int, sessionProvider: (@Sendable () -> LanguageModelSession)? = nil, validator: (nonisolated(nonsending) @Sendable (ModelSample<T>) async throws -> Bool)? = nil) -> some AsyncSequence<ModelSample<T>, any Error> where Element == ModelSample<T>, T : Generable, T : Decodable, T : Encodable, T : Sendable
```

#### Discussion

For more control over generation, create a `SampleGenerator` directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/makesamples(_:targetcount:sessionprovider:validator:)-5j7t0)*