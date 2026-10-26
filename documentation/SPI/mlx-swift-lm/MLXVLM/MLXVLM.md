---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm"
framework: "mlx-swift-lm/MLXVLM"
---

# MLXVLM

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: module  
**Role**: Framework

## Topics

### Classes
- [actor EmbeddingGemma2Embedding](./embeddinggemma2embedding.md)
  Embeddings of text, images, video and audio from an EmbeddingGemma 2 checkpoint, in one shared space. Load the checkpoint once and reuse this actor for every call.
- [class FastVLM](./fastvlm.md)
- [class Gemma3](./gemma3.md)
- [class Gemma4](./gemma4.md)
- [class Gemma4AssistantDraftInner](./gemma4assistantdraftinner.md)
  The drafter’s inner module — mirrors the Python `_DraftInner` so weight keys (`model.embed_tokens.weight`, `model.layers.N.*`, `model.norm.weight`) load without remapping.
- [class Gemma4AssistantDraftModel](./gemma4assistantdraftmodel.md)
  The Gemma 4 MTP drafter — a 4-layer Q-only assistant that cross-attends to the target model’s last full-attention and last sliding-attention K/V to propose K-1 tokens per round.
- [class Gemma4AssistantMaskedEmbedder](./gemma4assistantmaskedembedder.md)
  Centroid-routed sparse LM head used when `use_ordered_embeddings=true`.
- [class Gemma4Unified](./gemma4unified.md)
- [class GlmOcr](./glmocr.md)
  GlmOcr VLM
- [class Idefics3](./idefics3.md)
- [class LFM2VL](./lfm2vl.md)
  LFM2 VL VLM
- [class Mistral3VLM](./mistral3vlm.md)
- [class MuseGlimmer](./museglimmer.md)
- [class PaliGemma](./paligemma.md)
  PaliGemma VLM
- [class PixtralVLM](./pixtralvlm.md)
- [class Qwen25VL](./qwen25vl.md)
  Qwen2.5VL VLM
- [class Qwen2VL](./qwen2vl.md)
  Qwen2VL VLM
- [class Qwen35](./qwen35.md)
- [class Qwen35MoE](./qwen35moe.md)
- [class Qwen35VLMNextNDraftModel](./qwen35vlmnextndraftmodel.md)
- [class Qwen3VL](./qwen3vl.md)
- [class Qwen3VLMoE](./qwen3vlmoe.md)
- [class TrampolineModelFactory](./trampolinemodelfactory.md)
- [class VLMModelFactory](./vlmmodelfactory.md)
  Factory for creating new LLMs.
- [class VLMProcessorLoadingRegistry](./vlmprocessorloadingregistry.md)
  Ordered registry of processor-loading resolvers used by [`VLMModelFactory`](./vlmmodelfactory.md).
- [class VLMRegistry](./vlmregistry.md)
  Registry of models and any overrides that go with them, e.g. prompt augmentation. If asked for an unknown configuration this will use the model/tokenizer as-is.
### Protocols
- [protocol VLMModel](./vlmmodel.md)
- [protocol VLMProcessorLoadingResolver](./vlmprocessorloadingresolver.md)
  Supplies model-specific processor loading policy that is not present in a checkpoint.
### Structures
- [struct BaseProcessorConfiguration](./baseprocessorconfiguration.md)
- [struct FastVLMConfiguration](./fastvlmconfiguration.md)
  Configuration for [`FastVLM`](./fastvlm.md)
- [struct FastVLMMessageGenerator](./fastvlmmessagegenerator.md)
  This message generator adheres to the following format:
- [struct FastVLMProcessor](./fastvlmprocessor.md)
- [struct FastVLMProcessorConfiguration](./fastvlmprocessorconfiguration.md)
- [struct Gemma3Configuration](./gemma3configuration.md)
- [struct Gemma3Processor](./gemma3processor.md)
- [struct Gemma3ProcessorConfiguration](./gemma3processorconfiguration.md)
- [struct Gemma3TextConfiguration](./gemma3textconfiguration.md)
- [struct Gemma3VisionConfiguration](./gemma3visionconfiguration.md)
- [struct Gemma4AssistantConfiguration](./gemma4assistantconfiguration.md)
  Configuration for the Gemma 4 MTP speculative drafter.
