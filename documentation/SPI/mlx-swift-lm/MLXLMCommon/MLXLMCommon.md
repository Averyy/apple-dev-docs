---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MLXLMCommon

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: module  
**Role**: Framework

Common language model code.

## Articles

- [Model Compatibility](./model-compatibility.md)
- [Upgrade From 2.x Release](./upgrade.md)
- [Wired Memory and Weight Reservations](./wired-memory.md)
- [KV Cache Quantization](./kv-cache-quantization.md)
- [Observing token log probabilities](./generation-observability.md)

## Reranking

- [`Reranker`](./reranker.md)
- [`RerankerContainer`](./rerankercontainer.md)
- [`RerankRequest`](./rerankrequest.md)
- [`RerankDocument`](./rerankdocument.md)
- [`RerankResult`](./rerankresult.md)
- [`RerankedDocument`](./rerankeddocument.md)
- [`RerankResponse`](./rerankresponse.md)
- [`RerankDocumentsResponse`](./rerankdocumentsresponse.md)
- [`RerankExecutionOptions`](./rerankexecutionoptions.md)
- [`RerankTruncationPolicy`](./reranktruncationpolicy.md)
- [`RerankScoreKind`](./rerankscorekind.md)
- [`RerankerError`](./rerankererror.md)

## Other MLX Libraries Packages

- [MLXEmbedders](../MLXEmbedders/MLXEmbedders.md)
- [MLXLLM](../MLXLLM/MLXLLM.md)
- [MLXLMCommon](./MLXLMCommon.md)
- [MLXVLM](../MLXVLM/MLXVLM.md)

## Topics

### Articles
- [Developing mlx-swift-lm](./developing.md)
  Techniques for developing *in* mlx-swift-lm.
- [KV Cache Quantization](./kv-cache-quantization.md)
  Reduce the memory footprint of long-context generation by compressing the key/value cache.
- [Model Compatibility](./model-compatibility.md)
  How to decide whether a model repository can be loaded by mlx-swift-lm.
- [Observing token log probabilities](./generation-observability.md)
  Compose a token handler to observe generation without changing ordinary text or tool-call events.
- [Porting Models](./porting.md)
  There are a number of ways to implement new models in MLX in Swift:
- [Upgrade From 2.x Release](./upgrade.md)
  Notes on upgrading from mlx-swift-lm 2.x releases.
- [Using mlx-swift-lm](./using.md)
  How to use mlx-swift-lm in your own tools and applications
- [Wired Memory and Weight Reservations](./wired-memory.md)
  MLXLMCommon exposes wired memory policies and tickets to help coordinate a single process-wide wired memory limit during inference. Policies decide whether work should be admitted and what wired limit is needed; tickets represent active or reserved memory usage and are registered with the `WiredMemoryManager`.
### Classes
- [class AbstractModelRegistry](./abstractmodelregistry.md)
- [class AnyOnDemandComponent](./anyondemandcomponent.md)
  A model component that loads the first time it is used. See [`OnDemandComponent`](./ondemandcomponent.md).
- [class ArraysCache](./arrayscache.md)
  Base cache for array-based state storage
- [class BaseKVCache](./basekvcache.md)
  Base cache implementation providing default behaviors
- [class CacheList](./cachelist.md)
  Composite cache that manages multiple sub-caches
- [class ChatConventionsRegistry](./chatconventionsregistry.md)
  Ordered registry of [`ChatConventionsResolving`](./chatconventionsresolving.md) consulted by the model factories.
- [class ChatSession](./chatsession.md)
  Simplified API for multi-turn conversations with LLMs and VLMs.
- [class ChunkedKVCache](./chunkedkvcache.md)
  Chunked KV cache for processing large contexts in chunks
- [class CompiledTrace](./compiledtrace.md)
  A compiled trace of a body that reads module weights.
- [class DoRALinear](./doralinear.md)
  Implementation of DoRA `Linear` replacement layer.
- [class DynamicNTKAlphaRoPE](./dynamicntkalpharope.md)
  RoPE whose base is rescaled once by `alpha^(dim/(dim-2))` (Hunyuan’s static NTK scaling).
- [class EmbeddingGemma2](./embeddinggemma2.md)
  EmbeddingGemma 2: a bidirectional text encoder with per-layer embeddings that maps text and the soft tokens of images, video frames and audio into one normalized [`embeddingDim`](./embeddinggemma2configuration/embeddingdim.md) space. Load checkpoints with `loadWeights`. Vision and audio load independently on first use by default; keep the checkpoint files readable until then.
- [class FusedGateUpSwitchGLU](./fusedgateupswitchglu.md)
  SwitchGLU variant for models that ship a single fused `gate_up_proj` weight of shape `[numExperts, 2*hiddenDims, inputDims]` instead of separate `gate_proj` / `up_proj`. Used by Gemma 4 26B MoE.
- [class KVCacheSimple](./kvcachesimple.md)
  Standard KV cache implementation based on Python’s KVCache See https://github.com/ml-explore/mlx-examples/blob/main/llms/mlx_lm/models/base.py#L11
- [class Llama3RoPE](./llama3rope.md)
- [class LoRALinear](./loralinear.md)
  Implementation of LoRA `Linear` replacement layer.
- [class MTPDrafterContainer](./mtpdraftercontainer.md)
  Sendable container for an [`MTPDrafterContext`](./mtpdraftercontext.md).
- [class MTPDrafterModelFactory](./mtpdraftermodelfactory.md)
  Loader for [`MTPDrafterModel`](./mtpdraftermodel.md) checkpoints. Mirrors `LLMModelFactory` in shape, but produces an [`MTPDrafterContext`](./mtpdraftercontext.md) (no tokenizer, no user input processor, no message generator — drafters borrow their target’s tokenizer).
- [class MTPDrafterRegistry](./mtpdrafterregistry.md)
  Registry of model id (e.g. `"mlx-community/gemma-4-31B-it-assistant-bf16"`) to [`ModelConfiguration`](./modelconfiguration.md). Drafters don’t have prompts, so the configurations omit `defaultPrompt`.
- [class MambaCache](./mambacache.md)
  Simple cache for Mamba-style state space models
- [class ModelAdapterFactory](./modeladapterfactory.md)
  A factory responsible for loading and creating model adapters from configurations.
- [class ModelAdapterTypeRegistry](./modeladaptertyperegistry.md)
- [class ModelContainer](./modelcontainer.md)
  Container for models that guarantees single threaded access.
- [class ModelFactoryRegistry](./modelfactoryregistry.md)
  Registry of [`ModelFactory`](./modelfactory.md) trampolines.
- [actor ModelTypeRegistry](./modeltyperegistry.md)
- [class OnDemandComponent](./ondemandcomponent.md)
  A model component of type `Content` that loads the first time it is used.
- [class PairwiseRotation](./pairwiserotation.md)
  Standalone pairwise Givens rotation over the last axis of an activation tensor, fused with per-channel scaling in a single Metal kernel.
- [actor ProcessorTypeRegistry](./processortyperegistry.md)
- [class ProportionalRoPE](./proportionalrope.md)
- [class QDoRALinear](./qdoralinear.md)
  Implementation of DoRA `QuantizedLinear` replacement layer.
- [class QLoRALinear](./qloralinear.md)
  Implementation of LoRA `QuantizedLinear` replacement layer.
- [class QuantizedKVCache](./quantizedkvcache.md)
  Quantized KV cache for memory efficiency using MLX quantization
- [class QuantizedSwitchLinear](./quantizedswitchlinear.md)
- [class RerankerContainer](./rerankercontainer.md)
  A thread-safe, type-erased reranker returned by model factories.
- [class RotateQuantizedLinear](./rotatequantizedlinear.md)
  Pairwise Givens rotation + quantized matmul.
- [class RotateSwitchGLU](./rotateswitchglu.md)
  `SwitchGLU` with shared pairwise Givens rotations injected around the expert projections — the PARO MoE expert block (mirrors upstream z-lab `RotateSwitchGLU`, paroquant `modules.py`).
- [class RotatingKVCache](./rotatingkvcache.md)
  Rotating KV cache for sliding window attention
