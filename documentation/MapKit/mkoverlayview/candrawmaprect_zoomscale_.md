# canDrawMapRect:zoomScale:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the overlay view is ready to draw its content.

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use an [`MKOverlayRenderer`](../mkoverlayrenderer.md) object instead.

## Declaration

```objc
- (BOOL) canDrawMapRect:(MKMapRect) mapRect zoomScale:(MKZoomScale) zoomScale;
```

#### Return Value

[`true`](../../Swift/true.md) if this view is ready to draw its contents or [`false`](../../Swift/false.md) if it is not.

#### Discussion

Overlay views can override this method in situations where they may depend on the availability of other information to draw their contents. For example, an overlay view showing traffic information might want to delay drawing until it has all of the traffic data it needs. In such a case, it can return [`false`](../../Swift/false.md) from this method to indicate that it is not ready.

If you return [`false`](../../Swift/false.md) from this method, your application is responsible for calling the [`setNeedsDisplayInMapRect:zoomScale:`](./setneedsdisplayinmaprect_zoomscale_.md) method when the overlay view subsequently becomes ready to draw its contents.

The default implementation of this method returns [`true`](../../Swift/true.md).

## Parameters

- `mapRect`: The map rectangle that needs to be updated.
- `zoomScale`: The current scale factor applied to the map.

## See Also

### Drawing the overlay
- [- drawMapRect:zoomScale:inContext:](./drawmaprect_zoomscale_incontext_.md)
  Draws the contents of the overlay view.
- [- setNeedsDisplayInMapRect:](./setneedsdisplayinmaprect_.md)
  Invalidates the view in the given map rectangle at all zoom scales.
- [- setNeedsDisplayInMapRect:zoomScale:](./setneedsdisplayinmaprect_zoomscale_.md)
  Invalidates the view in the given map rectangle but only at the specified zoom scale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayview/candrawmaprect:zoomscale:)*