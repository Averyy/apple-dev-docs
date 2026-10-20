# loadedTimeRangesChanged

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The snapshot is out of sync due to a change of the loaded time ranges.

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
static let loadedTimeRangesChanged: AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason
```

```c
extern AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason const AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonLoadedTimeRangesChanged;
```

## See Also

### Getting the reasons
- [static let segmentsChanged: AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason](./segmentschanged.md)
  The snapshot is out of sync due to a change of segments.
- [static let currentSegmentChanged: AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason](./currentsegmentchanged.md)
  The snapshot is out of sync due to a change of the current segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerintegratedtimelinesnapshotsoutofsyncreason/loadedtimerangeschanged)*