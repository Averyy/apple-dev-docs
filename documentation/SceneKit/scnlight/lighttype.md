# SCNLight.LightType

**Framework**: SceneKit  
**Kind**: struct  
**Role**: Structure

Constants specifying the general behavior of a light, used by the [`type`](./type.md) property.

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
struct LightType
```

```c
typedef NSString * SCNLightType;
```

## Overview

Each of the four scenes in the figure below has the same content illuminated by a single [`SCNLight`](../scnlight.md) object. The node containing the light source has the same position and orientation in each scene—all differences between the four pictures are due to the light’s [`type`](./type.md) property.

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2929780@2x.png)

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2929783@2x.png)

## Topics

### Type Properties
- [static let IES: SCNLight.LightType](./lighttype/ies.md)
  A light source whose shape, direction, and intensity of illumination is determined by a photometric profile.
- [static let ambient: SCNLight.LightType](./lighttype/ambient.md)
  A light that illuminates all objects in the scene from all directions.
- [static let directional: SCNLight.LightType](./lighttype/directional.md)
  A light source with a uniform direction and constant intensity.
- [static let omni: SCNLight.LightType](./lighttype/omni.md)
  An omnidirectional light, also known as a *point light*.
- [static let probe: SCNLight.LightType](./lighttype/probe.md)
  A sample of the environment around a point in a scene to be used in environment-based lighting.
- [static let spot: SCNLight.LightType](./lighttype/spot.md)
  A light source that illuminates a cone-shaped area.
- [static let area: SCNLight.LightType](./lighttype/area.md)
### Initializers
- [init(rawValue: String)](./lighttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Modifying a Light’s Appearance
- [var type: SCNLight.LightType](./type.md)
  A constant identifying the general behavior of the light.
- [var color: Any](./color.md)
  The color of the light. Animatable.
- [var temperature: CGFloat](./temperature.md)
  The color temperature, in degrees Kelvin, of the light source. Animatable.
- [var intensity: CGFloat](./intensity.md)
  The luminous flux, in lumens, or total brightness of the light. Animatable.
- [var sphericalHarmonicsCoefficients: Data](./sphericalharmonicscoefficients.md)
  Data describing the estimated lighting environment in all directions for a light probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/lighttype)*