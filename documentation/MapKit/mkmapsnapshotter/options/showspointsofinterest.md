# showsPointsOfInterest

**Framework**: MapKit  
**Kind**: property

A Boolean value that indicates whether the map displays point-of-interest information.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+

## Declaration

```swift
var showsPointsOfInterest: Bool { get set }
```

#### Discussion

When this property is set to [`true`](https://developer.apple.com/documentation/swift/true), the map displays icons and labels for restaurants, schools, and other relevant points of interest. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var preferredConfiguration: MKMapConfiguration](mkmapsnapshotter/options/preferredconfiguration.md)
  The map configuration style to use for snapshots.
- [var mapType: MKMapType](mkmapsnapshotter/options/maptype.md)
  The map’s visual style.
- [var showsBuildings: Bool](mkmapsnapshotter/options/showsbuildings.md)
  A Boolean that indicates whether the map displays extruded building information.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mkmapsnapshotter/options/pointofinterestfilter.md)
  The filter to use for determining the points of interest that appear in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/showspointsofinterest)*