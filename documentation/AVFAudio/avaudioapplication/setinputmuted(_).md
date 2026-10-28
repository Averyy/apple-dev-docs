# setInputMuted(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Sets a Boolean value that indicates whether the app’s audio input is in a muted state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
func setInputMuted(_ muted: Bool) throws
```

```objc
- (BOOL) setInputMuted:(BOOL) muted error:(NSError **) outError;
```

## Discussion

In platforms that use [`AVAudioSession`](../avaudiosession.md), setting the value to [`true`](../../Swift/true.md) mutes all sources of audio input in the app. In macOS, the system instead invokes the callback that you register by calling [`setInputMuteStateChangeHandler(_:)`](./setinputmutestatechangehandler%28_%29.md) to handle input muting.

> **Note**:  This setting is specific to your app and doesn’t affect hardware mute state.

## Parameters

- `muted`: A Boolean value that indicates the new mute state.

## See Also

### Managing audio input mute state
- [var isInputMuted: Bool](./isinputmuted.md)
  A Boolean value that indicates whether the app’s audio input is in a muted state.
- [class let inputMuteStateChangeNotification: NSNotification.Name](./inputmutestatechangenotification.md)
  A notification the system posts when the app’s audio input mute state changes.
- [func setInputMuteStateChangeHandler(((Bool) -> Bool)?) throws](./setinputmutestatechangehandler%28_%29.md)
  Sets a callback to handle changes to application-level audio muting states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/setinputmuted(_:))*