---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmregistry"
framework: "mlx-swift-lm/MLXLLM"
---

# LLMRegistry

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

Registry of models and any overrides that go with them, e.g. prompt augmentation. If asked for an unknown configuration this will use the model/tokenizer as-is.

## Declaration

```swift
class LLMRegistry
```

#### Overview

The Python tokenizers have a very rich set of implementations and configuration. The swift-tokenizers code handles a good chunk of that and this is a place to augment that implementation, if needed.

## Topics

### Type Properties
- [static let acereason_7b_4bit: ModelConfiguration](./llmregistry/acereason_7b_4bit.md)
- [static let baichuan_m1_14b_instruct_4bit: ModelConfiguration](./llmregistry/baichuan_m1_14b_instruct_4bit.md)
- [static let bitnet_b1_58_2b_4t_4bit: ModelConfiguration](./llmregistry/bitnet_b1_58_2b_4t_4bit.md)
- [static let codeLlama13b4bit: ModelConfiguration](./llmregistry/codellama13b4bit.md)
- [static let deepSeekR1_7B_4bit: ModelConfiguration](./llmregistry/deepseekr1_7b_4bit.md)
- [static let deepseek_r1_4bit: ModelConfiguration](./llmregistry/deepseek_r1_4bit.md)
- [static let ernie_45_0_3BPT_bf16_ft: ModelConfiguration](./llmregistry/ernie_45_0_3bpt_bf16_ft.md)
- [static let exaone_4_0_1_2b_4bit: ModelConfiguration](./llmregistry/exaone_4_0_1_2b_4bit.md)
- [static let falconH1R7B: ModelConfiguration](./llmregistry/falconh1r7b.md)
- [static let gemma2bQuantized: ModelConfiguration](./llmregistry/gemma2bquantized.md)
- [static let gemma3_1B_qat_4bit: ModelConfiguration](./llmregistry/gemma3_1b_qat_4bit.md)
- [static let gemma3n_E2B_it_lm_4bit: ModelConfiguration](./llmregistry/gemma3n_e2b_it_lm_4bit.md)
- [static let gemma3n_E2B_it_lm_bf16: ModelConfiguration](./llmregistry/gemma3n_e2b_it_lm_bf16.md)
- [static let gemma3n_E4B_it_lm_4bit: ModelConfiguration](./llmregistry/gemma3n_e4b_it_lm_4bit.md)
- [static let gemma3n_E4B_it_lm_bf16: ModelConfiguration](./llmregistry/gemma3n_e4b_it_lm_bf16.md)
- [static let gemma4_e2b_it_4bit: ModelConfiguration](./llmregistry/gemma4_e2b_it_4bit.md)
- [static let gemma4_e4b_it_4bit: ModelConfiguration](./llmregistry/gemma4_e4b_it_4bit.md)
- [static let gemma_2_2b_it_4bit: ModelConfiguration](./llmregistry/gemma_2_2b_it_4bit.md)
- [static let gemma_2_9b_it_4bit: ModelConfiguration](./llmregistry/gemma_2_9b_it_4bit.md)
- [static let glm4_9b_4bit: ModelConfiguration](./llmregistry/glm4_9b_4bit.md)
- [static let gpt_oss_20b_MXFP4_Q8: ModelConfiguration](./llmregistry/gpt_oss_20b_mxfp4_q8.md)
- [static let granite3_3_2b_4bit: ModelConfiguration](./llmregistry/granite3_3_2b_4bit.md)
- [static let granite_4_0_h_tiny_4bit_dwq: ModelConfiguration](./llmregistry/granite_4_0_h_tiny_4bit_dwq.md)
- [static let helium_1_2b_4bit: ModelConfiguration](./llmregistry/helium_1_2b_4bit.md)
- [static let hunyuan_mt_7b_4bit: ModelConfiguration](./llmregistry/hunyuan_mt_7b_4bit.md)
- [static let hunyuan_mt_7b_8bit: ModelConfiguration](./llmregistry/hunyuan_mt_7b_8bit.md)
- [static let hy_mt2_7b_4bit: ModelConfiguration](./llmregistry/hy_mt2_7b_4bit.md)
- [static let hy_mt2_7b_8bit: ModelConfiguration](./llmregistry/hy_mt2_7b_8bit.md)
- [static let jamba_3b_4bit: ModelConfiguration](./llmregistry/jamba_3b_4bit.md)
- [static let jina_reranker_v3_mlx: ModelConfiguration](./llmregistry/jina_reranker_v3_mlx.md)
- [static let lfm2_1_2b_4bit: ModelConfiguration](./llmregistry/lfm2_1_2b_4bit.md)
- [static let lfm2_8b_a1b_3bit_mlx: ModelConfiguration](./llmregistry/lfm2_8b_a1b_3bit_mlx.md)
- [static let lille_130m_bf16: ModelConfiguration](./llmregistry/lille_130m_bf16.md)
- [static let ling_mini_2_2bit: ModelConfiguration](./llmregistry/ling_mini_2_2bit.md)
- [static let llama3_1_8B_4bit: ModelConfiguration](./llmregistry/llama3_1_8b_4bit.md)
- [static let llama3_2_1B_4bit: ModelConfiguration](./llmregistry/llama3_2_1b_4bit.md)
- [static let llama3_2_3B_4bit: ModelConfiguration](./llmregistry/llama3_2_3b_4bit.md)
- [static let llama3_8B_4bit: ModelConfiguration](./llmregistry/llama3_8b_4bit.md)
- [static let mellum2_1_12b_a2_5b_thinking_6bit: ModelConfiguration](./llmregistry/mellum2_1_12b_a2_5b_thinking_6bit.md)
- [static let mimo_7b_sft_4bit: ModelConfiguration](./llmregistry/mimo_7b_sft_4bit.md)
- [static let mistral7B4bit: ModelConfiguration](./llmregistry/mistral7b4bit.md)
- [static let mistralNeMo4bit: ModelConfiguration](./llmregistry/mistralnemo4bit.md)
- [static let nanochat_d20_mlx: ModelConfiguration](./llmregistry/nanochat_d20_mlx.md)
- [static let nemotron_labs_diffusion_3b_4bit: ModelConfiguration](./llmregistry/nemotron_labs_diffusion_3b_4bit.md)
- [static let olmo_2_1124_7B_Instruct_4bit: ModelConfiguration](./llmregistry/olmo_2_1124_7b_instruct_4bit.md)
- [static let olmoe_1b_7b_0125_instruct_4bit: ModelConfiguration](./llmregistry/olmoe_1b_7b_0125_instruct_4bit.md)
- [static let openelm270m4bit: ModelConfiguration](./llmregistry/openelm270m4bit.md)
- [static let phi3_5MoE: ModelConfiguration](./llmregistry/phi3_5moe.md)
- [static let phi3_5_4bit: ModelConfiguration](./llmregistry/phi3_5_4bit.md)
- [static let phi4bit: ModelConfiguration](./llmregistry/phi4bit.md)
- [static let qwen205b4bit: ModelConfiguration](./llmregistry/qwen205b4bit.md)
- [static let qwen2_5_1_5b: ModelConfiguration](./llmregistry/qwen2_5_1_5b.md)
- [static let qwen2_5_7b: ModelConfiguration](./llmregistry/qwen2_5_7b.md)
- [static let qwen3MoE_30b_a3b_4bit: ModelConfiguration](./llmregistry/qwen3moe_30b_a3b_4bit.md)
- [static let qwen3_0_6b_4bit: ModelConfiguration](./llmregistry/qwen3_0_6b_4bit.md)
- [static let qwen3_1_7b_4bit: ModelConfiguration](./llmregistry/qwen3_1_7b_4bit.md)
- [static let qwen3_4b_4bit: ModelConfiguration](./llmregistry/qwen3_4b_4bit.md)
- [static let qwen3_5_2b_4bit: ModelConfiguration](./llmregistry/qwen3_5_2b_4bit.md)
- [static let qwen3_6_27b_4bit: ModelConfiguration](./llmregistry/qwen3_6_27b_4bit.md)
- [static let qwen3_8_27b_4bit: ModelConfiguration](./llmregistry/qwen3_8_27b_4bit.md)
- [static let qwen3_8_27b_8bit: ModelConfiguration](./llmregistry/qwen3_8_27b_8bit.md)
- [static let qwen3_8b_4bit: ModelConfiguration](./llmregistry/qwen3_8b_4bit.md)
- [static let shared: LLMRegistry](./llmregistry/shared.md)
  Shared instance with default model configurations.
- [static let smolLM_135M_4bit: ModelConfiguration](./llmregistry/smollm_135m_4bit.md)
- [static let smollm3_3b_4bit: ModelConfiguration](./llmregistry/smollm3_3b_4bit.md)
- [static let translategemma_12b_it_4bit: ModelConfiguration](./llmregistry/translategemma_12b_it_4bit.md)
- [static let translategemma_12b_it_8bit: ModelConfiguration](./llmregistry/translategemma_12b_it_8bit.md)
- [static let translategemma_27b_it_4bit: ModelConfiguration](./llmregistry/translategemma_27b_it_4bit.md)
- [static let translategemma_27b_it_8bit: ModelConfiguration](./llmregistry/translategemma_27b_it_8bit.md)
- [static let translategemma_4b_it_4bit: ModelConfiguration](./llmregistry/translategemma_4b_it_4bit.md)
- [static let translategemma_4b_it_8bit: ModelConfiguration](./llmregistry/translategemma_4b_it_8bit.md)

## Relationships

### Inherits From
- MLXLMCommon.AbstractModelRegistry
### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmregistry)*