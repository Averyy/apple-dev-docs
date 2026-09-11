# UnlitLightingModel

**Framework**: RealityKit  
**Kind**: struct

Configuration for an unlit lighting model, which renders without any light interaction.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct UnlitLightingModel
```

## Topics

### Configuring tone mapping
- [var isTonemappingEnabled: Bool](unlitlightingmodel/istonemappingenabled.md)
  Whether to apply tonemapping to this material’s output.
### Initializers
- [init()](unlitlightingmodel/init.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum LightingModel](lightingmodel.md)
  The lighting model used by a [`ShaderGraphMaterial.Program`](shadergraphmaterial/program-swift.struct.md).
- [struct LitLightingModel](litlightingmodel.md)
  Configuration for RealityKit’s physically based lighting model.
- [struct HairLightingModel](hairlightingmodel.md)
  Configuration for RealityKit’s hair lighting model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitlightingmodel)*