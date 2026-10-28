# canDraw(_:zoomScale:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the overlay view is ready to draw its content.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func canDraw(_ mapRect: MKMapRect, zoomScale: MKZoomScale) -> Bool
```

```objc
- (BOOL) canDrawMapRect:(MKMapRect) mapRect zoomScale:(MKZoomScale) zoomScale;
```

## Return Value

[`true`](../../Swift/true.md) if this overlay renderer is ready to draw its contents on the map or [`false`](../../Swift/false.md) if it is not.

## Discussion

Overlay renderers can override this method in situations where they may depend on the availability of other information to draw their contents. For example, a renderer showing traffic information might want to delay drawing until it has all of the traffic data it needs. In such a case, it can return [`false`](../../Swift/false.md) from this method to indicate that it’s not ready. An overlay renderer might also return [`false`](../../Swift/false.md) if it doesn’t draw content in the specified rectangle.

If you return [`false`](../../Swift/false.md) from this method, your application is responsible for calling the [`setNeedsDisplay(_:zoomScale:)`](./setneedsdisplay%28_,zoomscale%29.md) method when the overlay renderer subsequently becomes ready to draw its contents.

The default implementation of this method returns [`true`](../../Swift/true.md).

## Parameters

- `mapRect`: The map rectangle that the renderer needs to update.
- `zoomScale`: The current scale factor applied to the map.

## See Also

### Drawing the overlay
- [func draw(MKMapRect, zoomScale: MKZoomScale, in: CGContext)](./draw%28_,zoomscale,in%29.md)
  Draws the overlay’s contents at the specified location on the map.
- [func setNeedsDisplay()](./setneedsdisplay%28%29.md)
  Invalidates the entire contents of the overlay for all zoom scales.
- [func setNeedsDisplay(MKMapRect)](./setneedsdisplay%28_%29.md)
  Invalidates the specified portion of the overlay at all zoom scales.
- [func setNeedsDisplay(MKMapRect, zoomScale: MKZoomScale)](./setneedsdisplay%28_,zoomscale%29.md)
  Invalidates the specified portion of the overlay, but only at the specified zoom scale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/candraw(_:zoomscale:))*