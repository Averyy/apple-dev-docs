# rectForMapRect:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle in the overlay view that corresponds to the specified rectangle on the map.

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use an [`MKOverlayRenderer`](../mkoverlayrenderer.md) object instead.

## Declaration

```objc
- (CGRect) rectForMapRect:(MKMapRect) mapRect;
```

#### Return Value

The rectangle specified in the receiver’s coordinate system.

#### Discussion

Because the bounds and frame rectangles of an overlay view do not change after the view has been created, you may call this method from multiple threads simultaneously. Therefore, you may call this method safely from your view’s [`drawMapRect:zoomScale:inContext:`](./drawmaprect_zoomscale_incontext_.md) method.

## Parameters

- `mapRect`: A rectangle on the two-dimensional map projection.

## See Also

### Converting points on the map
- [- pointForMapPoint:](./pointformappoint_.md)
  Returns the point in the overlay view that corresponds to specified point on the map.
- [- mapPointForPoint:](./mappointforpoint_.md)
  Returns the map point that corresponds to the specified point in the overlay view.
- [- mapRectForRect:](./maprectforrect_.md)
  Returns the map rectangle that corresponds to the rectangle in the overlay view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayview/rectformaprect:)*