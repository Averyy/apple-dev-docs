# isSpeaking

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether the speech synthesizer is speaking or is in a paused state and has utterances to speak.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isSpeaking: Bool { get }
```

#### Discussion

If `true`, the synthesizer is speaking or is in a paused state with utterances in its queue. If `false`, the synthesizer isn’t speaking and it doesn’t have any utterances in its queue.

## See Also

- [var isPaused: Bool](avspeechsynthesizer/ispaused.md)
  A Boolean value that indicates whether a speech synthesizer is in a paused state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/isspeaking)*