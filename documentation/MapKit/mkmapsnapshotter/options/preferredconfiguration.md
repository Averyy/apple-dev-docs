# preferredConfiguration

**Framework**: MapKit  
**Kind**: property

The map configuration style to use for snapshots.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var preferredConfiguration: MKMapConfiguration { get set }
```

#### Discussion

Set this property to one of the [`MKMapConfiguration`](mkmapconfiguration.md) subclasses to configure the map style to use when making map snapshots.

## See Also

- [var mapType: MKMapType](mkmapsnapshotter/options/maptype.md)
  The map’s visual style.
- [var showsBuildings: Bool](mkmapsnapshotter/options/showsbuildings.md)
  A Boolean that indicates whether the map displays extruded building information.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mkmapsnapshotter/options/pointofinterestfilter.md)
  The filter to use for determining the points of interest that appear in the snapshot.
- [var showsPointsOfInterest: Bool](mkmapsnapshotter/options/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/preferredconfiguration)*