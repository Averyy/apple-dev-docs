---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm"
framework: "mlx-swift-lm/MLXLLM"
---

# MLXLLM

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: module  
**Role**: Framework

Example implementations of various Large Language Models (LLMs).

#### Other MLX Libraries Packages

- [MLXEmbedders](../MLXEmbedders/MLXEmbedders.md)
- [MLXLLM](./MLXLLM.md)
- [MLXLMCommon](../MLXLMCommon/MLXLMCommon.md)
- [MLXVLM](../MLXVLM/MLXVLM.md)

#### Quick Start

See [Evaluation](./evaluation.md).

Using LLMs and VLMs is as easy as this:

```swift
import MLXLMCommon
    
let downloader: any Downloader = ...
let tokenizerLoader: any TokenizerLoader = ...

let model = try await loadModel(
    from: downloader,
    using: tokenizerLoader,
    id: "mlx-community/Qwen3-4B-4bit"
)
let session = ChatSession(model)
print(try await session.respond(to: "What are two things to see in San Francisco?"))
print(try await session.respond(to: "How about a great place to eat?"))
```

See [MLXLMCommon](../MLXLMCommon/MLXLMCommon.md) for information about `Downloader` and `TokenizerLoader`.

More advanced APIs are available for those that need them, see [Using a Model](./using-model.md).

## Topics

- [Evaluation](./evaluation.md)
  The simplified LLM/VLM API allows you to load a model and evaluate prompts with only a few lines of code.
- [Adding a Model](./adding-model.md)
  If the model follows the typical LLM pattern you can add a new model in a few steps.
- [Using a Model](./using-model.md)
  Using a model is easy:  load the weights, tokenize and evaluate.
### Models
- [class CohereModel](./coheremodel.md)
- [class GemmaModel](./gemmamodel.md)
- [class Gemma2Model](./gemma2model.md)
- [class InternLM2Model](./internlm2model.md)
- [class LlamaModel](./llamamodel.md)
  Model for Llama and Mistral model types.
- [class OpenELMModel](./openelmmodel.md)
- [class PhiModel](./phimodel.md)
- [class Phi3Model](./phi3model.md)
- [class PhiMoEModel](./phimoemodel.md)
- [class Qwen2Model](./qwen2model.md)
- [class Qwen3Model](./qwen3model.md)
- [class Starcoder2Model](./starcoder2model.md)
- [class MiMoModel](./mimomodel.md)
- [class GLM4Model](./glm4model.md)
### Classes
- [class AfMoEModel](./afmoemodel.md)
- [class ApertusModel](./apertusmodel.md)
- [class BaichuanM1Model](./baichuanm1model.md)
- [class BaichuanM1ModelInner](./baichuanm1modelinner.md)
- [class BailingMoeModel](./bailingmoemodel.md)
- [class BailingMoeModelInner](./bailingmoemodelinner.md)
- [class BitnetModel](./bitnetmodel.md)
- [class BitnetModelInner](./bitnetmodelinner.md)
- [class CohereModelInner](./coheremodelinner.md)
- [class DeepseekV2Model](./deepseekv2model.md)
- [class DeepseekV2ModelInner](./deepseekv2modelinner.md)
- [class DeepseekV3Model](./deepseekv3model.md)
- [class DeepseekV3ModelInner](./deepseekv3modelinner.md)
- [class Ernie45Model](./ernie45model.md)
- [class Ernie45ModelInner](./ernie45modelinner.md)
- [class Exaone4Model](./exaone4model.md)
- [class Exaone4ModelInner](./exaone4modelinner.md)
- [class FalconH1Model](./falconh1model.md)
- [class FalconH1ModelInner](./falconh1modelinner.md)
- [class GLM4MoELiteModel](./glm4moelitemodel.md)
- [class GLM4MoELiteModelInner](./glm4moelitemodelinner.md)
- [class GLM4MoEModel](./glm4moemodel.md)
- [class GLM4MoEModelInner](./glm4moemodelinner.md)
- [class GLM4ModelInner](./glm4modelinner.md)
- [class GPTOSSModel](./gptossmodel.md)
- [class GPTOSSModelInner](./gptossmodelinner.md)
- [class Gemma2ModelInner](./gemma2modelinner.md)
- [class Gemma3Model](./gemma3model.md)
- [class Gemma3TextModel](./gemma3textmodel.md)
- [class Gemma3nLanguageModel](./gemma3nlanguagemodel.md)
- [class Gemma3nTextModel](./gemma3ntextmodel.md)
- [class Gemma4Model](./gemma4model.md)
- [class Gemma4TextModel](./gemma4textmodel.md)
- [class GemmaModelInner](./gemmamodelinner.md)
- [class GraniteModel](./granitemodel.md)
- [class GraniteModelInner](./granitemodelinner.md)
- [class GraniteMoeHybridModel](./granitemoehybridmodel.md)
- [class GraniteMoeHybridModelInner](./granitemoehybridmodelinner.md)
- [class HeliumModel](./heliummodel.md)
- [class HeliumModelInner](./heliummodelinner.md)
- [class HunyuanModel](./hunyuanmodel.md)
- [class HunyuanModelInner](./hunyuanmodelinner.md)
- [class InternLM2ModelInner](./internlm2modelinner.md)
- [class JambaModel](./jambamodel.md)
- [class JambaModelInner](./jambamodelinner.md)
- [class JinaRerankerModel](./jinarerankermodel.md)
  Jina reranker v3 listwise model.
