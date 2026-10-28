# title

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The title of the marker group.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var title: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * title;
```

## Discussion

You set a marker group’s title with the [`AVNavigationMarkersGroup`](../avnavigationmarkersgroup.md) initializer. Each marker group in the [`navigationMarkerGroups`](../../AVFoundation/avplayeritem/navigationmarkergroups.md) array of an [`AVPlayerItem`](../../AVFoundation/avplayeritem.md) object must have a unique title. To use the marker group as a chapter list, set its title to `nil`.

## See Also

### Inspecting navigation metadata
- [var timedNavigationMarkers: [AVTimedMetadataGroup]?](./timednavigationmarkers.md)
  The array of timed navigation markers for which the group provides navigation.
- [var dateRangeNavigationMarkers: [AVDateRangeMetadataGroup]?](./daterangenavigationmarkers.md)
  The array of date range navigation markers for which the group provides navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avnavigationmarkersgroup/title)*