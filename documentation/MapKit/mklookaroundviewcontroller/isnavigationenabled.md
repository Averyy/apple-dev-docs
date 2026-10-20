# isNavigationEnabled

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the map’s navigation controls are visible.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var isNavigationEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isNavigationEnabled) BOOL navigationEnabled;
```

## See Also

### Customizing the LookAround display
- [var pointOfInterestFilter: MKPointOfInterestFilter?](./pointofinterestfilter.md)
  The filter used to determine the points of interest shown on the map.
- [var showsRoadLabels: Bool](./showsroadlabels.md)
  A Boolean value that indicates whether the map display road labels.
- [var badgePosition: MKLookAroundBadgePosition](./badgeposition.md)
  A value that indicates the badge’s position on the LookAround view.
- [enum MKLookAroundBadgePosition](../mklookaroundbadgeposition.md)
  Constants that control the position of badges on LookAround views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundviewcontroller/isnavigationenabled)*