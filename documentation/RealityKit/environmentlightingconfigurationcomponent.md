# EnvironmentLightingConfigurationComponent

**Framework**: RealityKit  
**Kind**: struct

A component that scales the amount of light that an entity receives from its environment.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct EnvironmentLightingConfigurationComponent
```

#### Overview

When rendering a RealityKit scene, you can control how much the environment’s lighting affects the virtual objects in your scene, such as the lighting from your real-world surroundings, a virtual environment, or both. Use an `EnvironmentLightingConfigurationComponent` to configure this amount for an entity.

For example, create an entity that receives no lighting from its environment by setting the weight to `0.0`.

```swift
let spaceship = try await Entity(named: "spaceship")
spaceship.components.set(EnvironmentLightingConfigurationComponent(
    environmentLightingWeight: 0.0))
```

> **Note**: The weight value of the component also affects the lighting of the entity’s descendants.

## Topics

### Creating an environment-lighting configuration component
- [init(environmentLightingWeight: Float)](environmentlightingconfigurationcomponent/init(environmentlightingweight:).md)
  Creates an environment-lighting configuration component.
### Scaling the environment-lighting contribution
- [var environmentLightingWeight: Float](environmentlightingconfigurationcomponent/environmentlightingweight.md)
  A value that controls the environment-lighting contribution to an entity’s lighting.
### Comparing environment-lighting configuration components
- [static func == (EnvironmentLightingConfigurationComponent, EnvironmentLightingConfigurationComponent) -> Bool](environmentlightingconfigurationcomponent/==(_:_:).md)
  Returns a Boolean value that indicates whether two environment-lighting configuration components are equal.

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [class EnvironmentResource](environmentresource.md)
  An environmental resource that contains background and lighting information for a scene.
- [struct VirtualEnvironmentProbeComponent](virtualenvironmentprobecomponent.md)
  A component that provides environment lighting for entities you place within the same virtual world.
- [VirtualEnvironmentProbeComponent.Probe](virtualenvironmentprobecomponent/probe.md)
  A sample of the environment around a point in a scene the system uses for environment-based lighting.
- [VirtualEnvironmentProbeComponent.Source](virtualenvironmentprobecomponent/source-swift.enum.md)
  Options that define the source of diffuse and specular lighting for environment lighting calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentlightingconfigurationcomponent)*