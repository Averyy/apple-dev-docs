# specularCubeDimension

**Framework**: RealityKit  
**Kind**: property

The dimension of the computed specular cubemap for material reflections.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var specularCubeDimension: Int?
```

#### Discussion

If `nil`, the environment resource uses the source cubemap’s dimensions.

A value lower than that of the cubemap helps to reduce the memory footprint in scenes where you view skybox details through specular reflections.

> **Note**: The specular cube dimension clamps to the source cubemap’s dimensions if it exceeds them.

## See Also

- [var compression: EnvironmentResource.Compression](environmentresource/createoptions/compression.md)
  The compression to apply to environment textures.
- [var samplingQuality: EnvironmentResource.CreateOptions.SamplingQuality](environmentresource/createoptions/samplingquality-swift.property.md)
  The skybox sampling quality for lighting textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/createoptions/specularcubedimension)*