- [class SuScaledRoPE](./suscaledrope.md)
  Su Scaled Rotary Position Embedding.
- [class SwitchGLU](./switchglu.md)
- [class SwitchLinear](./switchlinear.md)
- [class ToolCallProcessor](./toolcallprocessor.md)
  Processes generated text to detect and extract tool calls during streaming generation.
- [class TurboQuantKVCache](./turboquantkvcache.md)
  KV cache using TurboQuant compression with two-phase architecture:
- [class VarianceNormalizedKVCache](./variancenormalizedkvcache.md)
  Variance-normalized KV cache following KVarN’s core tile-compression steps.
- [class YarnRoPE](./yarnrope.md)
### Protocols
- [protocol AdditionalWeightFilesProviding](./additionalweightfilesproviding.md)
  Weight files a model needs that no naming convention or `model.safetensors.index.json` selects.
- [protocol AuxiliaryKVCache](./auxiliarykvcache.md)
  A cache entry that holds no attention state, such as a record of the tokens processed so far.
- [protocol BaseLanguageModel](./baselanguagemodel.md)
  Abstract form of a model that processes language.
- [protocol BatchPositionedKVCache](./batchpositionedkvcache.md)
  Protocol for KV caches that expose per-sequence RoPE offsets.
- [protocol ChatConventionsProviding](./chatconventionsproviding.md)
  A model’s chat conventions: how it encodes tool calls and how it reasons.
- [protocol ChatConventionsResolving](./chatconventionsresolving.md)
  Resolves a model’s chat conventions from identity signals the model instance cannot see for itself, today the Hugging Face repo id.
- [protocol CompiledTraceInvalidating](./compiledtraceinvalidating.md)
  Something `Module.invalidateCompiledTraces()` can reset: a [`CompiledTrace`](./compiledtrace.md) or a container of them.
- [protocol Downloader](./downloader.md)
  A protocol for downloading model repository snapshots to local directories.
- [protocol GenerationProviding](./generationproviding.md)
  Provides the base event that a chat session uses to maintain its state.
- [protocol GenerationTransformer](./generationtransformer.md)
  Configures a chat request and composes its per-pass token handlers.
- [protocol GenericModelFactory](./genericmodelfactory.md)
  Protocol for code that can load models.
- [protocol KVCache](./kvcache.md)
  Implementation of KV cache functionality for MLX Swift
- [protocol KVCacheAttentionProtocol](./kvcacheattentionprotocol.md)
  Protocol for caches that can update and compute attention from their own storage layout.
- [protocol KVCacheDimensionProvider](./kvcachedimensionprovider.md)
  Optional protocol that can be implemented by [`LanguageModel`](./languagemodel.md) and will provide an automatic implementation of [`newCache(parameters:)`](./languagemodel/newcache%28parameters%29.md)
- [protocol LanguageModel](./languagemodel.md)
  Interface for all Language Models (e.g. LLM, VLM).
- [protocol LoRALayer](./loralayer.md)
  A protocol representing a module that includes a LoRA adapter and can be converted back to its original, unadapted form.
- [protocol LoRAModel](./loramodel.md)
- [protocol LogitProcessor](./logitprocessor.md)
  A `LogitProcessor` is an optional visitor of `logits`.
- [protocol LogitSampler](./logitsampler.md)
  A `LogitSampler` is responsible for sampling `logits` produced by a [`LanguageModel`](./languagemodel.md) to produce a token.
- [protocol MTPDrafterModel](./mtpdraftermodel.md)
  Protocol for Multi-Token Prediction (MTP) speculative drafter models.
- [protocol MTPStatsCollecting](./mtpstatscollecting.md)
  Introspection surface for token iterators that perform MTP speculative decoding.
- [protocol MessageGenerator](./messagegenerator.md)
  Protocol for something that can convert structured [`Chat.Message`](./chat/message.md) into model specific [`Message`](./message.md) (raw dictionary) format.
- [protocol ModelAdapter](./modeladapter.md)
  Protocol defining an adapter that can modify a `LanguageModel`.
- [protocol ModelComponentsProviding](./modelcomponentsproviding.md)
  A model with components that can load separately or not at all.
- [protocol ModelConfigurationValidating](./modelconfigurationvalidating.md)
- [protocol ModelConversionMetadataProvider](./modelconversionmetadataprovider.md)
  Optional metadata a model wants written into converted safetensors.
- [protocol ModelFactoryTrampoline](./modelfactorytrampoline.md)
  Protocol for types that can provide ModelFactory instances.
- [protocol PreparedInputSplitting](./preparedinputsplitting.md)
  A model that can split its own prepared input at a token boundary, keeping only the media whose placeholders fall in the suffix.
- [protocol QuantizedKVCacheProtocol](./quantizedkvcacheprotocol.md)
  Protocol for caches that support efficient quantized operations
- [protocol Reranker](./reranker.md)
  Architecture-neutral interface for local reranker models.
- [protocol SpeculativeCacheRewindModel](./speculativecacherewindmodel.md)
  Target-side capability for rewinding an in-place speculative verify pass.
- [protocol StatefulMTPDrafterModel](./statefulmtpdraftermodel.md)
  Optional capability for MTP drafters that maintain per-stream state.
- [protocol StreamingDetokenizer](./streamingdetokenizer.md)
  Decodes one generated sequence. Preserve special tokens for downstream protocol parsing. `next()` returns available text, or nil until more tokens arrive. Custom implementations should emit stable text, holding incomplete bytes or context-dependent suffixes as needed.
- [protocol SuppressedTokensProviding](./suppressedtokensproviding.md)
  A language model that exposes token IDs that must never be sampled during generation.
- [protocol TokenIteratorProtocol](./tokeniteratorprotocol.md)
  Common properties shared by token-generating iterators.
- [protocol TokenLoopHandler](./tokenloophandler.md)
  Converts generated tokens into stream events.
- [protocol Tokenizer](./tokenizer.md)
  A protocol for tokenizing text into token IDs and decoding token IDs into text.
- [protocol TokenizerLoader](./tokenizerloader.md)
  A protocol for loading tokenizers from local directories.
- [protocol ToolCallParser](./toolcallparser.md)
  Protocol for parsing tool call content from model output.
- [protocol ToolProtocol](./toolprotocol.md)
  Protocol defining the requirements for a tool.
- [protocol UserInputProcessor](./userinputprocessor.md)
  Protocol for a type that can convert [`UserInput`](./userinput.md) to [`LMInput`](./lminput.md).
### Structures
- [struct ATEMToolCallParser](./atemtoolcallparser.md)
  Parser for Muse Glimmer’s Onyx ATEM tool-call format.
- [struct AffineKVCacheConfiguration](./affinekvcacheconfiguration.md)
  Affine cache compression settings.
- [struct ArgMaxSampler](./argmaxsampler.md)
  Sampler that uses `argMax` (most likely) to sample the logits.
- [struct BaseConfiguration](./baseconfiguration.md)
  The fundamental configuration for any MLX-based model.
- [struct CategoricalSampler](./categoricalsampler.md)
  Sampler that uses `temperature` to sample the logits.
- [struct ChainedLogitProcessor](./chainedlogitprocessor.md)
  Processor that applies multiple [`LogitProcessor`](./logitprocessor.md) instances in order.
- [struct CheckpointComponent](./checkpointcomponent.md)
  A checkpoint component’s serialized namespaces and runtime destination.
- [struct CheckpointNameMapping](./checkpointnamemapping.md)
  Ordered module-path mappings shared by tensors and per-layer quantization settings.
- [struct DeepSeekR1ConventionsResolver](./deepseekr1conventionsresolver.md)
  Recognizes DeepSeek-R1 and its distills by repo id.
- [struct DefaultMessageGenerator](./defaultmessagegenerator.md)
  Default implementation of [`MessageGenerator`](./messagegenerator.md) that produces `role` and `content`, plus `name`, `tool_call_id`, `tool_calls`, and `reasoning_content` when present.
- [struct DeferredTokenLogProbabilities](./deferredtokenlogprobabilities.md)
  Log probabilities for one generated token that are still on the GPU.
