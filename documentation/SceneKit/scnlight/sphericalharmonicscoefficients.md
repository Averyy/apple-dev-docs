# sphericalHarmonicsCoefficients

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

Data describing the estimated lighting environment in all directions for a light probe.

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
var sphericalHarmonicsCoefficients: Data { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * sphericalHarmonicsCoefficients;
```

#### Discussion

Spherical harmonic coefficients describe the distribution of light around a point in a format that can be used efficiently in real-time rendering. SceneKit supports spherical harmonics only for lights of the [`probe`](./lighttype/probe.md) type.

The data is an 32-bit floating-point values, containing three noninterleaved data sets corresponding to the red, green, and blue sets of coefficients. SceneKit supports only level 2 spherical harmonics, so the array has 3 sets of 9 values, or 27 values total.

## See Also

### Related Documentation
- [class ARDirectionalLightEstimate](../../ARKit/ardirectionallightestimate.md)
  Estimated environmental lighting information associated with a captured video frame in a face-tracking AR session.
- [class MDLLightProbe](../../ModelIO/mdllightprobe.md)
  A light source described in terms of the variations in color and intensity of its illumination in all directions.
### Modifying a Light’s Appearance
- [var type: SCNLight.LightType](./type.md)
  A constant identifying the general behavior of the light.
- [SCNLight.LightType](./lighttype.md)
  Constants specifying the general behavior of a light, used by the [`type`](./type.md) property.
- [var color: Any](./color.md)
  The color of the light. Animatable.
- [var temperature: CGFloat](./temperature.md)
  The color temperature, in degrees Kelvin, of the light source. Animatable.
- [var intensity: CGFloat](./intensity.md)
  The luminous flux, in lumens, or total brightness of the light. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/sphericalharmonicscoefficients)*