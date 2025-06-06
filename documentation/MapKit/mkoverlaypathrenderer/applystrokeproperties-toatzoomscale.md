# applyStrokeProperties(to:atZoomScale:)

**Framework**: MapKit  
**Kind**: method

Applies the renderer’s stroke-related drawing properties to the specified graphics context.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func applyStrokeProperties(to context: CGContext, atZoomScale zoomScale: MKZoomScale)
```

#### Discussion

This is a convenience method for applying all of the drawing properties MapKit uses when stroking a path. This method applies the stroke color, line width, line join, line cap, miter limit, line dash phase, and line dash attributes to the specified graphics context. This method applies the scale factor in the `zoomScale` parameter to the line width and line dash pattern automatically so that lines scale appropriately.

This method doesn’t save the current graphics state before applying the new attributes. If you want to preserve the existing state, save it and restore it later when you finish drawing.

## Parameters

- `context`: The graphics context for drawing the view’s contents.
- `zoomScale`: The zoom scale for drawing.

## See Also

- [func applyFillProperties(to: CGContext, atZoomScale: MKZoomScale)](mkoverlaypathrenderer/applyfillproperties(to:atzoomscale:).md)
  Applies the receiver’s fill-related drawing properties to the specified graphics context.
- [func strokePath(CGPath, in: CGContext)](mkoverlaypathrenderer/strokepath(_:in:).md)
  Draws a line along the specified path.
- [func fillPath(CGPath, in: CGContext)](mkoverlaypathrenderer/fillpath(_:in:).md)
  Fills the area that the specified path encloses.
- [var shouldRasterize: Bool](mkoverlaypathrenderer/shouldrasterize.md)
  A Boolean value that determines whether the overlay path renderer renders the overlay as a bitmap before compositing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/applystrokeproperties(to:atzoomscale:))*