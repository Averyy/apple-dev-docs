# title

**Framework**: AVKit  
**Kind**: property

The title of the marker group.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var title: String? { get }
```

#### Discussion

You set a marker group’s title with the [`AVNavigationMarkersGroup`](avnavigationmarkersgroup.md) initializer. Each marker group in the [`navigationMarkerGroups`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/navigationMarkerGroups) array of an [`AVPlayerItem`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem) object must have a unique title. To use the marker group as a chapter list, set its title to `nil`.

## See Also

- [var timedNavigationMarkers: [AVTimedMetadataGroup]?](avnavigationmarkersgroup/timednavigationmarkers.md)
  The array of timed navigation markers for which the group provides navigation.
- [var dateRangeNavigationMarkers: [AVDateRangeMetadataGroup]?](avnavigationmarkersgroup/daterangenavigationmarkers.md)
  The array of date range navigation markers for which the group provides navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avnavigationmarkersgroup/title)*