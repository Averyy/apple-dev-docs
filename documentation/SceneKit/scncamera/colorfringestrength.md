# colorFringeStrength

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The magnitude of color fringing effect to apply to the rendered scene.

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
var colorFringeStrength: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat colorFringeStrength;
```

## Discussion

Color fringing applies an effect that separately blurs the color components of each rendered pixel, adding subtle rainbow edge effects to the rendered scene that simulate the effects of chromatic aberration in a physical camera. Higher values create a more pronounced color shift, creating wider rainbow fringes; lower values spread colors across shorter distances, creating a subtler effect. The default value of `0.0` disables the color fringing effect entirely.

This property controls the breadth of color fringing. The [`colorFringeIntensity`](./colorfringeintensity.md) property controls the blend factor between the color-fringed and the otherwise-normally-rendered image.

To enable this behavior, you must first enable the [`wantsHDR`](./wantshdr.md) setting.

## See Also

### Adding Stylistic Visual Effects
- [var bloomIntensity: CGFloat](./bloomintensity.md)
  The magnitude of bloom effect to apply to highlights in the rendered scene. Animatable.
- [var bloomThreshold: CGFloat](./bloomthreshold.md)
  The brightness threshold at which to apply a bloom effect to highlights in the rendered scene. Animatable.
- [var bloomBlurRadius: CGFloat](./bloomblurradius.md)
  The radius, in pixels, for the blurring portion of the bloom effect applied to highlights in the rendered scene. Animatable.
- [var colorFringeIntensity: CGFloat](./colorfringeintensity.md)
  The blend factor for fading the color fringing effect applied to the rendered scene.
- [var vignettingIntensity: CGFloat](./vignettingintensity.md)
  The magnitude of vignette (darkening around edges) effect to apply to the rendered scene.
- [var vignettingPower: CGFloat](./vignettingpower.md)
  The amount of the rendered scene to darken with a vignette effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/colorfringestrength)*