# completeAnalysis()

**Framework**: Sound Analysis  
**Kind**: method

Notifies the analyzer when it receives the final audio buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func completeAnalysis()
```

#### Discussion

Use this method for requests that provide final results when a stream reaches its end. The analyzer ignores any further calls to the [`analyze(_:atAudioFramePosition:)`](snaudiostreamanalyzer/analyze(_:ataudioframeposition:).md) method.

## See Also

- [func analyze(AVAudioBuffer, atAudioFramePosition: AVAudioFramePosition)](snaudiostreamanalyzer/analyze(_:ataudioframeposition:).md)
  Adds a new audio buffer to the analyzer’s larger stream buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiostreamanalyzer/completeanalysis())*