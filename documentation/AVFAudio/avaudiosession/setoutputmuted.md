# setOutputMuted(_:)

**Framework**: AVFAudio  
**Kind**: method

Sets a Boolean value to inform the system to mute the session’s output audio. The default value is false (unmuted).

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
func setOutputMuted(_ muted: Bool) throws
```

#### Discussion

This property is supported with all categories and modes, except for [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) where it is only supported with [`default`](avaudiosession/mode-swift.struct/default.md). Changing the mode to non-default mode with [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) category will cause the session to unmute.

Changes in output mute state can be observed via [`outputMuteStateChangeNotification`](avaudiosession/outputmutestatechangenotification.md). If this value is set to true, [`userIntentToUnmuteOutputNotification`](avaudiosession/userintenttounmuteoutputnotification.md) may be sent when a user hints to unmute by changing the volume.

- `muted`: A Boolean value to set the audio output to the desired muted state.
- `error`: A pointer to an error object. If an error occurs, the framework sets the pointer to an error object that describes the failure.

> **Note**: This will not mute system sounds and haptics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setoutputmuted(_:))*