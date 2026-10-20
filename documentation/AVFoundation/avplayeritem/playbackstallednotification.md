# playbackStalledNotification

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A notification the system posts when a player item media doesn’t arrive in time to continue playback.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class let playbackStalledNotification: NSNotification.Name
```

```c
extern NSNotificationName const AVPlayerItemPlaybackStalledNotification;
```

#### Discussion

The notification’s object is the player item whose playback is unable to continue due to network delays. Streaming-media playback continues after the player item retrieves a sufficient amount of data. File-based playback doesn’t continue.

> ❗ **Important**:  The system may post this notification on a thread other than the one you use to register the observer.

## See Also

### Observing notifications
- [class let didPlayToEndTimeNotification: NSNotification.Name](./didplaytoendtimenotification.md)
  A notification the system posts when a player item plays to its end time.
- [class let failedToPlayToEndTimeNotification: NSNotification.Name](./failedtoplaytoendtimenotification.md)
  A notification that the system posts when a player item fails to play to its end time.
- [class let timeJumpedNotification: NSNotification.Name](./timejumpednotification.md)
  A notification the system posts when a player item’s time changes discontinuously.
- [class let mediaSelectionDidChangeNotification: NSNotification.Name](./mediaselectiondidchangenotification.md)
  A notification the player item posts when its media selection changes.
- [class let recommendedTimeOffsetFromLiveDidChangeNotification: NSNotification.Name](./recommendedtimeoffsetfromlivedidchangenotification.md)
  A notification the player item posts when its offset from the live time changes.
- [class let newAccessLogEntryNotification: NSNotification.Name](./newaccesslogentrynotification.md)
  A notification the system posts when a player item adds a new entry to its access log.
- [class let newErrorLogEntryNotification: NSNotification.Name](./newerrorlogentrynotification.md)
  A notification the system posts when a player item adds a new entry to its error log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/playbackstallednotification)*