# probe

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

A sample of the environment around a point in a scene to be used in environment-based lighting.

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
static let probe: SCNLight.LightType
```

```c
extern SCNLightType const SCNLightTypeProbe;
```

#### Discussion

A light probe describes a point in a scene in terms of the variations in color and intensity of the illumination it receives from all directions. This information can then be used in shading of materials based on their location in the scene. For example, a white object placed near blue and red walls will appear bluish on surfaces facing the blue wall and reddish on surfaces facing the red wall.

You can place light probes in a scene and generate their lighting contributions using the Xcode scene editor, or import light probes from scene file formats that support them. Lighting-related properties of the [`SCNLight`](../../scnlight.md) class do not apply to light probes; their contribution to scene rendering depends entirely on the light probe content generated in Xcode.

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
- [static let spot: SCNLight.LightType](./spot.md)
  A light source that illuminates a cone-shaped area.
- [static let area: SCNLight.LightType](./area.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/lighttype/probe)*