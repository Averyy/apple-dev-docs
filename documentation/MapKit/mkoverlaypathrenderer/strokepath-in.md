# strokePath(_:in:)

**Framework**: MapKit  
**Kind**: method

Draws a line along the specified path.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func strokePath(_ path: CGPath, in context: CGContext)
```

#### Discussion

You must set the current stroke color before calling this method. Typically you do this by calling the [`applyStrokeProperties(to:atZoomScale:)`](mkoverlaypathrenderer/applystrokeproperties(to:atzoomscale:).md) method prior to drawing. If the [`strokeColor`](mkoverlaypathrenderer/strokecolor.md) property is currently `nil`, this method does nothing.

## Parameters

- `path`: The path to draw.
- `context`: The graphics context in which to draw the path.

## See Also

- [func applyStrokeProperties(to: CGContext, atZoomScale: MKZoomScale)](mkoverlaypathrenderer/applystrokeproperties(to:atzoomscale:).md)
  Applies the renderer’s stroke-related drawing properties to the specified graphics context.
- [func applyFillProperties(to: CGContext, atZoomScale: MKZoomScale)](mkoverlaypathrenderer/applyfillproperties(to:atzoomscale:).md)
  Applies the receiver’s fill-related drawing properties to the specified graphics context.
- [func fillPath(CGPath, in: CGContext)](mkoverlaypathrenderer/fillpath(_:in:).md)
  Fills the area that the specified path encloses.
- [var shouldRasterize: Bool](mkoverlaypathrenderer/shouldrasterize.md)
  A Boolean value that determines whether the overlay path renderer renders the overlay as a bitmap before compositing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/strokepath(_:in:))*