# vignettingPower

**Framework**: SceneKit  
**Kind**: property

The amount of the rendered scene to darken with a vignette effect.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var vignettingPower: CGFloat { get set }
```

#### Discussion

A vignette effect darkens the edges and corners of the rendered scene, simulating the effect of lens and barrel shape on the image produced by a physical camera. Higher values result apply the darkening effect to a broader area around the edges of the rendered image, and lower values apply the effect to a smaller area, leaving more of the rendered image at full brightness. The default value of `0.0` results in no vignetting effect.

This property controls the area of the rendered image to be darkened; the [`vignettingIntensity`](scncamera/vignettingintensity.md) property controls the level of darkening applied to those areas.

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
- [var vignettingIntensity: CGFloat](scncamera/vignettingintensity.md)
  The magnitude of vignette (darkening around edges) effect to apply to the rendered scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/vignettingpower)*