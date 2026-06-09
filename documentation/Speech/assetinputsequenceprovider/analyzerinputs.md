# analyzerInputs

**Framework**: Speech  
**Kind**: property

A new sequence of speech analyzer input objects containing audio from the asset or file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var analyzerInputs: some Sendable & AsyncSequence<AnalyzerInput, any Error> { get }
```

#### Discussion

The sequence includes the entire asset track’s or file’s audio. You may release the provider object after obtaining the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinputsequenceprovider/analyzerinputs)*