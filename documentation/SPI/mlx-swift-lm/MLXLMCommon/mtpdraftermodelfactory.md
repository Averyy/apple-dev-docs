---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodelfactory"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MTPDrafterModelFactory

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Loader for [`MTPDrafterModel`](./mtpdraftermodel.md) checkpoints. Mirrors `LLMModelFactory` in shape, but produces an [`MTPDrafterContext`](./mtpdraftercontext.md) (no tokenizer, no user input processor, no message generator — drafters borrow their target’s tokenizer).

## Declaration

```swift
final class MTPDrafterModelFactory
```

## Topics

### Initializers
- [init(typeRegistry: ModelTypeRegistry<any MTPDrafterModel>, modelRegistry: AbstractModelRegistry)](./mtpdraftermodelfactory/init%28typeregistry,modelregistry%29.md)
### Instance Properties
- [let modelRegistry: AbstractModelRegistry](./mtpdraftermodelfactory/modelregistry.md)
- [let typeRegistry: ModelTypeRegistry<any MTPDrafterModel>](./mtpdraftermodelfactory/typeregistry.md)
### Type Aliases
- [MTPDrafterModelFactory.ContainerType](./mtpdraftermodelfactory/containertype.md)
- [MTPDrafterModelFactory.ContextType](./mtpdraftermodelfactory/contexttype.md)
### Type Properties
- [static let shared: MTPDrafterModelFactory](./mtpdraftermodelfactory/shared.md)
- [static let visionLanguage: MTPDrafterModelFactory](./mtpdraftermodelfactory/visionlanguage.md)
  Loader for multimodal drafters. Use this factory when the verifier was loaded by `VLMModelFactory` and can emit multimodal RoPE deltas.
### Default Implementations
- [GenericModelFactory Implementations](./mtpdraftermodelfactory/genericmodelfactory-implementations.md)

## Relationships

### Conforms To
- [GenericModelFactory](./genericmodelfactory.md)
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodelfactory)*