# IES

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

A light source whose shape, direction, and intensity of illumination is determined by a photometric profile.

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
static let IES: SCNLight.LightType
```

```c
extern SCNLightType const SCNLightTypeIES;
```

## Discussion

The intensity of a photometric light varies in different directions from the light source, much like the illumination from a real-world light source. The position of the containing node determines the location of the light source, and the orientation of the node determines the relative directions specified by the photometric profile. Spotlight angle attributes do not apply to photometric lights.

For more information about photometric lights, see the [`iesProfileURL`](../iesprofileurl.md) property.

## See Also

### Type Properties
- [static let ambient: SCNLight.LightType](./ambient.md)
  A light that illuminates all objects in the scene from all directions.
- [static let directional: SCNLight.LightType](./directional.md)
  A light source with a uniform direction and constant intensity.
- [static let omni: SCNLight.LightType](./omni.md)
  An omnidirectional light, also known as a *point light*.
- [static let probe: SCNLight.LightType](./probe.md)
  A sample of the environment around a point in a scene to be used in environment-based lighting.
- [static let spot: SCNLight.LightType](./spot.md)
  A light source that illuminates a cone-shaped area.
- [static let area: SCNLight.LightType](./area.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/lighttype/ies)*