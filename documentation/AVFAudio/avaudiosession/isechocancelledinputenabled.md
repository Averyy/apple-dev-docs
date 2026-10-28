# isEchoCancelledInputEnabled

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether an echo-canceled input is in an enabled state.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+

## Declaration

```swift
var isEchoCancelledInputEnabled: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isEchoCancelledInputEnabled;
```

## Discussion

For more information about echo cancellation, see [`setPrefersEchoCancelledInput(_:)`](./setprefersechocancelledinput%28_%29.md).

## See Also

### Configuring echo cancellation
- [var isEchoCancelledInputAvailable: Bool](./isechocancelledinputavailable.md)
  A Boolean value that indicates whether the built-in microphone and speaker route supports echo cancellation.
- [func setPrefersEchoCancelledInput(Bool) throws](./setprefersechocancelledinput%28_%29.md)
  Sets a preference to enable echo-canceled input on supported hardware.
- [var prefersEchoCancelledInput: Bool](./prefersechocancelledinput.md)
  A Boolean value that indicates the audio session’s preference for using an echo-canceled input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/isechocancelledinputenabled)*