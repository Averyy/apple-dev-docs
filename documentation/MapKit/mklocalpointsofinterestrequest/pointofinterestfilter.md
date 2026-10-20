# pointOfInterestFilter

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A filter that lists points of interest categories to include or exclude.

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
@NSCopying
var pointOfInterestFilter: MKPointOfInterestFilter? { get set }
```

```objc
@property (nonatomic, copy, nullable) MKPointOfInterestFilter * pointOfInterestFilter;
```

## See Also

### Configuring the request parameters
- [var region: MKCoordinateRegion](./region.md)
  The region of the bounding box of the request provided or the derived bounding box of the circle created by the radius.
- [var coordinate: CLLocationCoordinate2D](./coordinate.md)
  The center of the point of request as latitude and longitude.
- [var radius: CLLocationDistance](./radius.md)
  The distance provided in meters or the longest distance derived from the center point to the region’s bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalpointsofinterestrequest/pointofinterestfilter)*