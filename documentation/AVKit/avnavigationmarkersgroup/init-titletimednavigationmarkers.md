# init(title:timedNavigationMarkers:)

**Framework**: AVKit  
**Kind**: init

Initializes a navigation markers group with the specified title and array of timed navigation markers.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
init(title: String?, timedNavigationMarkers navigationMarkers: [AVTimedMetadataGroup])
```

#### Return Value

A new navigation markers group.

#### Discussion

To associate marker groups with an asset for playback, use the [`navigationMarkerGroups`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/navigationMarkerGroups) property of an [`AVPlayerItem`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem) object.

To create a chapter list, pass `nil` for the `title` parameter and set the group as the first item in the player item’s [`navigationMarkerGroups`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/navigationMarkerGroups) array. To provide additional options for navigating media (such as a “Goals Scored” group for a recorded sporting event), provide a unique `title` value for each marker group in the array.

## Parameters

- `title`: The title to present for the markers group.
- `navigationMarkers`: The array of timed navigation markers for which the group provides navigation.

## See Also

- [init(title: String?, dateRangeNavigationMarkers: [AVDateRangeMetadataGroup])](avnavigationmarkersgroup/init(title:daterangenavigationmarkers:).md)
  Initializes a navigation markers group with the specified title and array of date range navigation markers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avnavigationmarkersgroup/init(title:timednavigationmarkers:))*