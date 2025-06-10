# outputMuteStateChangeNotification

**Framework**: AVFAudio  
**Kind**: property

Notification sent to registered listeners when session’s output mute state changes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
class let outputMuteStateChangeNotification: NSNotification.Name
```

#### Discussion

The userInfo dictionary will contain the updated output mute value as accessed by [`muteStateKey`](avaudiosession/mutestatekey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/outputmutestatechangenotification)*