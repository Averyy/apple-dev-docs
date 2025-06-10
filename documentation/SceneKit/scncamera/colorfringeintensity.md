# colorFringeIntensity

**Framework**: SceneKit  
**Kind**: property

The blend factor for fading the color fringing effect applied to the rendered scene.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var colorFringeIntensity: CGFloat { get set }
```

#### Discussion

Color fringing applies an effect that separately blurs the color components of each rendered pixel, adding subtle rainbow edge effects to the rendered scene that simulate the effects of chromatic aberration in a physical camera. Higher values for this property result in brighter, more vivid color fringing, and lower values create a subtler effect. The default value of `1.0` leaves the color fringing effect at its most vivid.

This property controls a fade between the color fringing effect and the otherwise-normally-rendered image. The [`colorFringeStrength`](scncamera/colorfringestrength.md) property controls the breadth of the color fringing effect.

To enable this behavior, you must first enable the [`wantsHDR`](scncamera/wantshdr.md) setting.

## See Also

- [var bloomIntensity: CGFloat](scncamera/bloomintensity.md)
  The magnitude of bloom effect to apply to highlights in the rendered scene. Animatable.
- [var bloomThreshold: CGFloat](scncamera/bloomthreshold.md)
  The brightness threshold at which to apply a bloom effect to highlights in the rendered scene. Animatable.
- [var bloomBlurRadius: CGFloat](scncamera/bloomblurradius.md)
  The radius, in pixels, for the blurring portion of the bloom effect applied to highlights in the rendered scene. Animatable.
- [var colorFringeStrength: CGFloat](scncamera/colorfringestrength.md)
  The magnitude of color fringing effect to apply to the rendered scene.
- [var vignettingIntensity: CGFloat](scncamera/vignettingintensity.md)
  The magnitude of vignette (darkening around edges) effect to apply to the rendered scene.
- [var vignettingPower: CGFloat](scncamera/vignettingpower.md)
  The amount of the rendered scene to darken with a vignette effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/colorfringeintensity)*