- [class LFM2MoEModel](./lfm2moemodel.md)
- [class LFM2MoEModelInner](./lfm2moemodelinner.md)
- [class LFM2Model](./lfm2model.md)
- [class LFM2ModelInner](./lfm2modelinner.md)
- [class LLMModelFactory](./llmmodelfactory.md)
  Factory for creating new LLMs.
- [class LLMRegistry](./llmregistry.md)
  Registry of models and any overrides that go with them, e.g. prompt augmentation. If asked for an unknown configuration this will use the model/tokenizer as-is.
- [class Lille130mModel](./lille130mmodel.md)
- [class Lille130mModelInner](./lille130mmodelinner.md)
- [class LlamaModelInner](./llamamodelinner.md)
- [class Mamba2Backbone](./mamba2backbone.md)
- [class Mamba2Model](./mamba2model.md)
- [class MellumModel](./mellummodel.md)
- [class MellumModelInner](./mellummodelinner.md)
- [class MiMoModelInner](./mimomodelinner.md)
- [class MiMoV2FlashModel](./mimov2flashmodel.md)
- [class MiMoV2FlashModelInner](./mimov2flashmodelinner.md)
- [class MiniCPMModel](./minicpmmodel.md)
- [class MiniCPMModelInner](./minicpmmodelinner.md)
- [class MiniMaxModel](./minimaxmodel.md)
- [class MiniMaxModelInner](./minimaxmodelinner.md)
- [class Mistral3TextModel](./mistral3textmodel.md)
  Mistral3Text language model.
- [class Mistral3TextModelInner](./mistral3textmodelinner.md)
- [class MixtralModel](./mixtralmodel.md)
- [class MixtralModelInner](./mixtralmodelinner.md)
- [class NanbeigeModel](./nanbeigemodel.md)
- [class NanbeigeModelInner](./nanbeigemodelinner.md)
- [class NanoChatModel](./nanochatmodel.md)
- [class NanoChatModelInner](./nanochatmodelinner.md)
- [class NemotronHModel](./nemotronhmodel.md)
- [class NemotronLabsDiffusionEncoder](./nemotronlabsdiffusionencoder.md)
  The Ministral3 backbone. Weights live under `encoder.*` in the safetensors, matching the upstream Python class name `Ministral3Model` exposed as `self.encoder` on `NemotronLabsDiffusionModel`.
- [class NemotronLabsDiffusionModel](./nemotronlabsdiffusionmodel.md)
  `nvidia/Nemotron-Labs-Diffusion-3B` and family.
