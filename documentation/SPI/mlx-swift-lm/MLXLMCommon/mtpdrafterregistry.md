---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdrafterregistry"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MTPDrafterRegistry

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Registry of model id (e.g. `"mlx-community/gemma-4-31B-it-assistant-bf16"`) to [`ModelConfiguration`](./modelconfiguration.md). Drafters don’t have prompts, so the configurations omit `defaultPrompt`.

## Declaration

```swift
class MTPDrafterRegistry
```

## Topics

### Type Properties
- [static let gemma4_26B_assistant_bf16: ModelConfiguration](./mtpdrafterregistry/gemma4_26b_assistant_bf16.md)
- [static let gemma4_31B_assistant_bf16: ModelConfiguration](./mtpdrafterregistry/gemma4_31b_assistant_bf16.md)
- [static let qwen3_8_27b_mtp_4bit: ModelConfiguration](./mtpdrafterregistry/qwen3_8_27b_mtp_4bit.md)
- [static let shared: MTPDrafterRegistry](./mtpdrafterregistry/shared.md)

## Relationships

### Inherits From
- [AbstractModelRegistry](./abstractmodelregistry.md)
### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdrafterregistry)*