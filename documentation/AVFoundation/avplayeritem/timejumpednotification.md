# timeJumpedNotification

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A notification the system posts when a player item’s time changes discontinuously.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class let timeJumpedNotification: NSNotification.Name
```

```c
extern NSNotificationName const AVPlayerItemTimeJumpedNotification;
```

## Discussion

The notification’s object is the player item.

> ❗ **Important**:  The system may post this notification on a thread other than the one you use to register the observer.

## Topics

### User information keys
- [class let timeJumpedOriginatingParticipantKey: String](./timejumpedoriginatingparticipantkey.md)
  A key to retrieve a unique identifier of the participant that caused the time jump.

## See Also

### Observing notifications
- [class let didPlayToEndTimeNotification: NSNotification.Name](./didplaytoendtimenotification.md)
  A notification the system posts when a player item plays to its end time.
- [class let failedToPlayToEndTimeNotification: NSNotification.Name](./failedtoplaytoendtimenotification.md)
  A notification that the system posts when a player item fails to play to its end time.
- [class let playbackStalledNotification: NSNotification.Name](./playbackstallednotification.md)
  A notification the system posts when a player item media doesn’t arrive in time to continue playback.
- [class let mediaSelectionDidChangeNotification: NSNotification.Name](./mediaselectiondidchangenotification.md)
  A notification the player item posts when its media selection changes.
- [class let recommendedTimeOffsetFromLiveDidChangeNotification: NSNotification.Name](./recommendedtimeoffsetfromlivedidchangenotification.md)
  A notification the player item posts when its offset from the live time changes.
- [class let newAccessLogEntryNotification: NSNotification.Name](./newaccesslogentrynotification.md)
  A notification the system posts when a player item adds a new entry to its access log.
- [class let newErrorLogEntryNotification: NSNotification.Name](./newerrorlogentrynotification.md)
  A notification the system posts when a player item adds a new entry to its error log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/timejumpednotification)*