- [struct Gemma4Configuration](./gemma4configuration.md)
  Configuration of the Gemma 4 audio encoder (`model_type: gemma4_audio`).
- [struct Gemma4MessageGenerator](./gemma4messagegenerator.md)
- [struct Gemma4Processor](./gemma4processor.md)
- [struct Gemma4ProcessorConfiguration](./gemma4processorconfiguration.md)
- [struct Gemma4TextConfiguration](./gemma4textconfiguration.md)
- [struct Gemma4UnifiedAudioConfiguration](./gemma4unifiedaudioconfiguration.md)
- [struct Gemma4UnifiedConfiguration](./gemma4unifiedconfiguration.md)
- [struct Gemma4UnifiedProcessor](./gemma4unifiedprocessor.md)
- [struct Gemma4UnifiedProcessorConfiguration](./gemma4unifiedprocessorconfiguration.md)
- [struct Gemma4UnifiedVisionConfiguration](./gemma4unifiedvisionconfiguration.md)
- [struct GlmOcrConfiguration](./glmocrconfiguration.md)
  Configuration for [`GlmOcr`](./glmocr.md)
- [struct GlmOcrMessageGenerator](./glmocrmessagegenerator.md)
  Message Generator for GlmOcr
- [struct GlmOcrProcessor](./glmocrprocessor.md)
  GlmOcr VLM `UserInputProcessor`.
- [struct GlmOcrProcessorConfiguration](./glmocrprocessorconfiguration.md)
  Configuration for [`GlmOcrProcessor`](./glmocrprocessor.md)
- [struct Idefics3Configuration](./idefics3configuration.md)
- [struct Idefics3Processor](./idefics3processor.md)
- [struct Idefics3ProcessorConfiguration](./idefics3processorconfiguration.md)
- [struct LFM2VLConfiguration](./lfm2vlconfiguration.md)
  Configuration for [`LFM2VL`](./lfm2vl.md)
- [struct LFM2VLProcessor](./lfm2vlprocessor.md)
  LFM2 VL VLM `UserInputProcessor`.
- [struct LFM2VLProcessorConfiguration](./lfm2vlprocessorconfiguration.md)
  Configuration for [`LFM2VLProcessor`](./lfm2vlprocessor.md)
- [struct Mistral3MessageGenerator](./mistral3messagegenerator.md)
  Message generator for Mistral3 VLM that creates structured messages with image placeholders
- [struct Mistral3VLMConfiguration](./mistral3vlmconfiguration.md)
- [struct Mistral3VLMProcessor](./mistral3vlmprocessor.md)
- [struct Mistral3VLMProcessorConfiguration](./mistral3vlmprocessorconfiguration.md)
- [struct Mistral3VLMTextConfiguration](./mistral3vlmtextconfiguration.md)
- [struct ModelTypeProcessorResolver](./modeltypeprocessorresolver.md)
  A reusable processor-type rule keyed by `model_type` from `config.json`.
- [struct MuseGlimmerConfiguration](./museglimmerconfiguration.md)
- [struct MuseGlimmerProcessor](./museglimmerprocessor.md)
- [struct MuseGlimmerProcessorConfiguration](./museglimmerprocessorconfiguration.md)
- [struct MuseGlimmerTextConfiguration](./museglimmertextconfiguration.md)
- [struct MuseGlimmerVisionConfiguration](./museglimmervisionconfiguration.md)
- [struct PaliGemmaConfiguration](./paligemmaconfiguration.md)
  Confguration for [`PaliGemma`](./paligemma.md)
- [struct PaliGemmaProcessor](./paligemmaprocessor.md)
  PaliGemma VLM `UserInputProcessor`.
- [struct PaliGemmaProcessorConfiguration](./paligemmaprocessorconfiguration.md)
  Configuration for [`PaliGemmaProcessor`](./paligemmaprocessor.md)
