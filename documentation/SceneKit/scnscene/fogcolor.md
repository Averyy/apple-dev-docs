# fogColor

**Framework**: SceneKit  
**Kind**: property

The color of the fog effect to be rendered with the scene. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var fogColor: Any { get set }
```

#### Discussion

This property’s value can be an [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor) object (in macOS), a [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) object (in iOS), or a [`CGColor`](https://developer.apple.com/documentation/CoreGraphics/CGColor) object. The default fog color is white.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var fogStartDistance: CGFloat](scnscene/fogstartdistance.md)
  The distance from a point of view at which the scene’s contents begin to be obscured by fog. Animatable.
- [var fogEndDistance: CGFloat](scnscene/fogenddistance.md)
  The distance from a point of view at which the scene’s contents are completely obscured by fog. Animatable.
- [var fogDensityExponent: CGFloat](scnscene/fogdensityexponent.md)
  The transition curve for the fog’s intensity between its start and end distances. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/fogcolor)*