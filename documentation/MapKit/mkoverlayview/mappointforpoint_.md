# mapPointForPoint:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns the map point that corresponds to the specified point in the overlay view.

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use an [`MKOverlayRenderer`](../mkoverlayrenderer.md) object instead.

## Declaration

```objc
- (MKMapPoint) mapPointForPoint:(CGPoint) point;
```

## Return Value

The point on the two-dimensional map projection corresponding to the specified point.

## Discussion

Because the bounds and frame rectangles of an overlay view do not change after the view has been created, you may call this method from multiple threads simultaneously. Therefore, you may call this method safely from your view’s [`drawMapRect:zoomScale:inContext:`](./drawmaprect_zoomscale_incontext_.md) method.

## Parameters

- `point`: The point in the view’s coordinate system that you want to convert.

## See Also

### Converting points on the map
- [- pointForMapPoint:](./pointformappoint_.md)
  Returns the point in the overlay view that corresponds to specified point on the map.
- [- rectForMapRect:](./rectformaprect_.md)
  Returns the rectangle in the overlay view that corresponds to the specified rectangle on the map.
- [- mapRectForRect:](./maprectforrect_.md)
  Returns the map rectangle that corresponds to the rectangle in the overlay view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayview/mappointforpoint:)*