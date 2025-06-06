# snapshotsOutOfSyncNotification

**Framework**: AVFoundation  
**Kind**: property

A notification the system posts when the snapshot objects provided by this timeline become out of sync with the current timeline state.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
class let snapshotsOutOfSyncNotification: NSNotification.Name
```

## Topics

### User-information keys
- [class let snapshotsOutOfSyncReasonKey: String](avplayeritemintegratedtimeline/snapshotsoutofsyncreasonkey.md)
  A key to retrieve the reason for an out-of-sync state notification.
- [struct AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason](avplayerintegratedtimelinesnapshotsoutofsyncreason.md)
  Constants that represent the reason for an out-of-sync state.

## See Also

- [var currentSnapshot: AVPlayerItemIntegratedTimelineSnapshot](avplayeritemintegratedtimeline/currentsnapshot.md)
  An immutable representation of the timeline state at time of request.
- [class AVPlayerItemIntegratedTimelineSnapshot](avplayeritemintegratedtimelinesnapshot.md)
  An immutable representation of inspectable details of an integrated timeline object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/snapshotsoutofsyncnotification)*