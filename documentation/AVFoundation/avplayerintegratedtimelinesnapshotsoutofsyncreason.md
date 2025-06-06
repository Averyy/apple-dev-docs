# AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason

**Framework**: AVFoundation  
**Kind**: struct

Constants that represent the reason for an out-of-sync state.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason
```

## Topics

### Getting the reasons
- [static let segmentsChanged: AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason](avplayerintegratedtimelinesnapshotsoutofsyncreason/segmentschanged.md)
  The snapshot is out of sync due to a change of segments.
- [static let currentSegmentChanged: AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason](avplayerintegratedtimelinesnapshotsoutofsyncreason/currentsegmentchanged.md)
  The snapshot is out of sync due to a change of the current segment.
- [static let loadedTimeRangesChanged: AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason](avplayerintegratedtimelinesnapshotsoutofsyncreason/loadedtimerangeschanged.md)
  The snapshot is out of sync due to a change of the loaded time ranges.
### Creating a reason
- [init(rawValue: String)](avplayerintegratedtimelinesnapshotsoutofsyncreason/init(rawvalue:).md)
  Creates a new out-of-sync reason from the value you specify.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class let snapshotsOutOfSyncReasonKey: String](avplayeritemintegratedtimeline/snapshotsoutofsyncreasonkey.md)
  A key to retrieve the reason for an out-of-sync state notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerintegratedtimelinesnapshotsoutofsyncreason)*