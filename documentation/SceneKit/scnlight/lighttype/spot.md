# spot

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

A light source that illuminates a cone-shaped area.

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
static let spot: SCNLight.LightType
```

```c
extern SCNLightType const SCNLightTypeSpot;
```

## Discussion

The position and orientation of the node containing the light determines the area lit by the spotlight, and all lighting attributes affect its appearance.

## See Also

### Type Properties
- [static let IES: SCNLight.LightType](./ies.md)
  A light source whose shape, direction, and intensity of illumination is determined by a photometric profile.
- [static let ambient: SCNLight.LightType](./ambient.md)
  A light that illuminates all objects in the scene from all directions.
- [static let directional: SCNLight.LightType](./directional.md)
  A light source with a uniform direction and constant intensity.
- [static let omni: SCNLight.LightType](./omni.md)
  An omnidirectional light, also known as a *point light*.
- [static let probe: SCNLight.LightType](./probe.md)
  A sample of the environment around a point in a scene to be used in environment-based lighting.
- [static let area: SCNLight.LightType](./area.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/lighttype/spot)*