# shouldRasterize

**Framework**: MapKit  
**Kind**: property

A Boolean value that determines whether the overlay path renderer renders the overlay as a bitmap before compositing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var shouldRasterize: Bool { get set }
```

#### Discussion

The default value is `false`.

Whenever possible, MapKit vectorizes overlay shapes by default so that they scale along with the map and remain sharp. In some cases, you may want to force the rasterization of an overlay and not vectorize it. Set this variable to `true` to force the overlay path renderer to render the overlay as a bitmap.

## See Also

- [func applyStrokeProperties(to: CGContext, atZoomScale: MKZoomScale)](mkoverlaypathrenderer/applystrokeproperties(to:atzoomscale:).md)
  Applies the renderer’s stroke-related drawing properties to the specified graphics context.
- [func applyFillProperties(to: CGContext, atZoomScale: MKZoomScale)](mkoverlaypathrenderer/applyfillproperties(to:atzoomscale:).md)
  Applies the receiver’s fill-related drawing properties to the specified graphics context.
- [func strokePath(CGPath, in: CGContext)](mkoverlaypathrenderer/strokepath(_:in:).md)
  Draws a line along the specified path.
- [func fillPath(CGPath, in: CGContext)](mkoverlaypathrenderer/fillpath(_:in:).md)
  Fills the area that the specified path encloses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/shouldrasterize)*