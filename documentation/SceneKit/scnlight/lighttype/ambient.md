# ambient

**Framework**: SceneKit  
**Kind**: property

A light that illuminates all objects in the scene from all directions.

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
static let ambient: SCNLight.LightType
```

#### Discussion

Because the intensity of light from an ambient source is the same everywhere in the scene,  its position and direction have no effect. Attenuation, spotlight angle, and shadow attributes do not apply to ambient lights.

## See Also

- [static let IES: SCNLight.LightType](scnlight/lighttype/ies.md)
  A light source whose shape, direction, and intensity of illumination is determined by a photometric profile.
- [static let directional: SCNLight.LightType](scnlight/lighttype/directional.md)
  A light source with a uniform direction and constant intensity.
- [static let omni: SCNLight.LightType](scnlight/lighttype/omni.md)
  An omnidirectional light, also known as a .
- [static let probe: SCNLight.LightType](scnlight/lighttype/probe.md)
  A sample of the environment around a point in a scene to be used in environment-based lighting.
- [static let spot: SCNLight.LightType](scnlight/lighttype/spot.md)
  A light source that illuminates a cone-shaped area.
- [static let area: SCNLight.LightType](scnlight/lighttype/area.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/lighttype/ambient)*