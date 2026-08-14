# HairLightingModel

**Framework**: RealityKit  
**Kind**: struct

Configuration for RealityKit’s hair lighting model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct HairLightingModel
```

## Mentions

- [Rendering high-fidelity characters](rendering-high-fidelity-characters.md)

#### Overview

`LitLightingModel` doesn’t accurately represent hair and fur, since their thin, nearly cylindrical strands scatter light differently than a typical opaque surface. Use this lighting model for materials that shade hair or fur.

To render with the hair lighting model, set a `ShaderGraphMaterial.Program.Descriptor`’s `lightingModel` to `.hair()`:

```None
let descriptor = ShaderGraphMaterial.Program.Descriptor(shaderGraph: graph, lightingModel: .hair())
let program = try await ShaderGraphMaterial.Program(descriptor: descriptor)
```

The surface output node in the descriptor’s `ShaderGraph` must produce hair-shading output for this model to take effect.

## Topics

### Initializers
- [init()](hairlightingmodel/init.md)

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
- [struct UnlitLightingModel](unlitlightingmodel.md)
  Configuration for an unlit lighting model, which renders without any light interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hairlightingmodel)*