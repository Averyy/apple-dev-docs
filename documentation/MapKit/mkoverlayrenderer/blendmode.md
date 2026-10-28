# blendMode

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The blend mode to apply to the overlay.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var blendMode: CGBlendMode { get set }
```

```objc
@property (nonatomic, assign) CGBlendMode blendMode;
```

## Discussion

Choose the blend mode from one of the possible [`CGBlendMode`](../../CoreGraphics/cgblendmode.md) enumerations.

## See Also

### Attributes of the overlay
- [var overlay: any MKOverlay](./overlay.md)
  The overlay object containing the data for drawing.
- [var alpha: CGFloat](./alpha.md)
  The amount of transparency to apply to the overlay.
- [var contentScaleFactor: CGFloat](./contentscalefactor.md)
  The scale factor for drawing the overlay’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/blendmode)*