- [class Olmo2Model](./olmo2model.md)
- [class Olmo2ModelInner](./olmo2modelinner.md)
- [class Olmo3Model](./olmo3model.md)
- [class Olmo3ModelInner](./olmo3modelinner.md)
- [class OlmoEModel](./olmoemodel.md)
- [class OlmoEModelInner](./olmoemodelinner.md)
- [class OpenELMModelInner](./openelmmodelinner.md)
- [class Phi3ModelInner](./phi3modelinner.md)
- [class PhiMoEModelInner](./phimoemodelinner.md)
- [class PhiModelInner](./phimodelinner.md)
- [class Qwen2ModelInner](./qwen2modelinner.md)
- [class Qwen35MTPDraftModel](./qwen35mtpdraftmodel.md)
- [class Qwen35MoEModel](./qwen35moemodel.md)
- [class Qwen35Model](./qwen35model.md)
- [class Qwen35TextModel](./qwen35textmodel.md)
- [class Qwen35TextModelInner](./qwen35textmodelinner.md)
- [class Qwen3MoEModel](./qwen3moemodel.md)
- [class Qwen3MoEModelInner](./qwen3moemodelinner.md)
- [class Qwen3ModelInner](./qwen3modelinner.md)
- [class Qwen3NextAttention](./qwen3nextattention.md)
- [class Qwen3NextGatedDeltaNet](./qwen3nextgateddeltanet.md)
- [class Qwen3NextModel](./qwen3nextmodel.md)
- [class Qwen3NextModelInner](./qwen3nextmodelinner.md)
- [class SmolLM3Model](./smollm3model.md)
- [class SmolLM3ModelInner](./smollm3modelinner.md)
- [class Starcoder2ModelInner](./starcoder2modelinner.md)
- [class TrampolineModelFactory](./trampolinemodelfactory.md)
### Protocols
- [protocol LLMModel](./llmmodel.md)
  Marker protocol for LLMModels
### Structures
- [struct AfMoEConfiguration](./afmoeconfiguration.md)
- [struct ApertusConfiguration](./apertusconfiguration.md)
- [struct BaichuanM1Configuration](./baichuanm1configuration.md)
- [struct BailingMoeConfiguration](./bailingmoeconfiguration.md)
- [struct BitnetConfiguration](./bitnetconfiguration.md)
- [struct CohereConfiguration](./cohereconfiguration.md)
- [struct DeepseekV2Configuration](./deepseekv2configuration.md)
- [struct DeepseekV3Configuration](./deepseekv3configuration.md)
- [struct Ernie45Configuration](./ernie45configuration.md)
- [struct Exaone4Configuration](./exaone4configuration.md)
- [struct FalconH1Configuration](./falconh1configuration.md)
- [struct GLM4Configuration](./glm4configuration.md)
- [struct GLM4MoEConfiguration](./glm4moeconfiguration.md)
- [struct GLM4MoELiteConfiguration](./glm4moeliteconfiguration.md)
- [struct GPTOSSConfiguration](./gptossconfiguration.md)
- [struct Gemma2Configuration](./gemma2configuration.md)
- [struct Gemma3TextConfiguration](./gemma3textconfiguration.md)
- [struct Gemma3nTextConfiguration](./gemma3ntextconfiguration.md)
- [struct Gemma4Configuration](./gemma4configuration.md)
  Configuration for the `"gemma4"` model_type. This is a thin wrapper around `Gemma4TextConfiguration` that handles the nested `text_config` structure from HuggingFace model configs.
