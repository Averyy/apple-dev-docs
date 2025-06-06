# alpha

**Framework**: MapKit  
**Kind**: property

The amount of transparency to apply to the overlay.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var alpha: CGFloat { get set }
```

#### Discussion

The value in this property can be in the range `0.0` to `1.0`, where `0.0` represents total transparency and `1.0` represents total opacity. The default value of this property is `1.0`.

## See Also

- [var overlay: any MKOverlay](mkoverlayrenderer/overlay.md)
  The overlay object containing the data for drawing.
- [var contentScaleFactor: CGFloat](mkoverlayrenderer/contentscalefactor.md)
  The scale factor for drawing the overlay’s content.
- [var blendMode: CGBlendMode](mkoverlayrenderer/blendmode.md)
  The blend mode to apply to the overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/alpha)*