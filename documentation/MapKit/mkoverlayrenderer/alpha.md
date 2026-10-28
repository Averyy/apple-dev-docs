# alpha

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (atomic) CGFloat alpha;
```

## Discussion

The value in this property can be in the range `0.0` to `1.0`, where `0.0` represents total transparency and `1.0` represents total opacity. The default value of this property is `1.0`.

## See Also

### Attributes of the overlay
- [var overlay: any MKOverlay](./overlay.md)
  The overlay object containing the data for drawing.
- [var contentScaleFactor: CGFloat](./contentscalefactor.md)
  The scale factor for drawing the overlay’s content.
- [var blendMode: CGBlendMode](./blendmode.md)
  The blend mode to apply to the overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/alpha)*