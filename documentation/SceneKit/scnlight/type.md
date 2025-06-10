# type

**Framework**: SceneKit  
**Kind**: property

A constant identifying the general behavior of the light.

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
var type: SCNLight.LightType { get set }
```

#### Discussion

A light’s type determines the shape and directionality of illumination provided by the light, as well as the set of attributes available for modifying the light’s behavior. For example, light types include omnidirectional lights and spotlights. See `Light Types` for the full set of types and their behaviors.

## See Also

- [SCNLight.LightType](scnlight/lighttype.md)
  Constants specifying the general behavior of a light, used by the [`type`](scnlight/type.md) property.
- [var color: Any](scnlight/color.md)
  The color of the light. Animatable.
- [var temperature: CGFloat](scnlight/temperature.md)
  The color temperature, in degrees Kelvin, of the light source. Animatable.
- [var intensity: CGFloat](scnlight/intensity.md)
  The luminous flux, in lumens, or total brightness of the light. Animatable.
- [var sphericalHarmonicsCoefficients: Data](scnlight/sphericalharmonicscoefficients.md)
  Data describing the estimated lighting environment in all directions for a light probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/type)*