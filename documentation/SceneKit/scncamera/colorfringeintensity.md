# colorFringeIntensity

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The blend factor for fading the color fringing effect applied to the rendered scene.

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
var colorFringeIntensity: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat colorFringeIntensity;
```

#### Discussion

Color fringing applies an effect that separately blurs the color components of each rendered pixel, adding subtle rainbow edge effects to the rendered scene that simulate the effects of chromatic aberration in a physical camera. Higher values for this property result in brighter, more vivid color fringing, and lower values create a subtler effect. The default value of `1.0` leaves the color fringing effect at its most vivid.

This property controls a fade between the color fringing effect and the otherwise-normally-rendered image. The [`colorFringeStrength`](./colorfringestrength.md) property controls the breadth of the color fringing effect.

To enable this behavior, you must first enable the [`wantsHDR`](./wantshdr.md) setting.

## See Also

### Adding Stylistic Visual Effects
- [var bloomIntensity: CGFloat](./bloomintensity.md)
  The magnitude of bloom effect to apply to highlights in the rendered scene. Animatable.
- [var bloomThreshold: CGFloat](./bloomthreshold.md)
  The brightness threshold at which to apply a bloom effect to highlights in the rendered scene. Animatable.
- [var bloomBlurRadius: CGFloat](./bloomblurradius.md)
  The radius, in pixels, for the blurring portion of the bloom effect applied to highlights in the rendered scene. Animatable.
- [var colorFringeStrength: CGFloat](./colorfringestrength.md)
  The magnitude of color fringing effect to apply to the rendered scene.
- [var vignettingIntensity: CGFloat](./vignettingintensity.md)
  The magnitude of vignette (darkening around edges) effect to apply to the rendered scene.
- [var vignettingPower: CGFloat](./vignettingpower.md)
  The amount of the rendered scene to darken with a vignette effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/colorfringeintensity)*