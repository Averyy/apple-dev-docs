# cancelAnalysis(before:)

**Framework**: Speech  
**Kind**: method

Stops analyzing audio predating the given time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func cancelAnalysis(before: CMTime)
```

#### Discussion

This method is useful in live-audio cases where you are no longer interested in results predating a certain time. For example, when you are captioning video and the scene changes, you do not need pending captions from the previous scene.

This method can also be used to force “catch-up” if the analyzer is taking too long. By calling [`finalize(through:)`](speechanalyzer/finalize(through:).md), you indicate that you will  for pending results. By calling `cancelAnalysis(before:)`, you indicate that you  any longer for certain pending results.

Analysis will continue normally at and after the given time.

If you know in advance that you do not need results for a given range of audio, it is preferable to simply not provide that audio as input.

This is a best-effort cancellation. The implementation may still publish results from before the given time.

## Parameters

- `before`: An audio time that marks audio that remains of interest.

## See Also

- [func finalize(through: CMTime?) async throws](speechanalyzer/finalize(through:).md)
  Finalizes the modules’ analyses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/cancelanalysis(before:))*