- [struct EmbeddingGemma2Configuration](./embeddinggemma2configuration.md)
  Configuration of `google/embeddinggemma-2` (`model_type: embedding_gemma2`).
- [struct FrequencyPenaltyContext](./frequencypenaltycontext.md)
  Processor that applies an additive frequency penalty to tokens in a recent context window.
- [struct GLM4ToolCallParser](./glm4toolcallparser.md)
  Parser for the GLM4 tool-call dialects.
- [struct Gemma4VisionConfiguration](./gemma4visionconfiguration.md)
- [struct GemmaFunctionParser](./gemmafunctionparser.md)
  Parser for Gemma format: call:name{key:value,k:str} Reference: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/tool_parsers/function_gemma.py
- [struct GenerateCompletionInfo](./generatecompletioninfo.md)
  Represents metadata and statistics related to token generation.
- [struct GenerateParameters](./generateparameters.md)
  Parameters for text generation, see [`TokenIterator`](./tokeniterator.md).
- [struct GenerateResult](./generateresult.md)
  Result of a call to a deprecated callback-based generate function.
- [struct GenerateTokenLogProbabilities](./generatetokenlogprobabilities.md)
  Log-probability details for one generated token.
- [struct GenerateTokenLogProbability](./generatetokenlogprobability.md)
  The log probability assigned to one vocabulary token.
- [struct GenerationComponents](./generationcomponents.md)
  Optional behavioral components that augment [`GenerateParameters`](./generateparameters.md) for a generation.
- [struct GenerationConfigFile](./generationconfigfile.md)
  JSON wrapper for `generation_config.json` file.
- [struct IntOrIntArray](./intorintarray.md)
  Decodes a JSON value that can be either a single Int or an array of Ints. Used for fields like `eos_token_id` which may appear as `128001` or `[128001, 128008]`.
- [struct JSONToolCallParser](./jsontoolcallparser.md)
  Parser for JSON format: {“name”: “…”, “arguments”: {…}} Reference: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/tool_parsers/default.py
- [struct KVCacheApplicationResult](./kvcacheapplicationresult.md)
  The observed outcome of applying a cache configuration to a realized cache.
- [struct KVCacheConfiguration](./kvcacheconfiguration.md)
  A complete request for key-value cache storage during generation.
- [struct KVCacheLayerStatus](./kvcachelayerstatus.md)
  Effective state of one leaf in a model’s cache topology.
- [struct KVCacheRuntimeReport](./kvcacheruntimereport.md)
  Effective per-layer state for a configured KV cache.
- [struct KVCacheStatus](./kvcachestatus.md)
  Authoritative planned or realized state of a model’s KV / recurrent cache.
- [struct KVCacheStrategyIdentifier](./kvcachestrategyidentifier.md)
  Stable, open-ended identity for a resolved cache strategy.
- [struct KimiK2ToolCallParser](./kimik2toolcallparser.md)
  Parser for Kimi K2 format: functions.name:0<|tool_call_argument_begin|>{JSON} Reference: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/tool_parsers/kimi_k2.py
- [struct LMInput](./lminput.md)
  Representation of [`LanguageModel`](./languagemodel.md) input.
- [struct LMOutput](./lmoutput.md)
  [`LanguageModel`](./languagemodel.md) step output. This is consumed internally by the [`TokenIterator`](./tokeniterator.md).
- [struct Llama3ToolCallParser](./llama3toolcallparser.md)
  Parser for Llama 3 tool calls. Llama 3 often outputs inline JSON without standard start/end tags, or preceded by `<|python_tag|>`. It may also output native python function calls like `get_weather(location="San Francisco")`.
- [struct LoRAConfiguration](./loraconfiguration.md)
  Configuration for how LoRA or DoRA should be applied.
- [struct LoRAContainer](./loracontainer.md)
  A container for managing LoRA or DoRA adapters and applying them to a language model.
- [struct LoRAModelMetadata](./loramodelmetadata.md)
  Metadata describing where a model applies LoRA adapters.
- [struct LogProbabilityGenerationTransformer](./logprobabilitygenerationtransformer.md)
  Adds ordered per-token log probabilities to a chat request.
- [struct LogProbabilityTokenLoopHandler](./logprobabilitytokenloophandler.md)
  Adds per-token log probabilities to another handler’s output.
- [struct MTPDrafterContext](./mtpdraftercontext.md)
  Lightweight context for an MTP drafter — simpler than `ModelContext` because drafters have no tokenizer, no user input processor, no chat template.
- [struct MTPDrafterState](./mtpdrafterstate.md)
  Per-stream state for MTP drafters that need their own transient storage.
- [struct MTPSpeculativeTokenIterator](./mtpspeculativetokeniterator.md)
  Generator of tokens using MTP (Multi-Token Prediction) speculative decoding.
- [struct MessageGeneratorUserInputProcessor](./messagegeneratoruserinputprocessor.md)
  Applies a configured message generator before delegating input processing.
- [struct MiniMaxM2ToolCallParser](./minimaxm2toolcallparser.md)
  Parser for MiniMax M2 format: v Reference: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/tool_parsers/minimax_m2.py
- [struct MistralToolCallParser](./mistraltoolcallparser.md)
  Parser for Mistral V13 tool call format: `[TOOL_CALLS]name[ARGS]{"json_args"}`
- [struct ModelCheckpoint](./modelcheckpoint.md)
  Checkpoint tensors and the metadata and quantization settings that describe them.
- [struct ModelComponent](./modelcomponent.md)
  A part of a model that can load separately from the rest, such as the vision encoder of a VLM.
- [struct ModelConfiguration](./modelconfiguration.md)
  Configuration for a given model:  at least an org/name identifier or a directory with the model files.
- [struct ModelContext](./modelcontext.md)
  Context of types that work together to provide a [`LanguageModel`](./languagemodel.md) for inference.
- [struct ModelConversionOptions](./modelconversionoptions.md)
  Options controlling model conversion.
- [struct ModelConversionProgress](./modelconversionprogress.md)
  Progress update emitted by the Swift conversion pipeline.
- [struct ModelConversionQuantization](./modelconversionquantization.md)
  Quantization settings for one conversion pass or layer.
- [struct ModelConversionResult](./modelconversionresult.md)
  Result returned after converting and saving a model.
- [struct NaiveStreamingDetokenizer](./naivestreamingdetokenizer.md)
- [struct NoSystemMessageGenerator](./nosystemmessagegenerator.md)
  Implementation of [`MessageGenerator`](./messagegenerator.md) that produces a `role` and `content` but omits `system` roles.
- [struct PEFTAdapterConfiguration](./peftadapterconfiguration.md)
  PEFT `adapter_config.json` schema. Only the fields we use are decoded.
- [struct PenaltyProcessor](./penaltyprocessor.md)
  Processor that composes penalty processors in Python mlx-lm order.
- [struct PrefillParameters](./prefillparameters.md)
  Parameters controlling how a prompt is prefilled into the [`KVCache`](./kvcache.md).
- [struct PresencePenaltyContext](./presencepenaltycontext.md)
  Processor that applies an additive presence penalty to tokens in a recent context window.
- [struct PromptCacheSnapshot](./promptcachesnapshot.md)
  A prompt cache and the model state that belongs with it.
- [struct PythonicToolCallParser](./pythonictoolcallparser.md)
  Parser for Pythonic tool call format: [function_name(arg1=‘value1’, arg2=‘value2’)] Used by LFM2.5 and similar models that output tool calls in Python function call syntax. Reference: LiquidAI LFM2.5 chat template format
- [struct Qwen35ToolCallParser](./qwen35toolcallparser.md)
  Parser for Qwen 3.5’s two observed tool-call payload dialects.
- [struct RawTokenLoopHandler](./rawtokenloophandler.md)
  Emits raw token IDs and completion information as [`TokenGeneration`](./tokengeneration.md) events.
- [struct ReasoningBudgetTransition](./reasoningbudgettransition.md)
  A model-protocol transition used when a reasoning budget is exhausted.
- [struct ReasoningChannel](./reasoningchannel.md)
  The labeled-channel shape of a reasoning protocol: the start delimiter opens a *channel* whose role is named by a short label that follows it, and one shared end delimiter closes every channel whatever its role.