- [struct Gemma4TextConfiguration](./gemma4textconfiguration.md)
- [struct GemmaConfiguration](./gemmaconfiguration.md)
- [struct GraniteConfiguration](./graniteconfiguration.md)
- [struct GraniteMoeHybridConfiguration](./granitemoehybridconfiguration.md)
- [struct HeliumConfiguration](./heliumconfiguration.md)
- [struct HunyuanConfiguration](./hunyuanconfiguration.md)
- [struct InternLM2Configuration](./internlm2configuration.md)
- [struct JambaConfiguration](./jambaconfiguration.md)
- [struct LFM2Configuration](./lfm2configuration.md)
- [struct LFM2MoEConfiguration](./lfm2moeconfiguration.md)
- [struct Lille130mConfiguration](./lille130mconfiguration.md)
- [struct LlamaConfiguration](./llamaconfiguration.md)
- [struct Mamba2Configuration](./mamba2configuration.md)
- [struct MellumConfiguration](./mellumconfiguration.md)
- [struct MiMoConfiguration](./mimoconfiguration.md)
- [struct MiMoV2FlashConfiguration](./mimov2flashconfiguration.md)
- [struct MiniCPMConfiguration](./minicpmconfiguration.md)
- [struct MiniMaxConfiguration](./minimaxconfiguration.md)
- [struct Mistral3TextConfiguration](./mistral3textconfiguration.md)
- [struct MixtralConfiguration](./mixtralconfiguration.md)
- [struct NanbeigeConfiguration](./nanbeigeconfiguration.md)
- [struct NanoChatConfiguration](./nanochatconfiguration.md)
- [struct NemotronHConfiguration](./nemotronhconfiguration.md)
- [struct NemotronLabsDiffusionConfiguration](./nemotronlabsdiffusionconfiguration.md)
- [struct Olmo2Configuration](./olmo2configuration.md)
- [struct Olmo3Configuration](./olmo3configuration.md)
- [struct OlmoEConfiguration](./olmoeconfiguration.md)
- [struct OpenElmConfiguration](./openelmconfiguration.md)
- [struct Phi3Configuration](./phi3configuration.md)
- [struct PhiConfiguration](./phiconfiguration.md)
- [struct PhiMoEConfiguration](./phimoeconfiguration.md)
- [struct Qwen2Configuration](./qwen2configuration.md)
- [struct Qwen35Configuration](./qwen35configuration.md)
- [struct Qwen35TextConfiguration](./qwen35textconfiguration.md)
- [struct Qwen3Configuration](./qwen3configuration.md)
- [struct Qwen3MoEConfiguration](./qwen3moeconfiguration.md)
- [struct Qwen3NextConfiguration](./qwen3nextconfiguration.md)
- [struct SmolLM3Configuration](./smollm3configuration.md)
- [struct Starcoder2Configuration](./starcoder2configuration.md)
- [struct TranslateGemma3MessageGenerator](./translategemma3messagegenerator.md)
  Message generator for TranslateGemma, Google’s translation fine-tunes of Gemma 3.
### Functions
- [func computeDt(MLXArray, MLXArray, (Float, Float)) -> MLXArray](./computedt%28_,_,_%29.md)
- [func loadLoRAData(directory: URL, name: String) throws -> [String]](./loadloradata%28directory,name%29.md)
  Load a LoRA data file.
- [func loadLoRAData(url: URL) throws -> [String]](./loadloradata%28url%29.md)
  Load a .txt or .jsonl file and return the contents
- [func segsum(MLXArray, mask: MLXArray?) -> MLXArray](./segsum%28_,mask%29.md)
- [func ssmAttn(x: MLXArray, ALog: MLXArray, B: MLXArray, C: MLXArray, D: MLXArray, dt: MLXArray, dtBias: MLXArray, state: MLXArray?, timeStepLimit: (Float, Float), mask: MLXArray?, lengths: MLXArray?, step: Int) -> (MLXArray, MLXArray)](./ssmattn%28x,alog,b,c,d,dt,dtbias,state,timesteplimit,mask,lengths,step%29.md)
- [func ssmUpdate(hiddenStates: MLXArray, ALog: MLXArray, B: MLXArray, C: MLXArray, D: MLXArray, dt: MLXArray, dtBias: MLXArray, state: MLXArray?, timeStepLimit: (Float, Float), mask: MLXArray?, lengths: MLXArray?, step: Int) -> (MLXArray, MLXArray)](./ssmupdate%28hiddenstates,alog,b,c,d,dt,dtbias,state,timesteplimit,mask,lengths,step%29.md)
### Type Aliases
- [typealias ModelRegistry](./modelregistry.md)
### Enumerations
- [enum LLMTypeRegistry](./llmtyperegistry.md)
  Registry of model type, e.g ‘llama’, to functions that can instantiate the model from configuration.
- [enum LoRATrain](./loratrain.md)
  Collection of functions for adding LoRA adapters to an LLM model, training, fusing and saving/loading weights.
- [enum LoRATrainError](./loratrainerror.md)
  Errors thrown by [`train(model:train:validate:optimizer:loss:tokenizer:parameters:progress:)`](./loratrain/train%28model,train,validate,optimizer,loss,tokenizer,parameters,progress%29.md).
- [enum Qwen35TextMTPRegistration](./qwen35textmtpregistration.md)
  Registers Qwen3.5-family text MTP drafter model types.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm)*