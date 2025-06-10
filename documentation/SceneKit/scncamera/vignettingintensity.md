# vignettingIntensity

**Framework**: SceneKit  
**Kind**: property

The magnitude of vignette (darkening around edges) effect to apply to the rendered scene.

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
var vignettingIntensity: CGFloat { get set }
```

#### Discussion

A vignette effect darkens the edges and corners of the rendered scene, simulating the effect of lens and barrel shape on the image produced by a physical camera. Higher values result in more darkening, and lower values result in a subtler effect. The default value of `0.0` results in no vignetting effect.

This property controls the level of darkening applied; the [`vignettingPower`](scncamera/vignettingpower.md) property controls the area of the rendered image to be darkened.

To enable this behavior, you must first enable the [`wantsHDR`](scncamera/wantshdr.md) setting.

## See Also

- [var bloomIntensity: CGFloat](scncamera/bloomintensity.md)
  The magnitude of bloom effect to apply to highlights in the rendered scene. Animatable.
- [var bloomThreshold: CGFloat](scncamera/bloomthreshold.md)
  The brightness threshold at which to apply a bloom effect to highlights in the rendered scene. Animatable.
- [var bloomBlurRadius: CGFloat](scncamera/bloomblurradius.md)
  The radius, in pixels, for the blurring portion of the bloom effect applied to highlights in the rendered scene. Animatable.
- [var colorFringeIntensity: CGFloat](scncamera/colorfringeintensity.md)
  The blend factor for fading the color fringing effect applied to the rendered scene.
- [var colorFringeStrength: CGFloat](scncamera/colorfringestrength.md)
  The magnitude of color fringing effect to apply to the rendered scene.
- [var vignettingPower: CGFloat](scncamera/vignettingpower.md)
  The amount of the rendered scene to darken with a vignette effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/vignettingintensity)*