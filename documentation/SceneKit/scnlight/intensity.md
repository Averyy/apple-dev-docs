# intensity

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The luminous flux, in lumens, or total brightness of the light. Animatable.

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
var intensity: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat intensity;
```

#### Discussion

When working with photometric lights (see the [`iesProfileURL`](./iesprofileurl.md) property) or physically-based rendering (see [`physicallyBased`](../scnmaterial/lightingmodel-swift.struct/physicallybased.md)), you can leave the [`color`](./color.md) property at its default white color and use the [`intensity`](./intensity.md) and [`temperature`](./temperature.md) to control the light using realistic parameters. When working with physically-based materials, this value the luminous flux of the light source. The default value is `1000` lumens.

When not using physically-based rendering, this value (divided by 1000) serves as a multiplier for the the [`color`](./color.md) property. The default value of of `1000` leaves the light color unmodulated; you can use higher values, for example, to brighten a light whose color is already the maximum red value.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Modifying a Light’s Appearance
- [var type: SCNLight.LightType](./type.md)
  A constant identifying the general behavior of the light.
- [SCNLight.LightType](./lighttype.md)
  Constants specifying the general behavior of a light, used by the [`type`](./type.md) property.
- [var color: Any](./color.md)
  The color of the light. Animatable.
- [var temperature: CGFloat](./temperature.md)
  The color temperature, in degrees Kelvin, of the light source. Animatable.
- [var sphericalHarmonicsCoefficients: Data](./sphericalharmonicscoefficients.md)
  Data describing the estimated lighting environment in all directions for a light probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/intensity)*