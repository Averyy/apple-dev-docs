# color

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The color of the light. Animatable.

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
var color: Any { get set }
```

```objc
@property (nonatomic, retain) id color;
```

## Discussion

The value of this property is an [`NSColor`](../../AppKit/nscolor.md) or [`CGColor`](../../CoreGraphics/cgcolor.md) object. The default color is white.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Modifying a Light’s Appearance
- [var type: SCNLight.LightType](./type.md)
  A constant identifying the general behavior of the light.
- [SCNLight.LightType](./lighttype.md)
  Constants specifying the general behavior of a light, used by the [`type`](./type.md) property.
- [var temperature: CGFloat](./temperature.md)
  The color temperature, in degrees Kelvin, of the light source. Animatable.
- [var intensity: CGFloat](./intensity.md)
  The luminous flux, in lumens, or total brightness of the light. Animatable.
- [var sphericalHarmonicsCoefficients: Data](./sphericalharmonicscoefficients.md)
  Data describing the estimated lighting environment in all directions for a light probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/color)*