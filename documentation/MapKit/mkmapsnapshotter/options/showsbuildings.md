# showsBuildings

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the map displays extruded building information.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.9+ - Deprecated in 27.2
- tvOS 9.2+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: MapKit no longer supports this option.

## Declaration

```swift
var showsBuildings: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsBuildings;
```

## Discussion

When you set this property to [`true`](../../../Swift/true.md) and the camera has a pitch angle greater than 0, the map extrudes buildings so that they appear to extend above the map plane, creating a 3D effect. You need to set the [`mapType`](./maptype.md) property must to [`MKMapType.standard`](../../mkmaptype/standard.md) for the map to display extruded buildings. The default value of this property is [`true`](../../../Swift/true.md).

## See Also

### Configuring the map data
- [var preferredConfiguration: MKMapConfiguration](./preferredconfiguration.md)
  The map configuration style to use for snapshots.
- [var mapType: MKMapType](./maptype.md)
  The map’s visual style.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](./pointofinterestfilter.md)
  The filter to use for determining the points of interest that appear in the snapshot.
- [var showsPointsOfInterest: Bool](./showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/showsbuildings)*