# init(minCenterCoordinateDistance:maxCenterCoordinateDistance:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Create a camera zoom range by specifying a minimum and maximum distance from your map view’s center coordinates, measured in meters.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init?(minCenterCoordinateDistance minDistance: CLLocationDistance, maxCenterCoordinateDistance maxDistance: CLLocationDistance)
```

```objc
- (instancetype) initWithMinCenterCoordinateDistance:(CLLocationDistance) minDistance maxCenterCoordinateDistance:(CLLocationDistance) maxDistance;
```

## Discussion

Specify the camera zoom range by providing the minimum and maximum distance values, in meters, from the center coordinate to constrain your map view’s zoom range.

To specify MapKit’s default minimum or maximum center coordinate distance, use the [`MKMapCameraZoomDefault`](../../mkmapcamerazoomdefault.md) constant, that allows the user to zoom to any level that MapKit supports.

The following example creates a zoom range that allows the map to zoom from 1000 – 3000 meters:

```swift
MKMapView.CameraZoomRange(
    minCenterCoordinateDistance: 1000,
    maxCenterCoordinateDistance: 3000
)
```

## Parameters

- `minDistance`: The minimum distance the user can zoom in on a map based on its center point, measured in meters.

  To increase how far in the user can zoom, use a shorter distance value. To decrease how far in the user can zoom, use a larger distance value.
- `maxDistance`: The maximum distance the user can zoom out on a map based on its center point, measured in meters.

  To increase how far out the user can zoom, use a larger distance value. To decrease how far out the user can zoom, use a smaller distance value.

## See Also

### Creating a camera zoom range
- [convenience init?(minCenterCoordinateDistance: CLLocationDistance)](./init%28mincentercoordinatedistance%29.md)
  Create a camera zoom range by specifying the minimum distance from your map view’s center coordinate, measured in meters.
- [convenience init?(maxCenterCoordinateDistance: CLLocationDistance)](./init%28maxcentercoordinatedistance%29.md)
  Create a camera zoom range by specifying the maximum distance from your map view’s center coordinate, measured in meters.
- [let MKMapCameraZoomDefault: CLLocationDistance](../../mkmapcamerazoomdefault.md)
  A constant value used to represent the default value for zooming in or out on a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/camerazoomrange-swift.class/init(mincentercoordinatedistance:maxcentercoordinatedistance:))*