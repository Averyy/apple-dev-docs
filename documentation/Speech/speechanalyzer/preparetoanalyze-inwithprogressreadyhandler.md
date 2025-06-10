# prepareToAnalyze(in:withProgressReadyHandler:)

**Framework**: Speech  
**Kind**: method

Prepares the analyzer to begin work with minimal startup delay, reporting the progress of that preparation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func prepareToAnalyze(in audioFormat: AVAudioFormat?, withProgressReadyHandler progressReadyHandler: sending ((Progress) -> Void)?) async throws
```

## Parameters

- `audioFormat`: An audio format describing the expected input. The analyzer will load assets appropriate for the given format. If   or if the input is not in this format, the analyzer will reconfigure itself when it processes the actual audio.
- `progressReadyHandler`: A closure that this method calls when progress reporting becomes available. The closure takes the following parameter:

## See Also

- [func prepareToAnalyze(in: AVAudioFormat?) async throws](speechanalyzer/preparetoanalyze(in:).md)
  Prepares the analyzer to begin work with minimal startup delay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/preparetoanalyze(in:withprogressreadyhandler:))*