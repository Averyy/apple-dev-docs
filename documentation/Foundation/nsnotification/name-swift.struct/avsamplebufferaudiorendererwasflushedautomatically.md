# AVSampleBufferAudioRendererWasFlushedAutomatically

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A notification the system posts when a renderer flushes its enqueued media data without an explicit request to do so.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: Use the result of AVSampleBufferAudioRenderer.Receiver enqueue(_:) and enqueueImmediately(_:) for .successWithSuggestedFlushReason instead

## Declaration

```swift
static let AVSampleBufferAudioRendererWasFlushedAutomatically: NSNotification.Name
```

## Discussion

A renderer may flush enqueued media data when the user routes playback to a new destination, or when you change the playback rate of the attached [`AVSampleBufferRenderSynchronizer`](../../../AVFoundation/avsamplebufferrendersynchronizer.md). No flush occurs for normal pauses and resumes.

## See Also

### AVFoundation
- [static let AVAssetChapterMetadataGroupsDidChange: NSNotification.Name](./avassetchaptermetadatagroupsdidchange.md)
  A notification the system posts when an asset’s chapter metadata groups change.
- [static let AVAssetContainsFragmentsDidChange: NSNotification.Name](./avassetcontainsfragmentsdidchange.md)
  A notification the system posts when an asset’s fragments change.
- [static let AVAssetDurationDidChange: NSNotification.Name](./avassetdurationdidchange.md)
  A notification the system posts when a fragmented asset minder observes a change to a fragmented asset’s duration.
- [static let AVAssetMediaSelectionGroupsDidChange: NSNotification.Name](./avassetmediaselectiongroupsdidchange.md)
  A notification the system posts when an asset’s media selection groups change.
- [static let AVAssetTrackSegmentsDidChange: NSNotification.Name](./avassettracksegmentsdidchange.md)
  A notification the system posts when a fragmented asset minder observes a change to a fragmented asset track’s segments.
- [static let AVAssetTrackTimeRangeDidChange: NSNotification.Name](./avassettracktimerangedidchange.md)
  A notification the system posts when a fragmented asset minder observes a change to a fragmented asset track’s time range.
- [static let AVAssetTrackTrackAssociationsDidChange: NSNotification.Name](./avassettracktrackassociationsdidchange.md)
  A notification the system posts when the track associations for an asset track change.
- [static let AVAssetWasDefragmented: NSNotification.Name](./avassetwasdefragmented.md)
  A notification the system posts when a fragmented asset minder observes that the system defragments the asset on disk.
- [class let subjectAreaDidChangeNotification: NSNotification.Name](../../../AVFoundation/avcapturedevice/subjectareadidchangenotification.md)
  A notification the system posts when a capture device detects a substantial change to the video subject area.
- [class let wasConnectedNotification: NSNotification.Name](../../../AVFoundation/avcapturedevice/wasconnectednotification.md)
  A notification the system posts when a new capture device becomes available.
- [class let wasDisconnectedNotification: NSNotification.Name](../../../AVFoundation/avcapturedevice/wasdisconnectednotification.md)
  A notification the system posts when an existing device becomes unavailable.
- [class let formatDescriptionDidChangeNotification: NSNotification.Name](../../../AVFoundation/avcaptureinput/port/formatdescriptiondidchangenotification.md)
  A notification the system posts when the capture input port’s format description changes.
- [class let didStartRunningNotification: NSNotification.Name](../../../AVFoundation/avcapturesession/didstartrunningnotification.md)
  A notification the system posts when a capture session starts.
- [class let didStopRunningNotification: NSNotification.Name](../../../AVFoundation/avcapturesession/didstoprunningnotification.md)
  A notification the system posts when a capture session stops.
- [class let interruptionEndedNotification: NSNotification.Name](../../../AVFoundation/avcapturesession/interruptionendednotification.md)
  A notification the system posts when an interruption to a capture session finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/avsamplebufferaudiorendererwasflushedautomatically)*