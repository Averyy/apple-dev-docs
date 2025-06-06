# init(maxCenterCoordinateDistance:)

**Framework**: MapKit  
**Kind**: init

Create a camera zoom range by specifying the maximum distance from your map view’s center coordinate, measured in meters.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(maxCenterCoordinateDistance maxDistance: CLLocationDistance)
```

#### Discussion

The constant, [`MKMapCameraZoomDefault`](mkmapcamerazoomdefault.md), specifies the default distance for [`maxCenterCoordinateDistance`](mkmapview/camerazoomrange-swift.class/maxcentercoordinatedistance.md).

## Parameters

- `maxDistance`: To increase how far out the user can zoom, use a larger distance value. To decrease how far out the user can zoom, use a smaller distance value.

## See Also

- [init?(minCenterCoordinateDistance: CLLocationDistance, maxCenterCoordinateDistance: CLLocationDistance)](mkmapview/camerazoomrange-swift.class/init(mincentercoordinatedistance:maxcentercoordinatedistance:).md)
  Create a camera zoom range by specifying a minimum and maximum distance from your map view’s center coordinates, measured in meters.
- [convenience init?(minCenterCoordinateDistance: CLLocationDistance)](mkmapview/camerazoomrange-swift.class/init(mincentercoordinatedistance:).md)
  Create a camera zoom range by specifying the minimum distance from your map view’s center coordinate, measured in meters.
- [let MKMapCameraZoomDefault: CLLocationDistance](mkmapcamerazoomdefault.md)
  A constant value used to represent the default value for zooming in or out on a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/camerazoomrange-swift.class/init(maxcentercoordinatedistance:))*