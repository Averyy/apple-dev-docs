# EnvironmentResource.CreateOptions

**Framework**: RealityKit  
**Kind**: struct

A type that controls compression, sampling quality, and cubemap dimensions when creating an environment resource.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct CreateOptions
```

#### Overview

The options provide control for balancing memory usage, quality, and processing power when creating an environment’s lighting data.

## Topics

### Creating the options
- [init(samplingQuality: EnvironmentResource.CreateOptions.SamplingQuality, specularCubeDimension: Int?, compression: EnvironmentResource.Compression)](environmentresource/createoptions/init(samplingquality:specularcubedimension:compression:).md)
  Creates an environment creation options structure.
### Specifying the quality
- [EnvironmentResource.CreateOptions.SamplingQuality](environmentresource/createoptions/samplingquality-swift.enum.md)
  An object for controlling the skybox sampling quality for lighting textures.
### Accessing the option properties
- [var compression: EnvironmentResource.Compression](environmentresource/createoptions/compression.md)
  The compression to apply to environment textures.
- [var samplingQuality: EnvironmentResource.CreateOptions.SamplingQuality](environmentresource/createoptions/samplingquality-swift.property.md)
  The skybox sampling quality for lighting textures.
- [var specularCubeDimension: Int?](environmentresource/createoptions/specularcubedimension.md)
  The dimension of the computed specular cubemap for material reflections.
### Comparing the options
- [static func == (EnvironmentResource.CreateOptions, EnvironmentResource.CreateOptions) -> Bool](environmentresource/createoptions/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [func hash(into: inout Hasher)](environmentresource/createoptions/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](environmentresource/createoptions/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](environmentresource/createoptions/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [EnvironmentResource.Compression](environmentresource/compression.md)
  The compression to apply when creating an environment resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/createoptions)*