# point(for:)

**Framework**: MapKit  
**Kind**: method

Returns the point in the overlay renderer’s drawing area corresponding to the specified point on the map.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func point(for mapPoint: MKMapPoint) -> CGPoint
```

#### Return Value

The point in the overlay’s drawing area that corresponds to the map point.

#### Discussion

You may call this method safely from your view’s [`draw(_:zoomScale:in:)`](mkoverlayrenderer/draw(_:zoomscale:in:).md) method.

## Parameters

- `mapPoint`: A point on the two-dimensional map projection. If you have a coordinate value (latitude and longitude), you can use the   function to convert that coordinate to a map point.

## See Also

- [func mapPoint(for: CGPoint) -> MKMapPoint](mkoverlayrenderer/mappoint(for:).md)
  Returns the point on the map that corresponds to the specified point in the overlay renderer’s drawing area.
- [func rect(for: MKMapRect) -> CGRect](mkoverlayrenderer/rect(for:).md)
  Returns the rectangle in the overlay renderer’s drawing area corresponding to the specified rectangle on the map.
- [func mapRect(for: CGRect) -> MKMapRect](mkoverlayrenderer/maprect(for:).md)
  Returns the rectangle on the map that corresponds to the specified rectangle in the overlay renderer’s drawing area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/point(for:))*