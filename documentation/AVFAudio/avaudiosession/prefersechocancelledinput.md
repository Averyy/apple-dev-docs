# prefersEchoCancelledInput

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the audio session’s preference for using an echo-canceled input.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+

## Declaration

```swift
var prefersEchoCancelledInput: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL prefersEchoCancelledInput;
```

## See Also

### Configuring echo cancellation
- [var isEchoCancelledInputAvailable: Bool](./isechocancelledinputavailable.md)
  A Boolean value that indicates whether the built-in microphone and speaker route supports echo cancellation.
- [var isEchoCancelledInputEnabled: Bool](./isechocancelledinputenabled.md)
  A Boolean value that indicates whether an echo-canceled input is in an enabled state.
- [func setPrefersEchoCancelledInput(Bool) throws](./setprefersechocancelledinput%28_%29.md)
  Sets a preference to enable echo-canceled input on supported hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/prefersechocancelledinput)*