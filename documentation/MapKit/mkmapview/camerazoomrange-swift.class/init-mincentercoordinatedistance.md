# init(minCenterCoordinateDistance:)

**Framework**: MapKit  
**Kind**: init

Create a camera zoom range by specifying the minimum distance from your map view’s center coordinate, measured in meters.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(minCenterCoordinateDistance minDistance: CLLocationDistance)
```

#### Discussion

To specify MapKit’s default minimum distance from the center coordinate, use the [`MKMapCameraZoomDefault`](mkmapcamerazoomdefault.md) constant, that allows the user to zoom to any level that MapKit supports.

The following example prevents the user from zooming closer than 1000 meters from the map’s center coordinate:

```swift
MKMapView.CameraZoomRange(
    minCenterCoordinateDistance: 1000
)
```

## Parameters

- `minDistance`: To increase how far in the user can zoom, use a shorter distance value. To decrease how far in the user can zoom, use a larger distance value.

## See Also

- [init?(minCenterCoordinateDistance: CLLocationDistance, maxCenterCoordinateDistance: CLLocationDistance)](mkmapview/camerazoomrange-swift.class/init(mincentercoordinatedistance:maxcentercoordinatedistance:).md)
  Create a camera zoom range by specifying a minimum and maximum distance from your map view’s center coordinates, measured in meters.
- [convenience init?(maxCenterCoordinateDistance: CLLocationDistance)](mkmapview/camerazoomrange-swift.class/init(maxcentercoordinatedistance:).md)
  Create a camera zoom range by specifying the maximum distance from your map view’s center coordinate, measured in meters.
- [let MKMapCameraZoomDefault: CLLocationDistance](mkmapcamerazoomdefault.md)
  A constant value used to represent the default value for zooming in or out on a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/camerazoomrange-swift.class/init(mincentercoordinatedistance:))*