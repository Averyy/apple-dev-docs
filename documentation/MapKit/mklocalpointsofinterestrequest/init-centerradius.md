# init(center:radius:)

**Framework**: MapKit  
**Kind**: init

Creates a points of interest search request centered on the provided coordinate with the provided radius.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(center coordinate: CLLocationCoordinate2D, radius: CLLocationDistance)
```

## Parameters

- `coordinate`: The center point of a circular region to search.
- `radius`: The radius of the region to search in meters.

## See Also

- [init(coordinateRegion: MKCoordinateRegion)](mklocalpointsofinterestrequest/init(coordinateregion:).md)
  Creates a points of interest search request based on existing region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalpointsofinterestrequest/init(center:radius:))*