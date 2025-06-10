# shader(_:)

**Framework**: RealityKit  
**Kind**: method

Returns a hover effect style that applies hover state data to a custom shader that applies to the entity’s model.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static func shader(_ inputs: HoverEffectComponent.ShaderHoverEffectInputs) -> HoverEffectComponent.HoverEffect
```

#### Discussion

The custom shader can be either MaterialX or [`CustomMaterial`](custommaterial.md).

> ⚠️ **Warning**: This style doesn’t display anything without an appropriate custom shader.

## Parameters

- `inputs`: A   instance that allows you to customize various aspects of this hover effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hovereffectcomponent/hovereffect-swift.struct/shader(_:))*