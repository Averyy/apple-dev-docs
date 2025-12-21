# prepareToAnalyze(in:)

**Framework**: Speech  
**Kind**: method

Prepares the analyzer to begin work with minimal startup delay.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func prepareToAnalyze(in audioFormat: AVAudioFormat?) async throws
```

#### Discussion

The analyzer normally performs some configuration lazily as the first audio input becomes available. This method performs that work immediately to reduce or eliminate delays in analyzing the first audio input.

## Parameters

- `audioFormat`: An audio format describing the expected input. The analyzer will load assets appropriate for the given format. If   or if the input is not in this format, the analyzer will reconfigure itself when it processes the actual audio.

## See Also

- [func prepareToAnalyze(in: AVAudioFormat?, withProgressReadyHandler: sending ((Progress) -> Void)?) async throws](speechanalyzer/preparetoanalyze(in:withprogressreadyhandler:).md)
  Prepares the analyzer to begin work with minimal startup delay, reporting the progress of that preparation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/preparetoanalyze(in:))*