- [struct ReasoningConfig](./reasoningconfig.md)
  Describes a model’s reasoning (chain-of-thought) protocol: the delimiters that bracket its thinking in the decoded generation stream, and how thinking is toggled at prompt time.
- [struct ReasoningEventEmitter](./reasoningeventemitter.md)
  Routes a model’s decoded generation stream into reasoning (chain-of-thought) vs response segments by scanning for the model’s reasoning delimiters and any protocol-declared implicit exits.
- [struct ReasoningTokenCollector](./reasoningtokencollector.md)
  Drives a [`ReasoningEventEmitter`](./reasoningeventemitter.md) over a raw generated-token stream, accumulating the reasoning-span token IDs while routing decoded text to reasoning/response segments.
- [struct RejectedToolCall](./rejectedtoolcall.md)
  A tool-call-shaped model output that was deliberately not made executable.
- [struct RejectedToolCallError](./rejectedtoolcallerror.md)
  An error used when an API cannot represent a [`RejectedToolCall`](./rejectedtoolcall.md) as a structured stream event.
- [struct RepetitionContext](./repetitioncontext.md)
  Processor that implements a `repetitionPenalty`.
- [struct RerankDocument](./rerankdocument.md)
  A text document with an application-defined identifier and metadata.
- [struct RerankDocumentsResponse](./rerankdocumentsresponse.md)
  The result of scoring or reranking structured documents.
- [struct RerankExecutionOptions](./rerankexecutionoptions.md)
  Resource limits and execution behavior for a reranking operation.
- [struct RerankRequest](./rerankrequest.md)
  A request to score and order candidate documents by relevance to a query.
- [struct RerankResponse](./rerankresponse.md)
  The result of a reranking operation.
- [struct RerankResult](./rerankresult.md)
  The relevance score for one candidate document.
- [struct RerankedDocument](./rerankeddocument.md)
  A structured document and its relevance score.
- [struct ResolvedModelConfiguration](./resolvedmodelconfiguration.md)
  A fully resolved model configuration where all sources have been resolved to local directory paths.
- [struct SpeculativeDecodingConfig](./speculativedecodingconfig.md)
  Configuration for speculative decoding in a `ChatSession`.
- [struct SpeculativeDecodingMemoryError](./speculativedecodingmemoryerror.md)
- [struct SpeculativeDecodingMemoryEvaluation](./speculativedecodingmemoryevaluation.md)
  Result of evaluating speculative decoding against a memory policy.
- [struct SpeculativeDecodingMemoryPolicy](./speculativedecodingmemorypolicy.md)
  Policy for gating auxiliary-model speculative decoding by resident memory estimates.
- [struct SpeculativeDecodingTelemetry](./speculativedecodingtelemetry.md)
  Runtime counters for a speculative decoding pass.
- [struct SpeculativeTokenIterator](./speculativetokeniterator.md)
  Generator of tokens using speculative decoding.
- [struct StandInUserInputProcessor](./standinuserinputprocessor.md)
  A do-nothing [`UserInputProcessor`](./userinputprocessor.md).
- [struct SuppressTokensProcessor](./suppresstokensprocessor.md)
  Processor that masks a fixed set of token IDs to `-inf` so they can never be sampled.
- [struct THW](./thw.md)
  Time/Height/Width struct to represent information about input images.
- [struct TextGenerationTransformer](./textgenerationtransformer.md)
  Preserves the session’s standard decoded output and generation parameters.
- [struct TextToolTokenLoopHandler](./texttooltokenloophandler.md)
  Decodes response text and tool calls into [`Generation`](./generation.md) events.
- [struct ThinkingBudgetConfiguration](./thinkingbudgetconfiguration.md)
  A hard upper bound for model-selected reasoning tokens.
- [struct ThinkingBudgetProcessor](./thinkingbudgetprocessor.md)
  A token-level, protocol-aware reasoning budget.
- [struct TokenIterator](./tokeniterator.md)
  Generator of tokens.
- [struct Tool](./tool.md)
- [struct ToolCall](./toolcall.md)
- [struct ToolCallPolicy](./toolcallpolicy.md)
  Rules for recovering and validating generated tool calls. Native parser requirements and declared-tool authorization always apply.
- [struct ToolCallRecoveryEvent](./toolcallrecoveryevent.md)
  Provenance for a tool call produced by cross-dialect recovery.
- [struct ToolParameter](./toolparameter.md)
- [struct TopPSampler](./toppsampler.md)
  Sampler that uses probability filters (`topP`, `topK`, `minP`) and `temperature` to sample the logits.
- [struct TurboQuantKVCacheConfiguration](./turboquantkvcacheconfiguration.md)
  TurboQuant cache compression settings.
- [struct UserInput](./userinput.md)
  Container for raw user input.
- [struct VarianceNormalizedKVCacheConfiguration](./variancenormalizedkvcacheconfiguration.md)
  Variance-normalized (KVarN-inspired) cache compression settings.
- [struct WiredBudgetPolicy](./wiredbudgetpolicy.md)
  Budget policy: `baseline + baseBytes + sum(activeSizes)`, optionally capped.
- [struct WiredFixedPolicy](./wiredfixedpolicy.md)
  Fixed policy: limit is constant while any ticket is active.
- [struct WiredMaxPolicy](./wiredmaxpolicy.md)
  Max policy: `max(baseline, max(activeSizes))`.
- [struct WiredMemoryMeasurement](./wiredmemorymeasurement.md)
  Result of a wired memory measurement pass.
- [struct WiredSumPolicy](./wiredsumpolicy.md)
  Sum policy: `baseline + sum(activeSizes)`, optionally capped.
- [struct XMLFunctionParser](./xmlfunctionparser.md)
  Parser for XML function format: <function=name><parameter=key>value Reference: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/tool_parsers/qwen3_coder.py
### Variables
- [let compiledSiluProduct: @Sendable (MLXArray, MLXArray) -> MLXArray](./compiledsiluproduct.md)
- [let mtpCacheCheckpointIndexKey: LMOutput.Key<Int>](./mtpcachecheckpointindexkey.md)
  Requests a recurrent-cache checkpoint after this many verification input tokens. Hybrid Qwen models use `1` for MTP-1 so a rejected draft restores state after the always-committed bonus token without replaying the model.
- [let mtpEmitFlagKey: LMOutput.Key<Bool>](./mtpemitflagkey.md)
  The MTP iterator sets this key on the [`LMOutput.State`](./lmoutput/state-swift.struct.md) it passes into the main model on each call to opt the target into emitting [`mtpLastHiddenStatesKey`](./mtplasthiddenstateskey.md) and [`mtpSharedKVStatesKey`](./mtpsharedkvstateskey.md). An absent key reads as `false` (no emit), so non-MTP callers are unaffected.
- [let mtpLastHiddenStatesKey: LMOutput.Key<MLXArray>](./mtplasthiddenstateskey.md)
  Target writes the hidden representation required by its MTP head here. This is architecture-specific, but must match the representation used to train the paired MTP head. Qwen and Gemma assistants both publish their post-final-norm representation. The iterator threads it to the drafter unchanged as `lastHidden`.
- [let mtpPositionDeltasKey: LMOutput.Key<MLXArray>](./mtppositiondeltaskey.md)
  Target writes optional position delta state here for MTP drafters that need to reproduce target-specific RoPE continuation positions.
- [let mtpSharedKVOffsetsKey: LMOutput.Key<[String : Int]>](./mtpsharedkvoffsetskey.md)
  Target writes the absolute cache offset for each emitted shared-K/V layer-type here. The K/V tensors themselves may have a capped sequence axis when backed by a rotating cache, so their shape is not always the absolute RoPE/query position.
- [let mtpSharedKVSourceIndicesKey: LMOutput.Key<[String : Int]>](./mtpsharedkvsourceindiceskey.md)
  Which cache entry each [`mtpSharedKVStatesKey`](./mtpsharedkvstateskey.md) tuple was read from, keyed the same way.
