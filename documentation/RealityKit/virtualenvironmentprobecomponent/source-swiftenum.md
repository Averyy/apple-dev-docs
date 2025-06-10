# VirtualEnvironmentProbeComponent.Source

**Framework**: RealityKit  
**Kind**: enum

Options that define the source of diffuse and specular lighting for environment lighting calculations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
enum Source
```

## Topics

### Enumeration Cases
- [case blend(from: VirtualEnvironmentProbeComponent.Probe, to: VirtualEnvironmentProbeComponent.Probe, t: Float)](virtualenvironmentprobecomponent/source-swift.enum/blend(from:to:t:).md)
  A source that blends between two pregenerated probes based on the provided blend factor.
- [VirtualEnvironmentProbeComponent.Source.none](virtualenvironmentprobecomponent/source-swift.enum/none.md)
  A source without any lighting.
- [case single(VirtualEnvironmentProbeComponent.Probe)](virtualenvironmentprobecomponent/source-swift.enum/single(_:).md)
  A source representing a single pregenerated probe.

## See Also

- [class EnvironmentResource](environmentresource.md)
  An environmental resource that contains background and lighting information for a scene.
- [struct EnvironmentLightingConfigurationComponent](environmentlightingconfigurationcomponent.md)
  A component that scales the amount of light that an entity receives from its environment.
- [struct VirtualEnvironmentProbeComponent](virtualenvironmentprobecomponent.md)
  A component that provides environment lighting for entities you place within the same virtual world.
- [VirtualEnvironmentProbeComponent.Probe](virtualenvironmentprobecomponent/probe.md)
  A sample of the environment around a point in a scene the system uses for environment-based lighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/virtualenvironmentprobecomponent/source-swift.enum)*