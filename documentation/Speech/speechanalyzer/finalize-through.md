# finalize(through:)

**Framework**: Speech  
**Kind**: method

Finalizes the modules’ analyses.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func finalize(through: CMTime?) async throws
```

#### Discussion

At the return of this method, input up to and including the given time will have been analyzed. Modules will have published the finalized results to their stream, but the application may not have consumed them from the stream yet. [`volatileRange`](speechanalyzer/volatilerange.md) will post-date the given time.

If the given time has already been finalized (it pre-dates the volatile range), then this method does nothing.

> **Note**: Various errors including `CancellationError` if analysis is finished early before the given input time

## Parameters

- `through`: If  , finalizes up to and including the last audio the analyzer   taken from the input sequence, and if the analyzer has not taken any audio from the input sequence, this method does nothing.

## See Also

- [func cancelAnalysis(before: CMTime)](speechanalyzer/cancelanalysis(before:).md)
  Stops analyzing audio predating the given time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/finalize(through:))*