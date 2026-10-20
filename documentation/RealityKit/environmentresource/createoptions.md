# EnvironmentResource.CreateOptions

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A type that controls compression, sampling quality, and cubemap dimensions when creating an environment resource.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct CreateOptions
```

#### Overview

The options provide control for balancing memory usage, quality, and processing power when creating an environment’s lighting data.

## Topics

### Creating the options
- [init(samplingQuality: EnvironmentResource.CreateOptions.SamplingQuality, specularCubeDimension: Int?, compression: EnvironmentResource.Compression)](./createoptions/init%28samplingquality,specularcubedimension,compression%29.md)
  Creates an environment creation options structure.
### Specifying the quality
- [EnvironmentResource.CreateOptions.SamplingQuality](./createoptions/samplingquality-swift.enum.md)
  An object for controlling the skybox sampling quality for lighting textures.
### Accessing the option properties
- [var compression: EnvironmentResource.Compression](./createoptions/compression.md)
  The compression to apply to environment textures.
- [var samplingQuality: EnvironmentResource.CreateOptions.SamplingQuality](./createoptions/samplingquality-swift.property.md)
  The skybox sampling quality for lighting textures.
- [var specularCubeDimension: Int?](./createoptions/specularcubedimension.md)
  The dimension of the computed specular cubemap for material reflections.
### Creating create options
- [init(skyboxMode: EnvironmentResource.SkyboxMode, samplingQuality: EnvironmentResource.CreateOptions.SamplingQuality, specularCubeDimension: Int?, compression: EnvironmentResource.Compression)](./createoptions/init%28skyboxmode,samplingquality,specularcubedimension,compression%29.md)
  Creates an environment creation options structure.
### Configuring the skybox
- [var skyboxMode: EnvironmentResource.SkyboxMode](./createoptions/skyboxmode.md)
  Skybox’s preservation in the environment resource.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the resource creation
- [EnvironmentResource.Compression](./compression.md)
  The compression to apply when creating an environment resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/createoptions)*