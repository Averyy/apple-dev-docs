# analyzerInputs

**Framework**: Speech  
**Kind**: property

A new sequence of speech analyzer input objects containing captured audio.

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

The sequence includes only newly captured audio.

You may release the provider object after obtaining the sequence. The sequence terminates when you deallocate the audio data output, which typically happens when you deallocate the capture session and this provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/captureinputsequenceprovider/analyzerinputs)*