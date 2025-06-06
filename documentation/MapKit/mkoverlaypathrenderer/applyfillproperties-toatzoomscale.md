# applyFillProperties(to:atZoomScale:)

**Framework**: MapKit  
**Kind**: method

Applies the receiver’s fill-related drawing properties to the specified graphics context.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func applyFillProperties(to context: CGContext, atZoomScale zoomScale: MKZoomScale)
```

#### Discussion

This is a convenience method for applying all of the drawing properties used when filling a path. This method applies the current fill color to the specified graphics context.

## Parameters

- `context`: The graphics context used to draw the view’s contents.
- `zoomScale`: The current zoom scale used for drawing.

## See Also

- [func applyStrokeProperties(to: CGContext, atZoomScale: MKZoomScale)](mkoverlaypathrenderer/applystrokeproperties(to:atzoomscale:).md)
  Applies the renderer’s stroke-related drawing properties to the specified graphics context.
- [func strokePath(CGPath, in: CGContext)](mkoverlaypathrenderer/strokepath(_:in:).md)
  Draws a line along the specified path.
- [func fillPath(CGPath, in: CGContext)](mkoverlaypathrenderer/fillpath(_:in:).md)
  Fills the area that the specified path encloses.
- [var shouldRasterize: Bool](mkoverlaypathrenderer/shouldrasterize.md)
  A Boolean value that determines whether the overlay path renderer renders the overlay as a bitmap before compositing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/applyfillproperties(to:atzoomscale:))*