- [let mtpSharedKVStatesKey: LMOutput.Key<[String : (MLXArray, MLXArray)]>](./mtpsharedkvstateskey.md)
  Target writes one `(keys, values)` tuple per `layer_type` (`"full_attention"`, `"sliding_attention"`) here, drawn from the last layer of each type. [`MTPSpeculativeTokenIterator`](./mtpspeculativetokeniterator.md) reads it and threads it to the drafter as `sharedKV`.
- [let weightedExpertSum: @Sendable (MLXArray, MLXArray) -> MLXArray](./weightedexpertsum.md)
### Functions
- [func applyKVCacheConfiguration(cache: inout [KVCache], configuration: KVCacheConfiguration) throws -> KVCacheApplicationResult](./applykvcacheconfiguration%28cache,configuration%29.md)
  Apply a typed cache strategy to every eligible cache layer.
- [func applyRotaryPosition<R>(R, to: MLXArray, cache: KVCache?) -> MLXArray](./applyrotaryposition%28_,to,cache%29.md)
  Apply rotary position embeddings, using the cache offset when available.
- [func applyRotaryPosition<R>(R, to: MLXArray, offset: RoPEOffset?) -> MLXArray](./applyrotaryposition%28_,to,offset%29.md)
  Apply rotary position embeddings, using the cache offset when available.
- [func attentionCacheKind(parameters: GenerateParameters?) throws -> CacheLayerKind](./attentioncachekind%28parameters%29.md)
  Build a standard full-attention cache kind that honors the requested capacity.
- [func attentionWithCacheUpdate(queries: MLXArray, keys: MLXArray, values: MLXArray, cache: KVCache?, scale: Float, mask: MLXFast.ScaledDotProductAttentionMaskMode) -> MLXArray](./attentionwithcacheupdate%28queries,keys,values,cache,scale,mask%29.md)
  Automatic attention with cache update
- [func bicubicInterpolate(MLXArray, scaleFactor: Float, alignCorners: Bool, antialias: Bool) -> MLXArray](./bicubicinterpolate%28_,scalefactor,aligncorners,antialias%29.md)
  Bicubic interpolation with a single scale factor.
- [func bicubicInterpolate(MLXArray, size: (Int, Int)?, scaleFactor: (Float, Float)?, alignCorners: Bool, antialias: Bool) -> MLXArray](./bicubicinterpolate%28_,size,scalefactor,aligncorners,antialias%29.md)
  Bicubic interpolation using MLX Metal kernel.
- [func canTrimPromptCache([KVCache]) -> Bool](./cantrimpromptcache%28_%29.md)
  Check if model’s cache can be trimmed.
- [func canTrimPromptCache([KVCache], numTokens: Int) -> Bool](./cantrimpromptcache%28_,numtokens%29.md)
  Whether every layer retains enough history to rewind exactly by `numTokens`.
- [func convert(modelDirectory: URL, tokenizerDirectory: URL?, model: BaseLanguageModel, to: URL, bits: Int?, groupSize: Int?, mode: QuantizationMode, perLayerQuantization: BaseConfiguration.PerLayerQuantization?) throws -> ModelConversionResult](./convert%28modeldirectory,tokenizerdirectory,model,to,bits,groupsize,mode,perlayerquantization%29.md)
  Quantize and save an already-instantiated model from a compatible safetensors directory.
- [func convert(modelDirectory: URL, tokenizerDirectory: URL?, model: BaseLanguageModel, to: URL, options: ModelConversionOptions, progressHandler: @Sendable (ModelConversionProgress) -> Void, perLayerQuantization: BaseConfiguration.PerLayerQuantization?) throws -> ModelConversionResult](./convert%28modeldirectory,tokenizerdirectory,model,to,options,progresshandler,perlayerquantization%29.md)
  Quantize and save an already-instantiated model from a compatible safetensors directory.
- [func createAttentionMask(h: MLXArray, cache: [KVCache]?) -> MLXArray?](./createattentionmask%28h,cache%29.md)
  Create an attention mask using the parameters from the KVCache.
- [func createAttentionMask(h: MLXArray, cache: [KVCache]?, returnArray: Bool) -> MLXFast.ScaledDotProductAttentionMaskMode](./createattentionmask%28h,cache,returnarray%29.md)
- [func createAttentionMask(h: MLXArray, cache: KVCache?, windowSize: Int?, returnArray: Bool) -> MLXFast.ScaledDotProductAttentionMaskMode](./createattentionmask%28h,cache,windowsize,returnarray%29.md)
  Create an attention mask with explicit window size parameter.
- [func createBidirectionalMask(queryLen: Int, kvLen: Int, dtype: DType) -> MLXArray](./createbidirectionalmask%28querylen,kvlen,dtype%29.md)
  Bidirectional attention mask: every query position attends to every kv position equally (no causal restriction).
- [func createBidirectionalSlidingWindowMask(queryLen: Int, kvLen: Int, windowSize: Int, dtype: DType) -> MLXArray](./createbidirectionalslidingwindowmask%28querylen,kvlen,windowsize,dtype%29.md)
  Bidirectional sliding-window attention mask: when `kvLen` exceeds `windowSize`, each query attends to a contiguous window of the first `windowSize` kv positions; the remaining `kvLen - windowSize` positions are masked with `-inf`. When `windowSize >= kvLen` (the degenerate case — and the production MTP path, where the sliding-attention KV cache is capped at `windowSize` by `RotatingKVCache`), the helper early-exits to an all-zeros mask (every query attends to every kv position).
- [func createCausalMask(n: Int, offset: Int, windowSize: Int?, lengths: MLXArray?) -> MLXArray](./createcausalmask%28n,offset,windowsize,lengths%29.md)
- [func createSSMMask(h: MLXArray, cache: MambaCache?) -> MLXArray?](./createssmmask%28h,cache%29.md)
- [func gatedDeltaUpdate(q: MLXArray, k: MLXArray, v: MLXArray, a: MLXArray, b: MLXArray, aLog: MLXArray, dtBias: MLXArray, state: MLXArray?, mask: MLXArray?, useKernel: Bool) -> (MLXArray, MLXArray)](./gateddeltaupdate%28q,k,v,a,b,alog,dtbias,state,mask,usekernel%29.md)
- [func gatherSort(x: MLXArray, indices: MLXArray) -> (MLXArray, MLXArray, MLXArray)](./gathersort%28x,indices%29.md)
- [func generate(input: LMInput, cache: [KVCache]?, parameters: GenerateParameters, context: ModelContext, mtpDrafter: any MTPDrafterModel, blockSize: Int, components: GenerationComponents, wiredMemoryTicket: WiredMemoryTicket?, tools: [[String : any Sendable]]?) throws -> AsyncStream<Generation>](./generate%28input,cache,parameters,context,mtpdrafter,blocksize,components,wiredmemoryticket,tools%29.md)
  Generates tokens asynchronously using MTP speculative decoding.
- [func generate(input: LMInput, cache: [KVCache]?, state: LMOutput.State?, parameters: GenerateParameters, context: ModelContext, components: GenerationComponents, wiredMemoryTicket: WiredMemoryTicket?, tools: [[String : any Sendable]]?) throws -> AsyncStream<Generation>](./generate%28input,cache,state,parameters,context,components,wiredmemoryticket,tools%29.md)
  Generates tokens asynchronously using the provided language model input, parameters, and context.
- [func generate(input: LMInput, cache: [KVCache]?, state: LMOutput.State?, parameters: GenerateParameters, context: ModelContext, draftModel: any LanguageModel, draftCache: [KVCache]?, numDraftTokens: Int, components: GenerationComponents, wiredMemoryTicket: WiredMemoryTicket?, tools: [[String : any Sendable]]?) throws -> AsyncStream<Generation>](./generate%28input,cache,state,parameters,context,draftmodel,draftcache,numdrafttokens,components,wiredmemoryticket,tools%29.md)
  Generates text and tool calls asynchronously using speculative decoding with a draft model.
- [func generate(input: LMInput, context: ModelContext, iterator: TokenIterator, didGenerate: (Int) -> GenerateDisposition) -> GenerateCompletionInfo](./generate%28input,context,iterator,didgenerate%29-9fbvh.md)
  Low-level token generation using a [`TokenIterator`](./tokeniterator.md).
