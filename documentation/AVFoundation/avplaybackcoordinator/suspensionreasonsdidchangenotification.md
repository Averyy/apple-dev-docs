# suspensionReasonsDidChangeNotification

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A notification that the coordinator posts when its suspension reasons change.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class let suspensionReasonsDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const AVPlaybackCoordinatorSuspensionReasonsDidChangeNotification;
```

## See Also

### Observing suspension reasons
- [var suspensionReasons: [AVCoordinatedPlaybackSuspension.Reason]](./suspensionreasons.md)
  The reasons a coordinator is currently unable to participate in a group playback activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/suspensionreasonsdidchangenotification)*