# isPaused

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a speech synthesizer is in a paused state.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isPaused: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPaused) BOOL paused;
```

## Discussion

If `true`, the speech synthesizer is in a paused state after beginning to speak an utterance; otherwise, `false`.

## See Also

### Inspecting a speech synthesizer
- [var isSpeaking: Bool](./isspeaking.md)
  A Boolean value that indicates whether the speech synthesizer is speaking or is in a paused state and has utterances to speak.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/ispaused)*