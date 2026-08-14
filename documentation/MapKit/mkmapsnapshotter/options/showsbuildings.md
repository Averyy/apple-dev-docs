# showsBuildings

**Framework**: MapKit  
**Kind**: property

A Boolean that indicates whether the map displays extruded building information.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var showsBuildings: Bool { get set }
```

#### Discussion

When you set this property to [`true`](https://developer.apple.com/documentation/swift/true) and the camera has a pitch angle greater than 0, the map extrudes buildings so that they appear to extend above the map plane, creating a 3D effect. You need to set the [`mapType`](mkmapsnapshotter/options/maptype.md) property must to [`MKMapType.standard`](mkmaptype/standard.md) for the map to display extruded buildings. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var preferredConfiguration: MKMapConfiguration](mkmapsnapshotter/options/preferredconfiguration.md)
  The map configuration style to use for snapshots.
- [var mapType: MKMapType](mkmapsnapshotter/options/maptype.md)
  The map’s visual style.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mkmapsnapshotter/options/pointofinterestfilter.md)
  The filter to use for determining the points of interest that appear in the snapshot.
- [var showsPointsOfInterest: Bool](mkmapsnapshotter/options/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/showsbuildings)*