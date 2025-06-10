# EnvironmentResource.CreateOptions

**Framework**: RealityKit  
**Kind**: struct

A type that controls compression, sampling quality, and cubemap dimensions when creating an environment resource.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct CreateOptions
```

#### Overview

The options provide control for balancing memory usage, quality, and processing power when creating an environment’s lighting data.

## Topics

### Initializers
- [init(samplingQuality:specularCubeDimension:compression:)](environmentresource/createoptions-7diu2/init(samplingquality:specularcubedimension:compression:).md)
  Creates an environment creation options structure.
### Instance Properties
- [var compression: EnvironmentResource.Compression](environmentresource/createoptions-eoe9/compression.md)
  The compression to apply to environment textures.
- [var samplingQuality: EnvironmentResource.CreateOptions.SamplingQuality](environmentresource/createoptions-eoe9/samplingquality-swift.property.md)
  The skybox sampling quality for lighting textures.
- [var specularCubeDimension: Int?](environmentresource/createoptions-eoe9/specularcubedimension.md)
  The dimension of the computed specular cubemap for material reflections.
### Enumerations
- [EnvironmentResource.CreateOptions.SamplingQuality](environmentresource/createoptions-eoe9/samplingquality-swift.enum.md)
  An object for controlling the skybox sampling quality for lighting textures.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/createoptions-eoe9)*