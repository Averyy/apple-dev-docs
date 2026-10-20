# setOutputMuted(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Sets a Boolean value to inform the system to mute the session’s output audio. The default value is false (unmuted).

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func setOutputMuted(_ muted: Bool) throws
```

```objc
- (BOOL) setOutputMuted:(BOOL) muted error:(NSError **) outError;
```

#### Discussion

This property is supported with all categories and modes, except for [`playAndRecord`](./category-swift.struct/playandrecord.md) where it is only supported with [`default`](./mode-swift.struct/default.md). Changing the mode to non-default mode with [`playAndRecord`](./category-swift.struct/playandrecord.md) category will cause the session to unmute.

Changes in output mute state can be observed via [`outputMuteStateChangeNotification`](./outputmutestatechangenotification.md). If this value is set to true, [`userIntentToUnmuteOutputNotification`](./userintenttounmuteoutputnotification.md) may be sent when a user hints to unmute by changing the volume.

- `muted`: A Boolean value to set the audio output to the desired muted state.
- `error`: A pointer to an error object. If an error occurs, the framework sets the pointer to an error object that describes the failure.

> **Note**: This will not mute system sounds and haptics.

## See Also

### Configuring audio muting
- [var isOutputMuted: Bool](./isoutputmuted.md)
  A Boolean value that indicates whether audio output is in a muted state.
- [class let outputMuteStateChangeNotification: NSNotification.Name](./outputmutestatechangenotification.md)
  Notification sent to registered listeners when session’s output mute state changes.
- [class let muteStateKey: String](./mutestatekey.md)
  Keys for [`outputMuteStateChangeNotification`](./outputmutestatechangenotification.md) Value is `NSNumber` type with boolean value 0 for unmuted or value 1 for muted (samples zeroed out)
- [class let userIntentToUnmuteOutputNotification: NSNotification.Name](./userintenttounmuteoutputnotification.md)
  Notification sent to registered listeners when the application’s output is muted and user hints to unmute.
- [class let userIntentToUnmuteOutputNotification: NSNotification.Name](./userintenttounmuteoutputnotification.md)
  Notification sent to registered listeners when the application’s output is muted and user hints to unmute.
- [class let muteStateKey: String](./mutestatekey.md)
  Keys for [`outputMuteStateChangeNotification`](./outputmutestatechangenotification.md) Value is `NSNumber` type with boolean value 0 for unmuted or value 1 for muted (samples zeroed out)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setoutputmuted(_:))*