- [func generate(input: LMInput, context: ModelContext, iterator: TokenIterator, didGenerate: ([Int]) -> GenerateDisposition) -> GenerateResult](./generate%28input,context,iterator,didgenerate%29-pi3z.md)
  Low-level token generation using a [`TokenIterator`](./tokeniterator.md).
- [func generate(input: LMInput, context: ModelContext, iterator: TokenIterator, wiredMemoryTicket: WiredMemoryTicket?) -> AsyncStream<Generation>](./generate%28input,context,iterator,wiredmemoryticket%29.md)
- [func generate(input: LMInput, parameters: GenerateParameters, context: ModelContext, didGenerate: (Int) -> GenerateDisposition) throws -> GenerateCompletionInfo](./generate%28input,parameters,context,didgenerate%29-66zpx.md)
  Generate tokens from an [`LMInput`](./lminput.md) and a [`ModelContext`](./modelcontext.md).
- [func generate(input: LMInput, parameters: GenerateParameters, context: ModelContext, didGenerate: ([Int]) -> GenerateDisposition) throws -> GenerateResult](./generate%28input,parameters,context,didgenerate%29-76hgb.md)
  Generate tokens from an [`LMInput`](./lminput.md) and a [`ModelContext`](./modelcontext.md).
- [func generate(promptTokens: [Int], parameters: GenerateParameters, model: any LanguageModel, tokenizer: Tokenizer, extraEOSTokens: Set<String>?, didGenerate: ([Int]) -> GenerateDisposition) throws -> GenerateResult](./generate%28prompttokens,parameters,model,tokenizer,extraeostokens,didgenerate%29.md)
  Given prompt tokens generate text using the given model and parameters.
- [func generateLoopTask<Handler>(promptTokenCount: Int, modelConfiguration: ModelConfiguration, tokenizer: Tokenizer, iterator: consuming any TokenIteratorProtocol, wiredMemoryTicket: WiredMemoryTicket?, includeStopToken: Bool, handler: consuming Handler) -> (AsyncStream<Handler.Output>, Task<Void, Never>)](./generatelooptask%28prompttokencount,modelconfiguration,tokenizer,iterator,wiredmemoryticket,includestoptoken,handler%29.md)
  Runs a token iterator with a custom output handler.
- [func generateTask<TOKEN>(promptTokenCount: Int, modelConfiguration: ModelConfiguration, tokenizer: Tokenizer, iterator: consuming TOKEN, wiredMemoryTicket: WiredMemoryTicket?, tools: [[String : any Sendable]]?, toolCallPolicy: ToolCallPolicy, reasoningPrimedInside: Bool) -> (AsyncStream<Generation>, Task<Void, Never>)](./generatetask%28prompttokencount,modelconfiguration,tokenizer,iterator,wiredmemoryticket,tools,toolcallpolicy,reasoningprimedinside%29.md)
  Low-level token generation returning an `AsyncStream<Generation>` and a `Task`.
- [func generateTokenTask(promptTokenCount: Int, modelConfiguration: ModelConfiguration, tokenizer: Tokenizer, iterator: consuming TokenIterator, includeStopToken: Bool, wiredMemoryTicket: WiredMemoryTicket?) -> (AsyncStream<TokenGeneration>, Task<Void, Never>)](./generatetokentask%28prompttokencount,modelconfiguration,tokenizer,iterator,includestoptoken,wiredmemoryticket%29.md)
  Low-level raw token generation using a `TokenIterator`, returning an `AsyncStream<TokenGeneration>` and a `Task`.
- [func generateTokens(input: LMInput, cache: [KVCache]?, parameters: GenerateParameters, context: ModelContext, mtpDrafter: any MTPDrafterModel, blockSize: Int, components: GenerationComponents, wiredMemoryTicket: WiredMemoryTicket?) throws -> AsyncStream<TokenGeneration>](./generatetokens%28input,cache,parameters,context,mtpdrafter,blocksize,components,wiredmemoryticket%29.md)
  Generates raw token IDs asynchronously using MTP speculative decoding.
- [func generateTokens(input: LMInput, cache: [KVCache]?, state: LMOutput.State?, parameters: GenerateParameters, context: ModelContext, draftModel: any LanguageModel, draftCache: [KVCache]?, numDraftTokens: Int, components: GenerationComponents, wiredMemoryTicket: WiredMemoryTicket?) throws -> AsyncStream<TokenGeneration>](./generatetokens%28input,cache,state,parameters,context,draftmodel,draftcache,numdrafttokens,components,wiredmemoryticket%29.md)
  Generates raw token IDs asynchronously using speculative decoding with a draft model.
- [func generateTokens(input: LMInput, cache: [KVCache]?, state: LMOutput.State?, parameters: GenerateParameters, context: ModelContext, includeStopToken: Bool, components: GenerationComponents, wiredMemoryTicket: WiredMemoryTicket?) throws -> AsyncStream<TokenGeneration>](./generatetokens%28input,cache,state,parameters,context,includestoptoken,components,wiredmemoryticket%29.md)
  Generates raw token IDs asynchronously using the provided language model input, parameters, and context.
- [func generateTokensTask(input: LMInput, cache: [KVCache]?, state: LMOutput.State?, parameters: GenerateParameters, context: ModelContext, includeStopToken: Bool, components: GenerationComponents, wiredMemoryTicket: WiredMemoryTicket?) throws -> (AsyncStream<TokenGeneration>, Task<Void, Never>)](./generatetokenstask%28input,cache,state,parameters,context,includestoptoken,components,wiredmemoryticket%29.md)
  Generates raw token IDs asynchronously and returns the stream plus a `Task`.
- [func hybridAttentionCacheKind(parameters: GenerateParameters?, slidingWindow: Int?, usesSlidingWindow: Bool) throws -> CacheLayerKind](./hybridattentioncachekind%28parameters,slidingwindow,usesslidingwindow%29.md)
  Full-attention kind if the layer is not sliding-window; otherwise the architecture sliding window capped by legacy `maxKVSize`.
- [func initializeRope(dims: Int, base: Float, traditional: Bool, scalingConfig: [String : StringOrNumber]?, maxPositionEmbeddings: Int?) -> RoPELayer](./initializerope%28dims,base,traditional,scalingconfig,maxpositionembeddings%29.md)
- [func isParoQuantModel(directory: URL) -> Bool](./isparoquantmodel%28directory%29.md)
  Returns `true` if the model directory contains a ParoQuant checkpoint.
- [func kvCacheRuntimeReport(cache: [KVCache], configuration: KVCacheConfiguration) -> KVCacheRuntimeReport](./kvcacheruntimereport%28cache,configuration%29.md)
  Describe the effective strategy of every cache entry without mutating it.
- [func loadModel(from: URL, using: any TokenizerLoader) async throws -> sending ModelContext](./loadmodel%28from,using%29.md)
  Load a model from a local directory of configuration and weights.
