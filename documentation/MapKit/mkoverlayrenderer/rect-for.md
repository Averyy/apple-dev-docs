# rect(for:)

**Framework**: MapKit  
**Kind**: method

Returns the rectangle in the overlay renderer’s drawing area corresponding to the specified rectangle on the map.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func rect(for mapRect: MKMapRect) -> CGRect
```

#### Return Value

The rectangle in the overlay’s drawing area that corresponds to the map rectangle.

#### Discussion

You may call this method safely from your view’s [`draw(_:zoomScale:in:)`](mkoverlayrenderer/draw(_:zoomscale:in:).md) method.

## Parameters

- `mapRect`: A rectangle on the two-dimensional map projection.

## See Also

- [func point(for: MKMapPoint) -> CGPoint](mkoverlayrenderer/point(for:).md)
  Returns the point in the overlay renderer’s drawing area corresponding to the specified point on the map.
- [func mapPoint(for: CGPoint) -> MKMapPoint](mkoverlayrenderer/mappoint(for:).md)
  Returns the point on the map that corresponds to the specified point in the overlay renderer’s drawing area.
- [func mapRect(for: CGRect) -> MKMapRect](mkoverlayrenderer/maprect(for:).md)
  Returns the rectangle on the map that corresponds to the specified rectangle in the overlay renderer’s drawing area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/rect(for:))*