# fogDensityExponent

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The transition curve for the fog’s intensity between its start and end distances. Animatable.

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
var fogDensityExponent: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat fogDensityExponent;
```

#### Discussion

A fog effect fades out the contents of the scene with increasing distance from the [`pointOfView`](../scnscenerenderer/pointofview.md) location, replacing them with increasing intensities of the [`fogColor`](./fogcolor.md) color. The [`fogDensityExponent`](./fogdensityexponent.md) property determines the smoothness or abruptness of this transition.

A value of `0.0` (the default) specifies no attenuation—the fog’s intensity is the same at all distances . A value of `1.0` specifies a linear transition, and a value of `2.0` specifies a quadratic transition curve. Higher values have little visible effect.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adding Fog to a Scene
- [var fogStartDistance: CGFloat](./fogstartdistance.md)
  The distance from a point of view at which the scene’s contents begin to be obscured by fog. Animatable.
- [var fogEndDistance: CGFloat](./fogenddistance.md)
  The distance from a point of view at which the scene’s contents are completely obscured by fog. Animatable.
- [var fogColor: Any](./fogcolor.md)
  The color of the fog effect to be rendered with the scene. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/fogdensityexponent)*