- [func loadModel(from: any Downloader, using: any TokenizerLoader, configuration: ModelConfiguration, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> sending ModelContext](./loadmodel%28from,using,configuration,uselatest,progresshandler%29.md)
  Load a model given a [`ModelConfiguration`](./modelconfiguration.md), downloading via a [`Downloader`](./downloader.md).
- [func loadModel(from: any Downloader, using: any TokenizerLoader, id: String, revision: String, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> sending ModelContext](./loadmodel%28from,using,id,revision,uselatest,progresshandler%29.md)
  Load a model given a model identifier, downloading via a [`Downloader`](./downloader.md).
- [func loadModelContainer(from: URL, using: any TokenizerLoader) async throws -> sending ModelContainer](./loadmodelcontainer%28from,using%29.md)
  Load a model from a local directory of configuration and weights.
- [func loadModelContainer(from: any Downloader, using: any TokenizerLoader, configuration: ModelConfiguration, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> sending ModelContainer](./loadmodelcontainer%28from,using,configuration,uselatest,progresshandler%29.md)
  Load a model given a [`ModelConfiguration`](./modelconfiguration.md), downloading via a [`Downloader`](./downloader.md).
- [func loadModelContainer(from: any Downloader, using: any TokenizerLoader, id: String, revision: String, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> sending ModelContainer](./loadmodelcontainer%28from,using,id,revision,uselatest,progresshandler%29.md)
  Load a model given a model identifier, downloading via a [`Downloader`](./downloader.md).
- [func loadParoQuantModel<T>(from: URL, typeRegistry: ModelTypeRegistry<T>, tokenizerLoader: any TokenizerLoader, toolCallFormat: ToolCallFormat?) async throws -> ModelContainer](./loadparoquantmodel%28from,typeregistry,tokenizerloader,toolcallformat%29.md)
  Load a ParoQuant model from a local directory, returning a [`ModelContainer`](./modelcontainer.md).
- [func loadPromptCache(url: URL) throws -> ([KVCache], [String : String])](./loadpromptcache%28url%29.md)
  Load a prompt cache from a file, without model state.
- [func loadPromptCacheSnapshot(url: URL) throws -> PromptCacheSnapshot](./loadpromptcachesnapshot%28url%29.md)
  Load a prompt cache and its associated model state from a file.
- [func loadWeights(modelDirectory: URL, model: BaseLanguageModel, quantization: BaseConfiguration.Quantization?, perLayerQuantization: BaseConfiguration.PerLayerQuantization?, weightFileSelection: WeightFileSelection, excludedComponents: Set<ModelComponent>, componentLoading: ComponentLoading) throws](./loadweights%28modeldirectory,model,quantization,perlayerquantization,weightfileselection,excludedcomponents,componentloading%29-858j8.md)
  Load model weights.
- [func loadWeights(modelDirectory: URL, model: BaseLanguageModel, quantization: BaseConfiguration.Quantization?, perLayerQuantization: BaseConfiguration.PerLayerQuantization?, weightFileSelection: WeightFileSelection, excludedComponents: Set<ModelComponent>, componentLoading: ComponentLoading) async throws](./loadweights%28modeldirectory,model,quantization,perlayerquantization,weightfileselection,excludedcomponents,componentloading%29-fqoy.md)
  Async variant of [`loadWeights(modelDirectory:model:quantization:perLayerQuantization:weightFileSelection:excludedComponents:componentLoading:)`](./loadweights%28modeldirectory,model,quantization,perlayerquantization,weightfileselection,excludedcomponents,componentloading%29-858j8.md).
- [func makeAttentionKVCache(parameters: GenerateParameters?) throws -> KVCache](./makeattentionkvcache%28parameters%29.md)
  Build a standard full-attention [`KVCache`](./kvcache.md) that honors the requested capacity.
- [func makeAttentionMask(n: Int, cache: KVCache?, windowSize: Int?, returnArray: Bool) -> MLXFast.ScaledDotProductAttentionMaskMode](./makeattentionmask%28n,cache,windowsize,returnarray%29.md)
  Create an attention mask matching mlx-lm’s create_attention_mask helper.
- [func makeHybridAttentionKVCache(parameters: GenerateParameters?, slidingWindow: Int?, usesSlidingWindow: Bool) throws -> KVCache](./makehybridattentionkvcache%28parameters,slidingwindow,usesslidingwindow%29.md)
  Full-attention cache if the layer is not sliding-window; otherwise the architecture sliding window capped by legacy `maxKVSize`.
- [func makePromptCache(model: any LanguageModel, maxKVSize: Int?) throws -> [KVCache]](./makepromptcache%28model,maxkvsize%29.md)
  Legacy function for backwards compatibility
- [func makePromptCache(model: any LanguageModel, parameters: GenerateParameters?) throws -> [KVCache]](./makepromptcache%28model,parameters%29.md)
  Construct the model’s cache for use when generating.
- [func makePromptCacheWithLayerCount(numLayers: Int, maxKVSize: Int?) throws -> [KVCache]](./makepromptcachewithlayercount%28numlayers,maxkvsize%29.md)
  Fallback function to create cache when layer count is known
- [func makeSlidingWindowKVCache(parameters: GenerateParameters?, window: Int) throws -> KVCache](./makeslidingwindowkvcache%28parameters,window%29.md)
  Architecture-imposed sliding-window attention cache, capped by legacy `maxKVSize`.
- [func maybeQuantizeKVCache(cache: inout [KVCache], kvBits: Int?, kvGroupSize: Int, quantizedKVStart: Int, kvScheme: String?)](./maybequantizekvcache%28cache,kvbits,kvgroupsize,quantizedkvstart,kvscheme%29.md)
  Converts regular caches to quantized caches when:
- [func maybeTurboQuantizeKVCache(cache: inout [KVCache], keyBits: Int, valueBits: Int, quantizedKVStart: Int) -> Bool](./maybeturboquantizekvcache%28cache,keybits,valuebits,quantizedkvstart%29.md)
  Convert eligible `KVCacheSimple` layers to `TurboQuantKVCache` once their offset passes `quantizedKVStart`, transferring the accumulated KV state. Mamba / wrapper caches are left untouched. `RotatingKVCache` layers (Gemma-style sliding-window) are also left untouched – see `logRotatingKVCacheSkipOnce` – since they are already memory-bounded by their window size and their rotating storage layout does not fit the sequential-append compression path. Called from `maybeQuantizeKVCache` when `kvScheme` names a TurboQuant scheme.
- [func mergeGenerationConfigSuppressedTokens(GenerationConfigFile?, into: any LanguageModel)](./mergegenerationconfigsuppressedtokens%28_,into%29.md)
  Merge `suppress_tokens` from `generation_config.json` into the model’s suppressed-token set.
- [func nearestInterpolate(MLXArray, scaleFactor: Float) -> MLXArray](./nearestinterpolate%28_,scalefactor%29.md)
  Nearest neighbor interpolation with a single scale factor.
- [func nearestInterpolate(MLXArray, size: (Int, Int)?, scaleFactor: (Float, Float)?) -> MLXArray](./nearestinterpolate%28_,size,scalefactor%29.md)
  Nearest neighbor interpolation using MLX Metal kernel.
- [func quantizedScaledDotProductAttention(queries: MLXArray, quantizedKeys: (MLXArray, MLXArray, MLXArray?), quantizedValues: (MLXArray, MLXArray, MLXArray?), scale: Float, mask: MLXFast.ScaledDotProductAttentionMaskMode, groupSize: Int, bits: Int, mode: QuantizationMode) -> MLXArray](./quantizedscaleddotproductattention%28queries,quantizedkeys,quantizedvalues,scale,mask,groupsize,bits,mode%29.md)
- [func registerKVCacheType<T>(T.Type) throws](./registerkvcachetype%28_%29.md)
  Register a cache type so [`loadPromptCacheSnapshot(url:)`](./loadpromptcachesnapshot%28url%29.md) can restore it.
- [func resolve(configuration: ModelConfiguration, from: any Downloader, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> ResolvedModelConfiguration](./resolve%28configuration,from,uselatest,progresshandler%29.md)
  Resolve a [`ModelConfiguration`](./modelconfiguration.md) into a [`ResolvedModelConfiguration`](./resolvedmodelconfiguration.md) by downloading remote sources via a [`Downloader`](./downloader.md).
- [func resolveAffineScheme(String?) -> (bits: Int, groupSize: Int)?](./resolveaffinescheme%28_%29.md)
  Dynamically quantize KV caches during generation if conditions are met
- [func resolveTurboScheme(String?) -> (keyBits: Int, valueBits: Int)?](./resolveturboscheme%28_%29.md)
  Resolve a TurboQuant kvScheme string to (keyBits, valueBits). `keyBits == 0` means raw FP16 keys (only values are compressed). Returns nil for non-TurboQuant schemes.
- [func resolveVarianceNormalizedScheme(String?) -> (keyBits: Int, valueBits: Int, tileSize: Int, sinkhornIterations: Int)?](./resolvevariancenormalizedscheme%28_%29.md)
  Resolve a legacy `kvScheme` string for variance-normalized compression.
- [func savePromptCache(url: URL, cache: [KVCache], metadata: [String : String], state: LMOutput.State?) throws](./savepromptcache%28url,cache,metadata,state%29.md)
  Save a pre-computed prompt cache to a file.
- [func scatterUnsort(x: MLXArray, invOrder: MLXArray, shape: [Int]?) -> MLXArray](./scatterunsort%28x,invorder,shape%29.md)
- [func slidingWindowCacheKind(parameters: GenerateParameters?, window: Int) throws -> CacheLayerKind](./slidingwindowcachekind%28parameters,window%29.md)
  Architecture-imposed sliding-window attention kind, capped by legacy `maxKVSize`.
- [func trimPromptCache([KVCache], numTokens: Int) -> Int](./trimpromptcache%28_,numtokens%29.md)
  Trim the model’s cache by the given number of tokens.
- [func validateKVCacheCompatibility([KVCache], configuration: KVCacheConfiguration) throws](./validatekvcachecompatibility%28_,configuration%29.md)
  Validate the requested compatibility policy against a concrete model cache.
- [func validateMROPESection([String : StringOrNumber]?, context: String) throws](./validatemropesection%28_,context%29.md)
- [func validateRoPEConfiguration([String : StringOrNumber]?, context: String, supportedTypes: Set<String>?) throws](./validateropeconfiguration%28_,context,supportedtypes%29.md)
- [func withPreparedCache<Result>([any KVCache], lengths: [Int]?, () throws -> Result) rethrows -> Result](./withpreparedcache%28_,lengths,_%29.md)
### Type Aliases
- [typealias Message](./message.md)
- [typealias ModelConversionQuantizationPredicate](./modelconversionquantizationpredicate.md)
  Predicate used to customize layer quantization.
- [typealias ModelFactory](./modelfactory.md)
  For backward compatibility: `ModelFactory` refers to an LLM/VLM model factory.
- [typealias RoPELayer](./ropelayer.md)
- [typealias SendableModelAdapter](./sendablemodeladapter.md)
- [typealias StandardKVCache](./standardkvcache.md)
  Standard KV cache - alias to KVCacheSimple for compatibility
- [typealias SuScaledRotaryEmbedding](./suscaledrotaryembedding.md)
  Backward compatibility alias.
- [typealias ToolSpec](./toolspec.md)
### Enumerations
- [enum CacheLayerKind](./cachelayerkind.md)
  How a single model layer retains state across generation steps.
- [enum Chat](./chat.md)
- [enum ChatSessionError](./chatsessionerror.md)
  Errors thrown by [`ChatSession`](./chatsession.md).
- [enum ComponentLoading](./componentloading.md)
  When a load reads the components that a model can load on first use.
- [enum ContinuationStateError](./continuationstateerror.md)
  Errors thrown when a warm KV cache is continued without the model state it requires.
- [enum Gemma](./gemma.md)
- [enum Gemma4SharedKVState](./gemma4sharedkvstate.md)
  Per-layer key/value state threaded between Gemma 4 decoder layers when KV sharing is enabled.
- [enum GenerateDisposition](./generatedisposition.md)
  Action from token visitor callback in deprecated callback-based generate functions.
- [enum GenerateStopReason](./generatestopreason.md)
  Reason why token generation stopped.
- [enum Generation](./generation.md)
  Represents the different stages or outputs of the token generation process.
- [enum JSONValue](./jsonvalue.md)
  Type-safe representation of JSON values
- [enum KVCacheConfigurationError](./kvcacheconfigurationerror.md)
  Validation failures for typed or legacy KV-cache configuration.
- [enum LogProbabilityGeneration](./logprobabilitygeneration.md)
  Events from a handler composed with [`LogProbabilityTokenLoopHandler`](./logprobabilitytokenloophandler.md).
- [enum MTPDrafterTypeRegistry](./mtpdraftertyperegistry.md)
  Registry of `model_type` strings (e.g. `"gemma4_assistant"`) to creator closures that instantiate [`MTPDrafterModel`](./mtpdraftermodel.md) instances from `config.json` data.
- [enum ModelAdapterError](./modeladaptererror.md)
  Errors that can occur when working with a `ModelAdapter`.
- [enum ModelConversionError](./modelconversionerror.md)
  Errors thrown by model conversion helpers.
- [enum ModelConversionQuantizationCalibration](./modelconversionquantizationcalibration.md)
  How the quantization grid is derived from the source weights.
- [enum ModelConversionQuantizationDecision](./modelconversionquantizationdecision.md)
  Per-layer quantization decision.
- [enum ModelConversionStage](./modelconversionstage.md)
  Coarse conversion stage for progress callbacks.
- [enum ModelFactoryError](./modelfactoryerror.md)
- [enum OnDemandComponentError](./ondemandcomponenterror.md)
- [enum ParoQuantError](./paroquanterror.md)
- [enum ParoQuantPreparedCheckpoint](./paroquantpreparedcheckpoint.md)
  Prepared Checkpoint — the once-converted MLX-native form of a PARO checkpoint, stored beside the original so later loads skip the AutoAWQ conversion (unpack/reorder/repack, Mamba split, MoE expert stacking, rotation-key remap).
- [enum PrepareResult](./prepareresult.md)
  The result of the call to [`prepare(_:cache:state:prefill:)`](./languagemodel/prepare%28_,cache,state,prefill%29.md)
- [enum QwenReasoningProtocol](./qwenreasoningprotocol.md)
  Qwen-family reasoning protocol declarations.
- [enum ReasoningError](./reasoningerror.md)
  Errors raised while resolving or applying a model’s reasoning configuration.
- [enum ReasoningHeuristics](./reasoningheuristics.md)
  Pre-load heuristics for deciding whether a model identifier looks like a reasoning-capable family.
- [enum ReasoningPromptStrategy](./reasoningpromptstrategy.md)
  How a model’s “thinking on / off” preference is expressed to its chat template.
- [enum RerankScoreKind](./rerankscorekind.md)
  The semantic meaning and numeric range of scores returned by a reranker.
- [enum RerankTruncationPolicy](./reranktruncationpolicy.md)
  Controls how inputs that exceed a model’s context limit are handled.
- [enum RerankerError](./rerankererror.md)
  Errors thrown while preparing or scoring reranker inputs.
- [enum RoPEOffset](./ropeoffset.md)
  Offset to use with [`applyRotaryPosition(_:to:offset:)`](./applyrotaryposition%28_,to,offset%29.md).
- [enum SpeculativeDecodingMemoryAction](./speculativedecodingmemoryaction.md)
  Action to take when speculative decoding exceeds a memory budget.
- [enum StringOrNumber](./stringornumber.md)
  Representation of a heterogenous type in a JSON configuration file.
- [enum ThinkingBudgetDiagnostic](./thinkingbudgetdiagnostic.md)
  Diagnostics emitted when a hard reasoning budget cannot remain authoritative.
- [enum ThinkingBudgetError](./thinkingbudgeterror.md)
  Errors raised while configuring a reasoning-token budget.
- [enum TokenGeneration](./tokengeneration.md)
  Represents the different stages or outputs of raw-token generation.
- [enum TokenLoopDisposition](./tokenloopdisposition.md)
  Controls whether the generation loop continues.
- [enum TokenizerError](./tokenizererror.md)
- [enum TokenizerSource](./tokenizersource.md)
  Identifies where a tokenizer should be loaded from.
- [enum ToolCallFormat](./toolcallformat.md)
  Supported tool call formats for different language models.
- [enum ToolCallRecoveryPolicy](./toolcallrecoverypolicy.md)
  Policy governing bounded cross-dialect tool-call recovery.
- [enum ToolCallValidationPolicy](./toolcallvalidationpolicy.md)
  Controls schema enforcement independently of syntax recovery and tool-name authorization. Both modes normalize unambiguous, schema-declared values.
- [enum ToolError](./toolerror.md)
- [enum ToolParameterType](./toolparametertype.md)
- [enum WeightFileSelection](./weightfileselection.md)
  How the safetensors files holding a model’s weights are chosen.
- [enum WiredMemoryUtils](./wiredmemoryutils.md)
  Helpers for deriving wired memory budgets from real runtime measurements.
### Extended Modules
- [Foundation](./foundation.md)
- [MLXNN](./mlxnn.md)
- [Swift](./swift.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon)*