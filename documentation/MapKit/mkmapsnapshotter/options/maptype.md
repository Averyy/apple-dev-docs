# mapType

**Framework**: MapKit  
**Kind**: property

The map’s visual style.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var mapType: MKMapType { get set }
```

#### Discussion

The default value of this property is [`MKMapType.standard`](mkmaptype/standard.md).

## See Also

- [var preferredConfiguration: MKMapConfiguration](mkmapsnapshotter/options/preferredconfiguration.md)
  The map configuration style to use for snapshots.
- [var showsBuildings: Bool](mkmapsnapshotter/options/showsbuildings.md)
  A Boolean that indicates whether the map displays extruded building information.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mkmapsnapshotter/options/pointofinterestfilter.md)
  The filter to use for determining the points of interest that appear in the snapshot.
- [var showsPointsOfInterest: Bool](mkmapsnapshotter/options/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/maptype)*