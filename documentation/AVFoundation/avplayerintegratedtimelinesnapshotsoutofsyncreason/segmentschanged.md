# segmentsChanged

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The snapshot is out of sync due to a change of segments.

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
static let segmentsChanged: AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason
```

```c
extern AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason const AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonSegmentsChanged;
```

## See Also

### Getting the reasons
- [static let currentSegmentChanged: AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason](./currentsegmentchanged.md)
  The snapshot is out of sync due to a change of the current segment.
- [static let loadedTimeRangesChanged: AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason](./loadedtimerangeschanged.md)
  The snapshot is out of sync due to a change of the loaded time ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerintegratedtimelinesnapshotsoutofsyncreason/segmentschanged)*