# muteStateKey

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

Keys for [`outputMuteStateChangeNotification`](./outputmutestatechangenotification.md) Value is `NSNumber` type with boolean value 0 for unmuted or value 1 for muted (samples zeroed out)

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class let muteStateKey: String
```

```c
extern NSString * const AVAudioSessionMuteStateKey;
```

## See Also

### Configuring audio muting
- [var isOutputMuted: Bool](./isoutputmuted.md)
  A Boolean value that indicates whether audio output is in a muted state.
- [func setOutputMuted(Bool) throws](./setoutputmuted%28_%29.md)
  Sets a Boolean value to inform the system to mute the session’s output audio. The default value is false (unmuted).
- [class let outputMuteStateChangeNotification: NSNotification.Name](./outputmutestatechangenotification.md)
  Notification sent to registered listeners when session’s output mute state changes.
- [class let userIntentToUnmuteOutputNotification: NSNotification.Name](./userintenttounmuteoutputnotification.md)
  Notification sent to registered listeners when the application’s output is muted and user hints to unmute.
- [class let userIntentToUnmuteOutputNotification: NSNotification.Name](./userintenttounmuteoutputnotification.md)
  Notification sent to registered listeners when the application’s output is muted and user hints to unmute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mutestatekey)*