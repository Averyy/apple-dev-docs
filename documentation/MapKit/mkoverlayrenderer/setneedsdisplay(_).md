# setNeedsDisplay(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Invalidates the specified portion of the overlay at all zoom scales.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func setNeedsDisplay(_ mapRect: MKMapRect)
```

```objc
- (void) setNeedsDisplayInMapRect:(MKMapRect) mapRect;
```

## Discussion

Marking a rectangle as invalid causes that portion of the overlay to be redrawn during the next update cycle. This method invalidates the overlay regardless of the current zoom scale associated with the map.

## Parameters

- `mapRect`: The portion of the overlay to update. Specify this value using a map coordinates.

## See Also

### Drawing the overlay
- [func canDraw(MKMapRect, zoomScale: MKZoomScale) -> Bool](./candraw%28_,zoomscale%29.md)
  Returns a Boolean value that indicates whether the overlay view is ready to draw its content.
- [func draw(MKMapRect, zoomScale: MKZoomScale, in: CGContext)](./draw%28_,zoomscale,in%29.md)
  Draws the overlay’s contents at the specified location on the map.
- [func setNeedsDisplay()](./setneedsdisplay%28%29.md)
  Invalidates the entire contents of the overlay for all zoom scales.
- [func setNeedsDisplay(MKMapRect, zoomScale: MKZoomScale)](./setneedsdisplay%28_,zoomscale%29.md)
  Invalidates the specified portion of the overlay, but only at the specified zoom scale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/setneedsdisplay(_:))*