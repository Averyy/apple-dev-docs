# init(centerCoordinateBounds:minimumDistance:maximumDistance:)

**Framework**: MapKit  
**Kind**: init

Creates a camera bounds with the specified map rectangle boundary and zoom ranges.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
init(centerCoordinateBounds: MKMapRect, minimumDistance: Double? = nil, maximumDistance: Double? = nil)
```

## Parameters

- `centerCoordinateBounds`: An   that specifies a boundary of an area that the map’s center needs to remain in.
- `minimumDistance`: The minimum distance someone can zoom in on a map based on its center point, measured in meters.
- `maximumDistance`: The maximum distance the user can zoom out on a map based on its center point, measured in meters.

## See Also

- [init(centerCoordinateBounds: MKCoordinateRegion, minimumDistance: Double?, maximumDistance: Double?)](mapcamerabounds/init(centercoordinatebounds:minimumdistance:maximumdistance:)-97kis.md)
  Creates a camera bounds with the specified region boundary and zoom ranges.
- [init(minimumDistance: Double?, maximumDistance: Double?)](mapcamerabounds/init(minimumdistance:maximumdistance:).md)
  Creates a camera bounds with the zoom ranges you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcamerabounds/init(centercoordinatebounds:minimumdistance:maximumdistance:)-27z4p)*