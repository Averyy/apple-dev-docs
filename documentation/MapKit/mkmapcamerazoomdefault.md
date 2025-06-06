# MKMapCameraZoomDefault

**Framework**: MapKit  
**Kind**: var

A constant value used to represent the default value for zooming in or out on a map.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
let MKMapCameraZoomDefault: CLLocationDistance
```

#### Discussion

Use [`MKMapCameraZoomDefault`](mkmapcamerazoomdefault.md) for the minimum or maximum zoom range when you create an instance of [`MKMapView.CameraZoomRange`](mkmapview/camerazoomrange-swift.class.md) to allow the user to zoom to any level that MapKit supports.

## See Also

- [init?(minCenterCoordinateDistance: CLLocationDistance, maxCenterCoordinateDistance: CLLocationDistance)](mkmapview/camerazoomrange-swift.class/init(mincentercoordinatedistance:maxcentercoordinatedistance:).md)
  Create a camera zoom range by specifying a minimum and maximum distance from your map view’s center coordinates, measured in meters.
- [convenience init?(minCenterCoordinateDistance: CLLocationDistance)](mkmapview/camerazoomrange-swift.class/init(mincentercoordinatedistance:).md)
  Create a camera zoom range by specifying the minimum distance from your map view’s center coordinate, measured in meters.
- [convenience init?(maxCenterCoordinateDistance: CLLocationDistance)](mkmapview/camerazoomrange-swift.class/init(maxcentercoordinatedistance:).md)
  Create a camera zoom range by specifying the maximum distance from your map view’s center coordinate, measured in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapcamerazoomdefault)*