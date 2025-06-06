# delegate

**Framework**: AVFAudio  
**Kind**: property

The delegate object for the speech synthesizer.

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
weak var delegate: (any AVSpeechSynthesizerDelegate)? { get set }
```

## See Also

- [protocol AVSpeechSynthesizerDelegate](avspeechsynthesizerdelegate.md)
  A delegate protocol that contains optional methods you can implement to respond to events that occur during speech synthesis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/delegate)*