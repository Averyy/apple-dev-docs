# sphericalHarmonicsCoefficients

**Framework**: SceneKit  
**Kind**: property

Data describing the estimated lighting environment in all directions for a light probe.

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
var sphericalHarmonicsCoefficients: Data { get }
```

#### Discussion

Spherical harmonic coefficients describe the distribution of light around a point in a format that can be used efficiently in real-time rendering. SceneKit supports spherical harmonics only for lights of the [`probe`](scnlight/lighttype/probe.md) type.

The data is an 32-bit floating-point values, containing three noninterleaved data sets corresponding to the red, green, and blue sets of coefficients. SceneKit supports only level 2 spherical harmonics, so the array has 3 sets of 9 values, or 27 values total.

## See Also

- [class ARDirectionalLightEstimate](../ARKit/ARDirectionalLightEstimate.md)
  Estimated environmental lighting information associated with a captured video frame in a face-tracking AR session.
- [class MDLLightProbe](../ModelIO/MDLLightProbe.md)
  A light source described in terms of the variations in color and intensity of its illumination in all directions.
- [var type: SCNLight.LightType](scnlight/type.md)
  A constant identifying the general behavior of the light.
- [SCNLight.LightType](scnlight/lighttype.md)
  Constants specifying the general behavior of a light, used by the [`type`](scnlight/type.md) property.
- [var color: Any](scnlight/color.md)
  The color of the light. Animatable.
- [var temperature: CGFloat](scnlight/temperature.md)
  The color temperature, in degrees Kelvin, of the light source. Animatable.
- [var intensity: CGFloat](scnlight/intensity.md)
  The luminous flux, in lumens, or total brightness of the light. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/sphericalharmonicscoefficients)*