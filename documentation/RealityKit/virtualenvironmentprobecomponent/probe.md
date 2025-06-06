# VirtualEnvironmentProbeComponent.Probe

**Framework**: RealityKit  
**Kind**: struct

A sample of the environment around a point in a scene the system uses for environment-based lighting.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct Probe
```

## Topics

### Initializers
- [init(environment: EnvironmentResource, intensityExponent: Float)](virtualenvironmentprobecomponent/probe/init(environment:intensityexponent:).md)
  Creates a virtual-environment probe from an environment resource and intensity value.
### Instance Properties
- [var environment: EnvironmentResource](virtualenvironmentprobecomponent/probe/environment.md)
  The resource that stores a representation of diffuse and specular environment lighting.
- [var intensityExponent: Float](virtualenvironmentprobecomponent/probe/intensityexponent.md)
  The intensity value for the resource, which RealityKit defines on a logarithmic scale.

## See Also

- [class EnvironmentResource](environmentresource.md)
  An environmental resource that contains background and lighting information for a scene.
- [struct EnvironmentLightingConfigurationComponent](environmentlightingconfigurationcomponent.md)
  A component that scales the amount of light that an entity receives from its environment.
- [struct VirtualEnvironmentProbeComponent](virtualenvironmentprobecomponent.md)
  A component that provides environment lighting for entities you place within the same virtual world.
- [VirtualEnvironmentProbeComponent.Source](virtualenvironmentprobecomponent/source-swift.enum.md)
  Options that define the source of diffuse and specular lighting for environment lighting calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/virtualenvironmentprobecomponent/probe)*