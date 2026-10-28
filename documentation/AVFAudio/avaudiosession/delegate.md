# delegate

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The delegate object for the audio session.

**Availability**:
- Mac Catalyst 14.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the notifications described in the Handling interruptions section of this class instead.

## Declaration

```swift
unowned(unsafe) var delegate: (any AVAudioSessionDelegate)? { get set }
```

```objc
@property (assign, nullable) id<AVAudioSessionDelegate> delegate;
```

## Discussion

The delegate object must implement the protocol described in [`AVAudioSessionDelegate`](../avaudiosessiondelegate.md).

## See Also

### Responding to audio session changes
- [protocol AVAudioSessionDelegate](../avaudiosessiondelegate.md)
  A protocol that defines responses to changes in state for the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/delegate)*