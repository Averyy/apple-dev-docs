# SCNLight.LightType

**Framework**: SceneKit  
**Kind**: struct

Constants specifying the general behavior of a light, used by the [`type`](scnlight/type.md) property.

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
struct LightType
```

#### Overview

Each of the four scenes in the figure below has the same content illuminated by a single [`SCNLight`](scnlight.md) object. The node containing the light source has the same position and orientation in each scene—all differences between the four pictures are due to the light’s [`type`](scnlight/type.md) property.

![None](https://docs-assets.developer.apple.com/published/eb60d2d59a291b85e0103d60120f7d81/media-2929780%402x.png)

![None](https://docs-assets.developer.apple.com/published/ae5647e6cf3f8abe6ac1f57a449fa23b/media-2929783%402x.png)

## Topics

### Type Properties
- [static let IES: SCNLight.LightType](scnlight/lighttype/ies.md)
  A light source whose shape, direction, and intensity of illumination is determined by a photometric profile.
- [static let ambient: SCNLight.LightType](scnlight/lighttype/ambient.md)
  A light that illuminates all objects in the scene from all directions.
- [static let directional: SCNLight.LightType](scnlight/lighttype/directional.md)
  A light source with a uniform direction and constant intensity.
- [static let omni: SCNLight.LightType](scnlight/lighttype/omni.md)
  An omnidirectional light, also known as a .
- [static let probe: SCNLight.LightType](scnlight/lighttype/probe.md)
  A sample of the environment around a point in a scene to be used in environment-based lighting.
- [static let spot: SCNLight.LightType](scnlight/lighttype/spot.md)
  A light source that illuminates a cone-shaped area.
- [static let area: SCNLight.LightType](scnlight/lighttype/area.md)
### Initializers
- [init(rawValue: String)](scnlight/lighttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var type: SCNLight.LightType](scnlight/type.md)
  A constant identifying the general behavior of the light.
- [var color: Any](scnlight/color.md)
  The color of the light. Animatable.
- [var temperature: CGFloat](scnlight/temperature.md)
  The color temperature, in degrees Kelvin, of the light source. Animatable.
- [var intensity: CGFloat](scnlight/intensity.md)
  The luminous flux, in lumens, or total brightness of the light. Animatable.
- [var sphericalHarmonicsCoefficients: Data](scnlight/sphericalharmonicscoefficients.md)
  Data describing the estimated lighting environment in all directions for a light probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/lighttype)*