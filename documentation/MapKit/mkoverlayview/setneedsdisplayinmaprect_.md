# setNeedsDisplayInMapRect:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Invalidates the view in the given map rectangle at all zoom scales.

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use an [`MKOverlayRenderer`](../mkoverlayrenderer.md) object instead.

## Declaration

```objc
- (void) setNeedsDisplayInMapRect:(MKMapRect) mapRect;
```

#### Discussion

Marking a rectangle as invalid causes that portion of the view to be redrawn during the next update cycle. This method invalidates the overlay regardless of the current zoom scale associated with the map.

## Parameters

- `mapRect`: The portion of the overlay that needs to be updated. This value is specified using a map rectangle and not view coordinates. You can convert from a view rectangle to a map rectangle using the [`mapRectForRect:`](./maprectforrect_.md) method.

## See Also

### Drawing the overlay
- [- canDrawMapRect:zoomScale:](./candrawmaprect_zoomscale_.md)
  Returns a Boolean value indicating whether the overlay view is ready to draw its content.
- [- drawMapRect:zoomScale:inContext:](./drawmaprect_zoomscale_incontext_.md)
  Draws the contents of the overlay view.
- [- setNeedsDisplayInMapRect:zoomScale:](./setneedsdisplayinmaprect_zoomscale_.md)
  Invalidates the view in the given map rectangle but only at the specified zoom scale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayview/setneedsdisplayinmaprect:)*