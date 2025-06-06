# setNeedsDisplay(_:zoomScale:)

**Framework**: MapKit  
**Kind**: method

Invalidates the specified portion of the overlay, but only at the specified zoom scale.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func setNeedsDisplay(_ mapRect: MKMapRect, zoomScale: MKZoomScale)
```

#### Discussion

Marking a rectangle as invalid causes that portion of the overlay to be redrawn during the next update cycle. This method invalidates the overlay only at the specified zoom scale.

## Parameters

- `mapRect`: The portion of the overlay to update. Specify this value using a map coordinates.
- `zoomScale`: The zoom scale for which you want to invalidate the overlay.

## See Also

- [func canDraw(MKMapRect, zoomScale: MKZoomScale) -> Bool](mkoverlayrenderer/candraw(_:zoomscale:).md)
  Returns a Boolean value that indicates whether the overlay view is ready to draw its content.
- [func draw(MKMapRect, zoomScale: MKZoomScale, in: CGContext)](mkoverlayrenderer/draw(_:zoomscale:in:).md)
  Draws the overlay’s contents at the specified location on the map.
- [func setNeedsDisplay()](mkoverlayrenderer/setneedsdisplay.md)
  Invalidates the entire contents of the overlay for all zoom scales.
- [func setNeedsDisplay(MKMapRect)](mkoverlayrenderer/setneedsdisplay(_:).md)
  Invalidates the specified portion of the overlay at all zoom scales.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/setneedsdisplay(_:zoomscale:))*