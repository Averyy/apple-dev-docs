# timedNavigationMarkers

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The array of timed navigation markers for which the group provides navigation.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var timedNavigationMarkers: [AVTimedMetadataGroup]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<AVTimedMetadataGroup *> * timedNavigationMarkers;
```

## Discussion

Returns the array of [`AVTimedMetadataGroup`](../../AVFoundation/avtimedmetadatagroup.md) objects managed by this group. This value may be `nil`.

## See Also

### Inspecting navigation metadata
- [var title: String?](./title.md)
  The title of the marker group.
- [var dateRangeNavigationMarkers: [AVDateRangeMetadataGroup]?](./daterangenavigationmarkers.md)
  The array of date range navigation markers for which the group provides navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avnavigationmarkersgroup/timednavigationmarkers)*