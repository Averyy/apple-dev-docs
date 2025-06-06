# delegate

**Framework**: AVFAudio  
**Kind**: property

The delegate object for the audio session.

**Availability**:
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
unowned(unsafe) var delegate: (any AVAudioSessionDelegate)? { get set }
```

#### Discussion

The delegate object must implement the protocol described in [`AVAudioSessionDelegate`](avaudiosessiondelegate.md).

## See Also

- [protocol AVAudioSessionDelegate](avaudiosessiondelegate.md)
  A protocol that defines responses to changes in state for the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/delegate)*