# analyzerInputs

**Framework**: Speech  
**Kind**: property

A new sequence of speech analyzer input objects containing audio from the asset or file.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final var analyzerInputs: some Sendable & AsyncSequence<AnalyzerInput, any Error> { get }
```

#### Discussion

The sequence includes the entire asset track’s or file’s audio. You may release the provider object after obtaining the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinputsequenceprovider/analyzerinputs)*