---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/deepseekr1conventionsresolver"
framework: "mlx-swift-lm/MLXLMCommon"
---

# DeepSeekR1ConventionsResolver

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Recognizes DeepSeek-R1 and its distills by repo id.

## Declaration

```swift
struct DeepSeekR1ConventionsResolver
```

## Overview

Two reasons this cannot be a model declaration:

- R1-Distill checkpoints report a base `model_type` (`qwen2` / `llama`), which is indistinguishable from plain Qwen2.5 / Llama.
- R1 proper reports `deepseek_v3`, an architecture it shares with DeepSeek-V3. Always-on reasoning belongs to the R1 checkpoints and their chat template, not to that architecture, so declaring it on `DeepseekV3Model` would wrongly advertise reasoning for plain V3.

## Topics

### Initializers
- [init()](./deepseekr1conventionsresolver/init%28%29.md)
### Instance Methods
- [func reasoningConfig(modelId: String, modelType: String) -> ReasoningConfig?](./deepseekr1conventionsresolver/reasoningconfig%28modelid,modeltype%29.md)
### Default Implementations
- [ChatConventionsResolving Implementations](./deepseekr1conventionsresolver/chatconventionsresolving-implementations.md)

## Relationships

### Conforms To
- [ChatConventionsResolving](./chatconventionsresolving.md)
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/deepseekr1conventionsresolver)*