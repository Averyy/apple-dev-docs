# color

**Framework**: SceneKit  
**Kind**: property

The color of the light. Animatable.

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
var color: Any { get set }
```

#### Discussion

The value of this property is an [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor) or [`CGColor`](https://developer.apple.com/documentation/CoreGraphics/CGColor) object. The default color is white.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var type: SCNLight.LightType](scnlight/type.md)
  A constant identifying the general behavior of the light.
- [SCNLight.LightType](scnlight/lighttype.md)
  Constants specifying the general behavior of a light, used by the [`type`](scnlight/type.md) property.
- [var temperature: CGFloat](scnlight/temperature.md)
  The color temperature, in degrees Kelvin, of the light source. Animatable.
- [var intensity: CGFloat](scnlight/intensity.md)
  The luminous flux, in lumens, or total brightness of the light. Animatable.
- [var sphericalHarmonicsCoefficients: Data](scnlight/sphericalharmonicscoefficients.md)
  Data describing the estimated lighting environment in all directions for a light probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/color)*