---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# LLMModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: protocol  
**Role**: Protocol

Marker protocol for LLMModels

## Declaration

```swift
protocol LLMModel : LanguageModel, LoRAModel
```

## Topics

### Instance Methods
- [func messageGenerator(tokenizer: Tokenizer) -> MessageGenerator](./llmmodel/messagegenerator%28tokenizer%29.md)
  Models can implement this is they need a custom `MessageGenerator`.

## Relationships

### Inherits From
- MLXLMCommon.BaseLanguageModel
- MLXLMCommon.ChatConventionsProviding
- MLXLMCommon.LanguageModel
- MLXLMCommon.LoRAModel
### Conforming Types
- [AfMoEModel](./afmoemodel.md)
- [ApertusModel](./apertusmodel.md)
- [BaichuanM1Model](./baichuanm1model.md)
- [BailingMoeModel](./bailingmoemodel.md)
- [BitnetModel](./bitnetmodel.md)
- [CohereModel](./coheremodel.md)
- [DeepseekV2Model](./deepseekv2model.md)
- [DeepseekV3Model](./deepseekv3model.md)
- [Ernie45Model](./ernie45model.md)
- [Exaone4Model](./exaone4model.md)
- [FalconH1Model](./falconh1model.md)
- [GLM4MoELiteModel](./glm4moelitemodel.md)
- [GLM4MoEModel](./glm4moemodel.md)
- [GLM4Model](./glm4model.md)
- [GPTOSSModel](./gptossmodel.md)
- [Gemma2Model](./gemma2model.md)
- [Gemma3TextModel](./gemma3textmodel.md)
- [Gemma3nTextModel](./gemma3ntextmodel.md)
- [Gemma4Model](./gemma4model.md)
- [Gemma4TextModel](./gemma4textmodel.md)
- [GemmaModel](./gemmamodel.md)
- [GraniteModel](./granitemodel.md)
- [GraniteMoeHybridModel](./granitemoehybridmodel.md)
- [HeliumModel](./heliummodel.md)
- [HunyuanModel](./hunyuanmodel.md)
- [InternLM2Model](./internlm2model.md)
- [JambaModel](./jambamodel.md)
- [LFM2MoEModel](./lfm2moemodel.md)
- [LFM2Model](./lfm2model.md)
- [Lille130mModel](./lille130mmodel.md)
- [LlamaModel](./llamamodel.md)
- [Mamba2Model](./mamba2model.md)
- [MellumModel](./mellummodel.md)
- [MiMoModel](./mimomodel.md)
- [MiMoV2FlashModel](./mimov2flashmodel.md)
- [MiniCPMModel](./minicpmmodel.md)
- [MiniMaxModel](./minimaxmodel.md)
- [Mistral3TextModel](./mistral3textmodel.md)
- [MixtralModel](./mixtralmodel.md)
- [NanbeigeModel](./nanbeigemodel.md)
- [NanoChatModel](./nanochatmodel.md)
- [NemotronHModel](./nemotronhmodel.md)
- [NemotronLabsDiffusionModel](./nemotronlabsdiffusionmodel.md)
- [Olmo2Model](./olmo2model.md)
- [Olmo3Model](./olmo3model.md)
- [OlmoEModel](./olmoemodel.md)
- [OpenELMModel](./openelmmodel.md)
- [Phi3Model](./phi3model.md)
- [PhiMoEModel](./phimoemodel.md)
- [PhiModel](./phimodel.md)
- [Qwen2Model](./qwen2model.md)
- [Qwen35MoEModel](./qwen35moemodel.md)
- [Qwen35Model](./qwen35model.md)
- [Qwen35TextModel](./qwen35textmodel.md)
- [Qwen3MoEModel](./qwen3moemodel.md)
- [Qwen3Model](./qwen3model.md)
- [Qwen3NextModel](./qwen3nextmodel.md)
- [SmolLM3Model](./smollm3model.md)
- [Starcoder2Model](./starcoder2model.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmmodel)*