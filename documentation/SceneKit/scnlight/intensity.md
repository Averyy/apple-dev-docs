# intensity

**Framework**: SceneKit  
**Kind**: property

The luminous flux, in lumens, or total brightness of the light. Animatable.

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
var intensity: CGFloat { get set }
```

#### Discussion

When working with photometric lights (see the [`iesProfileURL`](scnlight/iesprofileurl.md) property) or physically-based rendering (see [`physicallyBased`](scnmaterial/lightingmodel-swift.struct/physicallybased.md)), you can leave the [`color`](scnlight/color.md) property at its default white color and use the [`intensity`](scnlight/intensity.md) and [`temperature`](scnlight/temperature.md) to control the light using realistic parameters. When working with physically-based materials, this value the luminous flux of the light source. The default value is `1000` lumens.

When not using physically-based rendering, this value (divided by 1000) serves as a multiplier for the the [`color`](scnlight/color.md) property. The default value of of `1000` leaves the light color unmodulated; you can use higher values, for example, to brighten a light whose color is already the maximum red value.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var type: SCNLight.LightType](scnlight/type.md)
  A constant identifying the general behavior of the light.
- [SCNLight.LightType](scnlight/lighttype.md)
  Constants specifying the general behavior of a light, used by the [`type`](scnlight/type.md) property.
- [var color: Any](scnlight/color.md)
  The color of the light. Animatable.
- [var temperature: CGFloat](scnlight/temperature.md)
  The color temperature, in degrees Kelvin, of the light source. Animatable.
- [var sphericalHarmonicsCoefficients: Data](scnlight/sphericalharmonicscoefficients.md)
  Data describing the estimated lighting environment in all directions for a light probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/intensity)*