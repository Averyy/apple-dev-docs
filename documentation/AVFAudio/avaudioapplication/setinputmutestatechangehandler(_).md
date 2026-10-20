# setInputMuteStateChangeHandler(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Sets a callback to handle changes to application-level audio muting states.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func setInputMuteStateChangeHandler(_ inputMuteHandler: ((Bool) -> Bool)?) throws
```

```objc
- (BOOL) setInputMuteStateChangeHandler:(BOOL (^)(BOOL inputShouldBeMuted)) inputMuteHandler error:(NSError **) outError;
```

#### Discussion

Use this method to set a closure to handle your macOS app’s input muting logic. The system calls thie closure when the input mute state changes, either due to setting the [`isInputMuted`](./isinputmuted.md) state, or due to a Bluetooth audio accessory gesture (certain AirPods / Beats headphones) changing the mute state.

Since the input mute handling logic should happen a single place, subsequent calls to this method overwrite any previously registered block with the one you provide. You can specify a `nil` to cancel the callback.

> **Note**:  This method is available in macOS only. On other platforms, the system handles muting logic internally. Perform your input muting logic within this closure, and perform your user interface updates within the handler for [`inputMuteStateChangeNotification`](./inputmutestatechangenotification.md).

## Parameters

- `inputMuteHandler`: A callback that the system invokes when the input mute state changes. If the callback receives a [`true`](../../Swift/true.md) value, mute all input audio samples until the next time the system calls the handler. Return a value of [`true`](../../Swift/true.md) if you muted input successfully, or in exceptional cases, return [`false`](../../Swift/false.md) to indicate the mute action fails.

## See Also

### Managing audio input mute state
- [var isInputMuted: Bool](./isinputmuted.md)
  A Boolean value that indicates whether the app’s audio input is in a muted state.
- [func setInputMuted(Bool) throws](./setinputmuted%28_%29.md)
  Sets a Boolean value that indicates whether the app’s audio input is in a muted state.
- [class let inputMuteStateChangeNotification: NSNotification.Name](./inputmutestatechangenotification.md)
  A notification the system posts when the app’s audio input mute state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/setinputmutestatechangehandler(_:))*