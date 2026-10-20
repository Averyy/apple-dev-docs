# init(title:timedNavigationMarkers:)

**Framework**: AVKit  
**Kind**: init  
**Role**: Initializer

Initializes a navigation markers group with the specified title and array of timed navigation markers.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
init(title: String?, timedNavigationMarkers navigationMarkers: [AVTimedMetadataGroup])
```

```objc
- (instancetype) initWithTitle:(NSString *) title timedNavigationMarkers:(NSArray<AVTimedMetadataGroup *> *) navigationMarkers;
```

#### Return Value

A new navigation markers group.

#### Discussion

To associate marker groups with an asset for playback, use the [`navigationMarkerGroups`](../../AVFoundation/avplayeritem/navigationmarkergroups.md) property of an [`AVPlayerItem`](../../AVFoundation/avplayeritem.md) object.

To create a chapter list, pass `nil` for the `title` parameter and set the group as the first item in the player item’s [`navigationMarkerGroups`](../../AVFoundation/avplayeritem/navigationmarkergroups.md) array. To provide additional options for navigating media (such as a “Goals Scored” group for a recorded sporting event), provide a unique `title` value for each marker group in the array.

## Parameters

- `title`: The title to present for the markers group.
- `navigationMarkers`: The array of timed navigation markers for which the group provides navigation.

## See Also

### Creating a navigation marker group
- [init(title: String?, dateRangeNavigationMarkers: [AVDateRangeMetadataGroup])](./init%28title,daterangenavigationmarkers%29.md)
  Initializes a navigation markers group with the specified title and array of date range navigation markers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avnavigationmarkersgroup/init(title:timednavigationmarkers:))*