---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftertyperegistry/visionlanguage"
framework: "mlx-swift-lm/MLXLMCommon"
---

# visionLanguage

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Type Property

Registry for drafters whose forward pass consumes multimodal position state. It is separate from [`shared`](./shared.md) because standalone Qwen MTP checkpoints intentionally ship an empty `vision_config`, so their target architecture cannot be inferred from drafter metadata alone.

## Declaration

```swift
static let visionLanguage: ModelTypeRegistry<any MTPDrafterModel>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftertyperegistry/visionlanguage)*