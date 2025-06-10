# omni

**Framework**: SceneKit  
**Kind**: property

An omnidirectional light, also known as a .

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
static let omni: SCNLight.LightType
```

#### Discussion

Because an omnidirectional light casts equal illumination in all directions, the orientation of the node containing the light has no effect. Spotlight angle and shadow attributes do not apply to directional lights.

## See Also

- [static let IES: SCNLight.LightType](scnlight/lighttype/ies.md)
  A light source whose shape, direction, and intensity of illumination is determined by a photometric profile.
- [static let ambient: SCNLight.LightType](scnlight/lighttype/ambient.md)
  A light that illuminates all objects in the scene from all directions.
- [static let directional: SCNLight.LightType](scnlight/lighttype/directional.md)
  A light source with a uniform direction and constant intensity.
- [static let probe: SCNLight.LightType](scnlight/lighttype/probe.md)
  A sample of the environment around a point in a scene to be used in environment-based lighting.
- [static let spot: SCNLight.LightType](scnlight/lighttype/spot.md)
  A light source that illuminates a cone-shaped area.
- [static let area: SCNLight.LightType](scnlight/lighttype/area.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/lighttype/omni)*