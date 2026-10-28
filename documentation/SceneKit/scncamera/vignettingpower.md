# vignettingPower

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The amount of the rendered scene to darken with a vignette effect.

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
var vignettingPower: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat vignettingPower;
```

## Discussion

A vignette effect darkens the edges and corners of the rendered scene, simulating the effect of lens and barrel shape on the image produced by a physical camera. Higher values result apply the darkening effect to a broader area around the edges of the rendered image, and lower values apply the effect to a smaller area, leaving more of the rendered image at full brightness. The default value of `0.0` results in no vignetting effect.

This property controls the area of the rendered image to be darkened; the [`vignettingIntensity`](./vignettingintensity.md) property controls the level of darkening applied to those areas.

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
- [var colorFringeStrength: CGFloat](./colorfringestrength.md)
  The magnitude of color fringing effect to apply to the rendered scene.
- [var vignettingIntensity: CGFloat](./vignettingintensity.md)
  The magnitude of vignette (darkening around edges) effect to apply to the rendered scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/vignettingpower)*