# fogColor

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The color of the fog effect to be rendered with the scene. Animatable.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var fogColor: Any { get set }
```

```objc
@property (nonatomic, retain) id fogColor;
```

#### Discussion

This property’s value can be an [`NSColor`](../../AppKit/nscolor.md) object (in macOS), a [`UIColor`](../../UIKit/uicolor.md) object (in iOS), or a [`CGColor`](../../CoreGraphics/cgcolor.md) object. The default fog color is white.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adding Fog to a Scene
- [var fogStartDistance: CGFloat](./fogstartdistance.md)
  The distance from a point of view at which the scene’s contents begin to be obscured by fog. Animatable.
- [var fogEndDistance: CGFloat](./fogenddistance.md)
  The distance from a point of view at which the scene’s contents are completely obscured by fog. Animatable.
- [var fogDensityExponent: CGFloat](./fogdensityexponent.md)
  The transition curve for the fog’s intensity between its start and end distances. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/fogcolor)*