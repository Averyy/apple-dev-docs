---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmregistry"
framework: "mlx-swift-lm/MLXVLM"
---

# VLMRegistry

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

Registry of models and any overrides that go with them, e.g. prompt augmentation. If asked for an unknown configuration this will use the model/tokenizer as-is.

## Declaration

```swift
class VLMRegistry
```

## Overview

The python tokenizers have a very rich set of implementations and configuration. The swift-tokenizers code handles a good chunk of that and this is a place to augment that implementation, if needed.

## Topics

### Type Properties
- [static let fastvlm: ModelConfiguration](./vlmregistry/fastvlm.md)
- [static let gemma3_12B_qat_4bit: ModelConfiguration](./vlmregistry/gemma3_12b_qat_4bit.md)
- [static let gemma3_27B_qat_4bit: ModelConfiguration](./vlmregistry/gemma3_27b_qat_4bit.md)
- [static let gemma3_4B_qat_4bit: ModelConfiguration](./vlmregistry/gemma3_4b_qat_4bit.md)
- [static let gemma4_26BA4B_it_4bit: ModelConfiguration](./vlmregistry/gemma4_26ba4b_it_4bit.md)
- [static let gemma4_31B_it_4bit: ModelConfiguration](./vlmregistry/gemma4_31b_it_4bit.md)
- [static let gemma4_E2B_it_4bit: ModelConfiguration](./vlmregistry/gemma4_e2b_it_4bit.md)
- [static let gemma4_E4B_it_4bit: ModelConfiguration](./vlmregistry/gemma4_e4b_it_4bit.md)
- [static let lfm2_5_vl_1_6B_4bit: ModelConfiguration](./vlmregistry/lfm2_5_vl_1_6b_4bit.md)
- [static let lfm2_vl_1_6B_4bit: ModelConfiguration](./vlmregistry/lfm2_vl_1_6b_4bit.md)
- [static let mistral3_3B_Instruct_4bit: ModelConfiguration](./vlmregistry/mistral3_3b_instruct_4bit.md)
- [static let museGlimmer30B4bit: ModelConfiguration](./vlmregistry/museglimmer30b4bit.md)
- [static let paligemma3bMix448_8bit: ModelConfiguration](./vlmregistry/paligemma3bmix448_8bit.md)
- [static let qwen2VL2BInstruct4Bit: ModelConfiguration](./vlmregistry/qwen2vl2binstruct4bit.md)
- [static let qwen2_5VL3BInstruct4Bit: ModelConfiguration](./vlmregistry/qwen2_5vl3binstruct4bit.md)
- [static let qwen3VL4BInstruct4Bit: ModelConfiguration](./vlmregistry/qwen3vl4binstruct4bit.md)
- [static let qwen3VL4BInstruct8Bit: ModelConfiguration](./vlmregistry/qwen3vl4binstruct8bit.md)
- [static let qwen3_5_27B_4bit: ModelConfiguration](./vlmregistry/qwen3_5_27b_4bit.md)
- [static let qwen3_5_35B_A3B_4bit: ModelConfiguration](./vlmregistry/qwen3_5_35b_a3b_4bit.md)
- [static let qwen3_8_27B_4bit: ModelConfiguration](./vlmregistry/qwen3_8_27b_4bit.md)
- [static let qwen3_8_27B_8bit: ModelConfiguration](./vlmregistry/qwen3_8_27b_8bit.md)
- [static let shared: VLMRegistry](./vlmregistry/shared.md)
  Shared instance with default model configurations.
- [static let smolvlm: ModelConfiguration](./vlmregistry/smolvlm.md)
- [static let smolvlminstruct4bit: ModelConfiguration](./vlmregistry/smolvlminstruct4bit.md)
### Type Methods
- [static func all() -> [ModelConfiguration]](./vlmregistry/all%28%29.md)

## Relationships

### Inherits From
- MLXLMCommon.AbstractModelRegistry
### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmregistry)*