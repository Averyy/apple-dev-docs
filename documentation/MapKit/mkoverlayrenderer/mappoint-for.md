# mapPoint(for:)

**Framework**: MapKit  
**Kind**: method

Returns the point on the map that corresponds to the specified point in the overlay renderer’s drawing area.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func mapPoint(for point: CGPoint) -> MKMapPoint
```

#### Return Value

The point on the two-dimensional map projection corresponding to the specified point.

#### Discussion

You may call this method safely from your view’s [`draw(_:zoomScale:in:)`](mkoverlayrenderer/draw(_:zoomscale:in:).md) method.

## Parameters

- `point`: The point in the overlay’s drawing area that you want to convert.

## See Also

- [func point(for: MKMapPoint) -> CGPoint](mkoverlayrenderer/point(for:).md)
  Returns the point in the overlay renderer’s drawing area corresponding to the specified point on the map.
- [func rect(for: MKMapRect) -> CGRect](mkoverlayrenderer/rect(for:).md)
  Returns the rectangle in the overlay renderer’s drawing area corresponding to the specified rectangle on the map.
- [func mapRect(for: CGRect) -> MKMapRect](mkoverlayrenderer/maprect(for:).md)
  Returns the rectangle on the map that corresponds to the specified rectangle in the overlay renderer’s drawing area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/mappoint(for:))*