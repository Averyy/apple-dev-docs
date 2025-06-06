# init(mapRect:)

**Framework**: MapKit  
**Kind**: init

Creates and returns a circle object that derives the circular area from the specified rectangle.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
convenience init(mapRect: MKMapRect)
```

#### Return Value

A circle overlay object.

## Parameters

- `mapRect`: The map rectangle that determines the circular area. The initializer uses the center point of the rectangle as the center point of the circle. If the rectangle isn’t a square, the method uses the longest side of the rectangle to define the radius of the resulting circle.

## See Also

- [convenience init(center: CLLocationCoordinate2D, radius: CLLocationDistance)](mkcircle/init(center:radius:).md)
  Creates and returns a circle object using the specified coordinate and radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcircle/init(maprect:))*