# contentScaleFactor

**Framework**: MapKit  
**Kind**: property

The scale factor for drawing the overlay’s content.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var contentScaleFactor: CGFloat { get }
```

#### Discussion

The scale factor determines how the overlay renders map content from the logical coordinate space (in points) to the device coordinate space (in pixels). This value is typically either `1.0` or `2.0`. Higher scale factors indicate that each point represents more than one pixel on the screen. For example, if the scale factor is `2.0` and the drawing rectangle size is 50 x 50 points, the size of the underlying area is 100 x 100 pixels.

When drawing the content for your overlays, you can use this value to determine how best to render your content.

## See Also

- [var overlay: any MKOverlay](mkoverlayrenderer/overlay.md)
  The overlay object containing the data for drawing.
- [var alpha: CGFloat](mkoverlayrenderer/alpha.md)
  The amount of transparency to apply to the overlay.
- [var blendMode: CGBlendMode](mkoverlayrenderer/blendmode.md)
  The blend mode to apply to the overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/contentscalefactor)*