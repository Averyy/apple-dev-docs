# AVAssetChapterMetadataGroupsDidChangeNotification

**Framework**: AVFoundation  
**Kind**: var  
**Role**: Global Variable

Posted when the collection of arrays of timed metadata groups representing chapters of an AVAsset change and when any of the contents of the timed metadata groups change, but only for changes that occur after the status of the value of @“availableChapterLocales” has reached AVKeyValueStatusLoaded.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern NSString * const AVAssetChapterMetadataGroupsDidChangeNotification;
```

## See Also

### Notifications
- [AVAssetContainsFragmentsDidChangeNotification](./avassetcontainsfragmentsdidchangenotification.md)
  A notification the system posts when an asset’s fragments change.
- [AVAssetDurationDidChangeNotification](./avassetdurationdidchangenotification.md)
  A notification the system posts when a fragmented asset minder observes a change to a fragmented asset’s duration.
- [AVAssetMediaSelectionGroupsDidChangeNotification](./avassetmediaselectiongroupsdidchangenotification.md)
  Posted when the collection of media selection groups provided by an AVAsset changes and when any of the contents of its media selection groups change, but only for changes that occur after the status of the value of @“availableMediaCharacteristicsWithMediaSelectionOptions” has reached AVKeyValueStatusLoaded.
- [AVAssetTrackSegmentsDidChangeNotification](./avassettracksegmentsdidchangenotification.md)
  Posted when the array of segments of an AVFragmentedAssetTrack changes while the associated instance of AVFragmentedAsset is being minded by an AVFragmentedAssetMinder, but only for changes that occur after the status of the value of @“segments” has reached AVKeyValueStatusLoaded.
- [AVAssetTrackTimeRangeDidChangeNotification](./avassettracktimerangedidchangenotification.md)
  Posted when the timeRange of an AVFragmentedAssetTrack changes while the associated instance of AVFragmentedAsset is being minded by an AVFragmentedAssetMinder, but only for changes that occur after the status of the value of @“timeRange” has reached AVKeyValueStatusLoaded.
- [AVAssetTrackTrackAssociationsDidChangeNotification](./avassettracktrackassociationsdidchangenotification.md)
  Posted when the collection of track associations of an AVAssetTrack changes, but only for changes that occur after the status of the value of @“availableTrackAssociationTypes” has reached AVKeyValueStatusLoaded.
- [AVAssetWasDefragmentedNotification](./avassetwasdefragmentednotification.md)
  A notification the system posts when a fragmented asset minder observes that the system defragments the asset on disk.
- [AVFragmentedMovieContainsMovieFragmentsDidChangeNotification](./avfragmentedmoviecontainsmoviefragmentsdidchangenotification.md)
  Posted after the value of @“containsMovieFragments” has already been loaded and the AVFragmentedMovie is added to an AVFragmentedMovieMinder, either when 1) movie fragments are detected in the movie file on disk after it had previously contained none or when 2) no movie fragments are detected in the movie file on disk after it had previously contained one or more.
- [AVFragmentedMovieDurationDidChangeNotification](./avfragmentedmoviedurationdidchangenotification.md)
  Posted when the duration of an AVFragmentedMovie changes while it’s being minded by an AVFragmentedMovieMinder, but only for changes that occur after the status of the value of @“duration” has reached AVKeyValueStatusLoaded.
- [AVFragmentedMovieTrackSegmentsDidChangeNotification](./avfragmentedmovietracksegmentsdidchangenotification.md)
- [AVFragmentedMovieTrackTimeRangeDidChangeNotification](./avfragmentedmovietracktimerangedidchangenotification.md)
- [AVFragmentedMovieTrackTotalSampleDataLengthDidChangeNotification](./avfragmentedmovietracktotalsampledatalengthdidchangenotification.md)
- [AVFragmentedMovieWasDefragmentedNotification](./avfragmentedmoviewasdefragmentednotification.md)
  Posted when the movie file on disk is defragmented while an AVFragmentedMovie is being minded by an AVFragmentedMovieMinder, but only if the defragmentation occurs after the status of the value of @“canContainMovieFragments” has reached AVKeyValueStatusLoaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetchaptermetadatagroupsdidchangenotification)*