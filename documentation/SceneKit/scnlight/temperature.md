# temperature

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The color temperature, in degrees Kelvin, of the light source. Animatable.

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
var temperature: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat temperature;
```

## Discussion

SceneKit determines the actual color of the light by multiplying the [`color`](./color.md) value by a color corresponding to the light’s temperature. The default value of `6500` K represents a pure white light (leaving the color unmodulated); lower values (down to a minimum of zero) add a “warmer” yellow or orange effect to the light source, and higher values (up to a maximum of `40000`) add a “cooler” blue effect.

This property affects all light types, but is especially useful when working with photometric lights (see the [`iesProfileURL`](./iesprofileurl.md) property) or physically-based rendering (see [`physicallyBased`](../scnmaterial/lightingmodel-swift.struct/physicallybased.md)). You can leave the [`color`](./color.md) property at its default white color and use the [`intensity`](./intensity.md) and [`temperature`](./temperature.md) properties to control the light using realistic parameters.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Modifying a Light’s Appearance
- [var type: SCNLight.LightType](./type.md)
  A constant identifying the general behavior of the light.
- [SCNLight.LightType](./lighttype.md)
  Constants specifying the general behavior of a light, used by the [`type`](./type.md) property.
- [var color: Any](./color.md)
  The color of the light. Animatable.
- [var intensity: CGFloat](./intensity.md)
  The luminous flux, in lumens, or total brightness of the light. Animatable.
- [var sphericalHarmonicsCoefficients: Data](./sphericalharmonicscoefficients.md)
  Data describing the estimated lighting environment in all directions for a light probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/temperature)*