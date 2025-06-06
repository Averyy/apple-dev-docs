# probe

**Framework**: SceneKit  
**Kind**: property

A sample of the environment around a point in a scene to be used in environment-based lighting.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static let probe: SCNLight.LightType
```

#### Discussion

A light probe describes a point in a scene in terms of the variations in color and intensity of the illumination it receives from all directions. This information can then be used in shading of materials based on their location in the scene. For example, a white object placed near blue and red walls will appear bluish on surfaces facing the blue wall and reddish on surfaces facing the red wall.

You can place light probes in a scene and generate their lighting contributions using the Xcode scene editor, or import light probes from scene file formats that support them. Lighting-related properties of the [`SCNLight`](scnlight.md) class do not apply to light probes; their contribution to scene rendering depends entirely on the light probe content generated in Xcode.

## See Also

- [static let IES: SCNLight.LightType](scnlight/lighttype/ies.md)
  A light source whose shape, direction, and intensity of illumination is determined by a photometric profile.
- [static let ambient: SCNLight.LightType](scnlight/lighttype/ambient.md)
  A light that illuminates all objects in the scene from all directions.
- [static let directional: SCNLight.LightType](scnlight/lighttype/directional.md)
  A light source with a uniform direction and constant intensity.
- [static let omni: SCNLight.LightType](scnlight/lighttype/omni.md)
  An omnidirectional light, also known as a .
- [static let spot: SCNLight.LightType](scnlight/lighttype/spot.md)
  A light source that illuminates a cone-shaped area.
- [static let area: SCNLight.LightType](scnlight/lighttype/area.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/lighttype/probe)*