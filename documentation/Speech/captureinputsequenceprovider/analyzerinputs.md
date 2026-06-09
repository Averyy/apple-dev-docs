# analyzerInputs

**Framework**: Speech  
**Kind**: property

A new sequence of speech analyzer input objects containing captured audio.

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

The sequence includes only newly captured audio.

You may release the provider object after obtaining the sequence. The sequence terminates when you deallocate the audio data output, which typically happens when you deallocate the capture session and this provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/captureinputsequenceprovider/analyzerinputs)*