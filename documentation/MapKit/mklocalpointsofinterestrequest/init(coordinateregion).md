# init(coordinateRegion:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a points of interest search request based on existing region.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(coordinateRegion region: MKCoordinateRegion)
```

```objc
- (instancetype) initWithCoordinateRegion:(MKCoordinateRegion) region;
```

## Parameters

- `region`: The region to search.

## See Also

### Creating a point of interest request
- [init(center: CLLocationCoordinate2D, radius: CLLocationDistance)](./init%28center,radius%29.md)
  Creates a points of interest search request centered on the provided coordinate with the provided radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalpointsofinterestrequest/init(coordinateregion:))*