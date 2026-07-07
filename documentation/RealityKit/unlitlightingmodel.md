# UnlitLightingModel

**Framework**: RealityKit  
**Kind**: struct

Configuration for an unlit lighting model, which renders without any light interaction.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum LightingModel](lightingmodel.md)
  The lighting model used by a [`ShaderGraphMaterial.Program`](shadergraphmaterial/program-swift.struct.md).
- [struct LitLightingModel](litlightingmodel.md)
  Configuration for RealityKit’s physically based lighting model.
- [struct HairLightingModel](hairlightingmodel.md)
  Configuration for RealityKit’s hair lighting model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitlightingmodel)*