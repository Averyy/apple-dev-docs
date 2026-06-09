# init(skyboxMode:samplingQuality:specularCubeDimension:compression:)

**Framework**: RealityKit  
**Kind**: init

Creates an environment creation options structure.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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