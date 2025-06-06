# init(center:radius:)

**Framework**: MapKit  
**Kind**: init

Creates a circle with the center coordinate and radius you specify.

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
init(center coordinate: CLLocationCoordinate2D, radius: CLLocationDistance)
```

## Parameters

- `coordinate`: The location of the center of the circle.
- `radius`: The radius of the circle, in meters.

## See Also

- [init(MKCircle)](mapcircle/init(_:).md)
  Creates a circle overlay from an existing map circle object.
- [init(mapRect: MKMapRect)](mapcircle/init(maprect:).md)
  Creates the largest possible circle centered within the given map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcircle/init(center:radius:))*