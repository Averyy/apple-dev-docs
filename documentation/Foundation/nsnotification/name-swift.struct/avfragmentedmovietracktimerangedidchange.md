# AVFragmentedMovieTrackTimeRangeDidChange

**Framework**: Foundation  
**Kind**: property

A notification the system posts when a fragmented movie minder observes a change to a movie track’s time range.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let AVFragmentedMovieTrackTimeRangeDidChange: NSNotification.Name
```

#### Discussion

The system posts this notification only for changes that occur after a movie track’s [`timeRange`](https://developer.apple.com/documentation/avfoundation/avassettrack/timerange) property reaches a [`AVKeyValueStatus.loaded`](https://developer.apple.com/documentation/avfoundation/avkeyvaluestatus/loaded) status.

## See Also

- [static let AVAssetChapterMetadataGroupsDidChange: NSNotification.Name](nsnotification/name-swift.struct/avassetchaptermetadatagroupsdidchange.md)
  A notification the system posts when an asset’s chapter metadata groups change.
- [static let AVAssetContainsFragmentsDidChange: NSNotification.Name](nsnotification/name-swift.struct/avassetcontainsfragmentsdidchange.md)
  A notification the system posts when an asset’s fragments change.
- [static let AVAssetDurationDidChange: NSNotification.Name](nsnotification/name-swift.struct/avassetdurationdidchange.md)
  A notification the system posts when a fragmented asset minder observes a change to a fragmented asset’s duration.
- [static let AVAssetMediaSelectionGroupsDidChange: NSNotification.Name](nsnotification/name-swift.struct/avassetmediaselectiongroupsdidchange.md)
  A notification the system posts when an asset’s media selection groups change.
- [static let AVAssetTrackSegmentsDidChange: NSNotification.Name](nsnotification/name-swift.struct/avassettracksegmentsdidchange.md)
  A notification the system posts when a fragmented asset minder observes a change to a fragmented asset track’s segments.
- [static let AVAssetTrackTimeRangeDidChange: NSNotification.Name](nsnotification/name-swift.struct/avassettracktimerangedidchange.md)
  A notification the system posts when a fragmented asset minder observes a change to a fragmented asset track’s time range.
- [static let AVAssetTrackTrackAssociationsDidChange: NSNotification.Name](nsnotification/name-swift.struct/avassettracktrackassociationsdidchange.md)
  A notification the system posts when the track associations for an asset track change.
- [static let AVAssetWasDefragmented: NSNotification.Name](nsnotification/name-swift.struct/avassetwasdefragmented.md)
  A notification the system posts when a fragmented asset minder observes that the system defragments the asset on disk.
- [class let subjectAreaDidChangeNotification: NSNotification.Name](../avfoundation/avcapturedevice/subjectareadidchangenotification.md)
  A notification the system posts when a capture device detects a substantial change to the video subject area.
- [class let wasConnectedNotification: NSNotification.Name](../avfoundation/avcapturedevice/wasconnectednotification.md)
  A notification the system posts when a new capture device becomes available.
- [class let wasDisconnectedNotification: NSNotification.Name](../avfoundation/avcapturedevice/wasdisconnectednotification.md)
  A notification the system posts when an existing device becomes unavailable.
- [class let formatDescriptionDidChangeNotification: NSNotification.Name](../avfoundation/avcaptureinput/port/formatdescriptiondidchangenotification.md)
  A notification the system posts when the capture input port’s format description changes.
- [class let didStartRunningNotification: NSNotification.Name](../avfoundation/avcapturesession/didstartrunningnotification.md)
  A notification the system posts when a capture session starts.
- [class let didStopRunningNotification: NSNotification.Name](../avfoundation/avcapturesession/didstoprunningnotification.md)
  A notification the system posts when a capture session stops.
- [class let interruptionEndedNotification: NSNotification.Name](../avfoundation/avcapturesession/interruptionendednotification.md)
  A notification the system posts when an interruption to a capture session finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/avfragmentedmovietracktimerangedidchange)*