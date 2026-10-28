# bloomBlurRadius

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The radius, in pixels, for the blurring portion of the bloom effect applied to highlights in the rendered scene. Animatable.

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
var bloomBlurRadius: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat bloomBlurRadius;
```

## Discussion

A bloom effect adds a soft glow to highlights (areas of bright color) in the rendered scene, simulating the way bright highlights appear to the human eye or a physical camera in a real-world scene. The bloom effect combines selective brightening and blurring effects; this property controls the blur portion of the effect. A value of zero effectively disables the bloom effect, and higher values result in a broader, softer glow. The default value is `4.0` pixels.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

To enable this behavior, you must first enable the [`wantsHDR`](./wantshdr.md) setting.

## See Also

### Adding Stylistic Visual Effects
- [var bloomIntensity: CGFloat](./bloomintensity.md)
  The magnitude of bloom effect to apply to highlights in the rendered scene. Animatable.
- [var bloomThreshold: CGFloat](./bloomthreshold.md)
  The brightness threshold at which to apply a bloom effect to highlights in the rendered scene. Animatable.
- [var colorFringeIntensity: CGFloat](./colorfringeintensity.md)
  The blend factor for fading the color fringing effect applied to the rendered scene.
- [var colorFringeStrength: CGFloat](./colorfringestrength.md)
  The magnitude of color fringing effect to apply to the rendered scene.
- [var vignettingIntensity: CGFloat](./vignettingintensity.md)
  The magnitude of vignette (darkening around edges) effect to apply to the rendered scene.
- [var vignettingPower: CGFloat](./vignettingpower.md)
  The amount of the rendered scene to darken with a vignette effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/bloomblurradius)*