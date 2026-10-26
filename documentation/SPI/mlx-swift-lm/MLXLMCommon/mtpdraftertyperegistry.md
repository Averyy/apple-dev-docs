---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftertyperegistry"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MTPDrafterTypeRegistry

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Registry of `model_type` strings (e.g. `"gemma4_assistant"`) to creator closures that instantiate [`MTPDrafterModel`](./mtpdraftermodel.md) instances from `config.json` data.

## Declaration

```swift
enum MTPDrafterTypeRegistry
```

#### Overview

Empty at bootstrap because drafter implementations live in MLXVLM — importing them here would create a circular dependency. Downstream modules call [`registerModelType(_:creator:)`](./modeltyperegistry/registermodeltype%28_,creator%29.md) on the shared registry at app/import time. See `Gemma4AssistantRegistration` in MLXVLM.

Note: [`ModelTypeRegistry`](./modeltyperegistry.md) is an `actor`; registration is `async`.

## Topics

### Type Properties
- [static let shared: ModelTypeRegistry<any MTPDrafterModel>](./mtpdraftertyperegistry/shared.md)
  Shared registry. Empty until a downstream module registers a drafter type via `await MTPDrafterTypeRegistry.shared.registerModelType(...)`.
- [static let visionLanguage: ModelTypeRegistry<any MTPDrafterModel>](./mtpdraftertyperegistry/visionlanguage.md)
  Registry for drafters whose forward pass consumes multimodal position state. It is separate from [`shared`](./mtpdraftertyperegistry/shared.md) because standalone Qwen MTP checkpoints intentionally ship an empty `vision_config`, so their target architecture cannot be inferred from drafter metadata alone.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftertyperegistry)*