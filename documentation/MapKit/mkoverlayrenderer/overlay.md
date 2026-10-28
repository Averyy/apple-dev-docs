# overlay

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The overlay object containing the data for drawing.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var overlay: any MKOverlay { get }
```

```objc
@property (nonatomic, readonly) id<MKOverlay> overlay;
```

## Discussion

The overlay object contains the coordinate at which to draw the overlay and other information that your app provides.

## See Also

### Attributes of the overlay
- [var alpha: CGFloat](./alpha.md)
  The amount of transparency to apply to the overlay.
- [var contentScaleFactor: CGFloat](./contentscalefactor.md)
  The scale factor for drawing the overlay’s content.
- [var blendMode: CGBlendMode](./blendmode.md)
  The blend mode to apply to the overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/overlay)*