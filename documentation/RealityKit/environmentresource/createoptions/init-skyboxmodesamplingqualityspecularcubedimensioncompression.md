# init(skyboxMode:samplingQuality:specularCubeDimension:compression:)

**Framework**: RealityKit  
**Kind**: init

Creates an environment creation options structure.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(skyboxMode: EnvironmentResource.SkyboxMode, samplingQuality: EnvironmentResource.CreateOptions.SamplingQuality = .fast, specularCubeDimension: Int? = nil, compression: EnvironmentResource.Compression = .default)
```

#### Discussion

> **Note**: The skybox is not needed for image based lighting with `VirtualEnvironmentProbeComponent` and `ImageBasedLightComponent`.

## Parameters

- `skyboxMode`: Skybox’s preservation in the environment resource.
- `samplingQuality`: The skybox sampling quality for lighting textures.
- `specularCubeDimension`: The dimension of the computed specular cubemap for material reflections.
- `compression`: The compression to apply to environment textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/createoptions/init(skyboxmode:samplingquality:specularcubedimension:compression:))*