# temperature

**Framework**: SceneKit  
**Kind**: property

The color temperature, in degrees Kelvin, of the light source. Animatable.

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
var temperature: CGFloat { get set }
```

#### Discussion

SceneKit determines the actual color of the light by multiplying the [`color`](scnlight/color.md) value by a color corresponding to the light’s temperature. The default value of `6500` K represents a pure white light (leaving the color unmodulated); lower values (down to a minimum of zero) add a “warmer” yellow or orange effect to the light source, and higher values (up to a maximum of `40000`) add a “cooler” blue effect.

This property affects all light types, but is especially useful when working with photometric lights (see the [`iesProfileURL`](scnlight/iesprofileurl.md) property) or physically-based rendering (see [`physicallyBased`](scnmaterial/lightingmodel-swift.struct/physicallybased.md)). You can leave the [`color`](scnlight/color.md) property at its default white color and use the [`intensity`](scnlight/intensity.md) and [`temperature`](scnlight/temperature.md) properties to control the light using realistic parameters.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var type: SCNLight.LightType](scnlight/type.md)
  A constant identifying the general behavior of the light.
- [SCNLight.LightType](scnlight/lighttype.md)
  Constants specifying the general behavior of a light, used by the [`type`](scnlight/type.md) property.
- [var color: Any](scnlight/color.md)
  The color of the light. Animatable.
- [var intensity: CGFloat](scnlight/intensity.md)
  The luminous flux, in lumens, or total brightness of the light. Animatable.
- [var sphericalHarmonicsCoefficients: Data](scnlight/sphericalharmonicscoefficients.md)
  Data describing the estimated lighting environment in all directions for a light probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/temperature)*