- [struct PixtralConfiguration](./pixtralconfiguration.md)
- [struct PixtralProcessor](./pixtralprocessor.md)
- [struct PixtralProcessorConfiguration](./pixtralprocessorconfiguration.md)
- [struct PixtralTextConfiguration](./pixtraltextconfiguration.md)
- [struct PixtralVisionConfiguration](./pixtralvisionconfiguration.md)
- [struct ProcessedFrames](./processedframes.md)
- [struct Qwen25VLConfiguration](./qwen25vlconfiguration.md)
  Configuration for [`Qwen25VL`](./qwen25vl.md)
- [struct Qwen25VLProcessor](./qwen25vlprocessor.md)
  Qwen2.5VL VLM `UserInputProcessor`.
- [struct Qwen25VLProcessorConfiguration](./qwen25vlprocessorconfiguration.md)
  Configuration for [`Qwen25VLProcessor`](./qwen25vlprocessor.md)
- [struct Qwen2VLConfiguration](./qwen2vlconfiguration.md)
  Configuration for [`Qwen2VL`](./qwen2vl.md)
- [struct Qwen2VLMessageGenerator](./qwen2vlmessagegenerator.md)
  Message Generator for Qwen2VL
- [struct Qwen2VLProcessor](./qwen2vlprocessor.md)
  Qwen2VL VLM `UserInputProcessor`.
- [struct Qwen2VLProcessorConfiguration](./qwen2vlprocessorconfiguration.md)
  Configuration for [`Qwen2VLProcessor`](./qwen2vlprocessor.md)
- [struct Qwen35Configuration](./qwen35configuration.md)
- [struct Qwen35ProcessorLoadingResolver](./qwen35processorloadingresolver.md)
  Reconstructs processor metadata omitted by Qwen3.5 checkpoints from their vision config.
- [struct Qwen3VLConfiguration](./qwen3vlconfiguration.md)
- [struct Qwen3VLMessageGenerator](./qwen3vlmessagegenerator.md)
- [struct Qwen3VLMoEConfiguration](./qwen3vlmoeconfiguration.md)
- [struct Qwen3VLProcessor](./qwen3vlprocessor.md)
- [struct Qwen3VLProcessorConfiguration](./qwen3vlprocessorconfiguration.md)
- [struct QwenVL](./qwenvl.md)
- [struct SmolVLM2MessageGenerator](./smolvlm2messagegenerator.md)
- [struct SmolVLMProcessor](./smolvlmprocessor.md)
- [struct SmolVLMProcessorConfiguration](./smolvlmprocessorconfiguration.md)
- [struct VLMProcessorConfiguration](./vlmprocessorconfiguration.md)
  Fully resolved input for constructing a VLM processor.
- [struct VLMProcessorLoadingContext](./vlmprocessorloadingcontext.md)
  The model metadata available while resolving how to load a VLM processor.
### Type Aliases
- [typealias EmbeddingGemma2](./embeddinggemma2.md)
  The shared EmbeddingGemma 2 encoder.
- [typealias EmbeddingGemma2Configuration](./embeddinggemma2configuration.md)
  The shared EmbeddingGemma 2 checkpoint configuration.
- [typealias Gemma4VisionConfiguration](./gemma4visionconfiguration.md)
- [typealias Mistral3VisionConfiguration](./mistral3visionconfiguration.md)
- [typealias ModelRegistry](./modelregistry.md)
- [typealias VideoFrame](./videoframe.md)
- [typealias VideoProcessing](./videoprocessing.md)
### Enumerations
- [enum Gemma4AssistantRegistration](./gemma4assistantregistration.md)
  Registers the `gemma4_assistant` model type with the shared MTP drafter type registry.
- [enum MediaProcessing](./mediaprocessing.md)
  Collection of methods for processing media (images, video, etc.).
- [enum Qwen35Language](./qwen35language.md)
- [enum Qwen35VLMMTPRegistration](./qwen35vlmmtpregistration.md)
  Registers Qwen3.5-family multimodal MTP drafter model types.
- [enum VLMError](./vlmerror.md)
- [enum VLMProcessorTypeRegistry](./vlmprocessortyperegistry.md)
- [enum VLMTypeRegistry](./vlmtyperegistry.md)
  Registry of model type, e.g ‘llama’, to functions that can instantiate the model from configuration.
### Extended Modules
- [CoreImage](./coreimage.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm)*