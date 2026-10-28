# mapPoint(for:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (MKMapPoint) mapPointForPoint:(CGPoint) point;
```

## Return Value

The point on the two-dimensional map projection corresponding to the specified point.

## Discussion

You may call this method safely from your view’s [`draw(_:zoomScale:in:)`](./draw%28_,zoomscale,in%29.md) method.

## Parameters

- `point`: The point in the overlay’s drawing area that you want to convert.

## See Also

### Converting points on the map
- [func point(for: MKMapPoint) -> CGPoint](./point%28for%29.md)
  Returns the point in the overlay renderer’s drawing area corresponding to the specified point on the map.
- [func rect(for: MKMapRect) -> CGRect](./rect%28for%29.md)
  Returns the rectangle in the overlay renderer’s drawing area corresponding to the specified rectangle on the map.
- [func mapRect(for: CGRect) -> MKMapRect](./maprect%28for%29.md)
  Returns the rectangle on the map that corresponds to the specified rectangle in the overlay renderer’s drawing area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/mappoint(for:))*