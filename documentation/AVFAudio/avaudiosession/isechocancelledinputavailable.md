# isEchoCancelledInputAvailable

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the built-in microphone and speaker route supports echo cancellation.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.2+

## Declaration

```swift
var isEchoCancelledInputAvailable: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isEchoCancelledInputAvailable;
```

#### Discussion

This value is `true` if the device supports echo cancellation and the app uses the [`playAndRecord`](./category-swift.struct/playandrecord.md) category and [`default`](./mode-swift.struct/default.md) mode.

## See Also

### Configuring echo cancellation
- [var isEchoCancelledInputEnabled: Bool](./isechocancelledinputenabled.md)
  A Boolean value that indicates whether an echo-canceled input is in an enabled state.
- [func setPrefersEchoCancelledInput(Bool) throws](./setprefersechocancelledinput%28_%29.md)
  Sets a preference to enable echo-canceled input on supported hardware.
- [var prefersEchoCancelledInput: Bool](./prefersechocancelledinput.md)
  A Boolean value that indicates the audio session’s preference for using an echo-canceled input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/isechocancelledinputavailable)*