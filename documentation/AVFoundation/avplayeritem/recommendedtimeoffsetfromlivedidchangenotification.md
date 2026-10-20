# recommendedTimeOffsetFromLiveDidChangeNotification

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A notification the player item posts when its offset from the live time changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class let recommendedTimeOffsetFromLiveDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const AVPlayerItemRecommendedTimeOffsetFromLiveDidChangeNotification;
```

#### Discussion

Register to observe notifications of this type to observe changes to the value of the [`recommendedTimeOffsetFromLive`](./recommendedtimeoffsetfromlive.md) property.

## See Also

### Observing notifications
- [class let didPlayToEndTimeNotification: NSNotification.Name](./didplaytoendtimenotification.md)
  A notification the system posts when a player item plays to its end time.
- [class let failedToPlayToEndTimeNotification: NSNotification.Name](./failedtoplaytoendtimenotification.md)
  A notification that the system posts when a player item fails to play to its end time.
- [class let timeJumpedNotification: NSNotification.Name](./timejumpednotification.md)
  A notification the system posts when a player item’s time changes discontinuously.
- [class let playbackStalledNotification: NSNotification.Name](./playbackstallednotification.md)
  A notification the system posts when a player item media doesn’t arrive in time to continue playback.
- [class let mediaSelectionDidChangeNotification: NSNotification.Name](./mediaselectiondidchangenotification.md)
  A notification the player item posts when its media selection changes.
- [class let newAccessLogEntryNotification: NSNotification.Name](./newaccesslogentrynotification.md)
  A notification the system posts when a player item adds a new entry to its access log.
- [class let newErrorLogEntryNotification: NSNotification.Name](./newerrorlogentrynotification.md)
  A notification the system posts when a player item adds a new entry to its error log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/recommendedtimeoffsetfromlivedidchangenotification)*