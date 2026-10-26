---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generateparameters"
framework: "mlx-swift-lm/MLXLMCommon"
---

# GenerateParameters

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Parameters for text generation, see [`TokenIterator`](./tokeniterator.md).

## Declaration

```swift
struct GenerateParameters
```

#### Overview

This produces:

- [`LogitSampler`](./logitsampler.md)
- [`LogitProcessor`](./logitprocessor.md)

for the `TokenIterator`.

## Topics

### Initializers
- [init(maxTokens: Int?, maxKVSize: Int?, kvBits: Int?, kvGroupSize: Int, quantizedKVStart: Int, kvScheme: String?, temperature: Float, topP: Float, topK: Int, minP: Float, repetitionPenalty: Float?, repetitionContextSize: Int, presencePenalty: Float?, presenceContextSize: Int, frequencyPenalty: Float?, frequencyContextSize: Int, prefillStepSize: Int?, seed: UInt64?)](./generateparameters/init%28maxtokens,maxkvsize,kvbits,kvgroupsize,quantizedkvstart,kvscheme,temperature,topp,topk,minp,repetitionpenalty,repetitioncontextsize,presencepenalty,presencecontextsize,frequencypenalty,frequencycontextsize,prefill-7e17e849.md)
- [init(maxTokens: Int?, maxKVSize: Int?, kvCache: KVCacheConfiguration?, kvBits: Int?, kvGroupSize: Int, quantizedKVStart: Int, kvScheme: String?, temperature: Float, topP: Float, topK: Int, minP: Float, logProbabilities: Int?, repetitionPenalty: Float?, repetitionContextSize: Int, presencePenalty: Float?, presenceContextSize: Int, frequencyPenalty: Float?, frequencyContextSize: Int, prefill: PrefillParameters, seed: UInt64?, toolCallPolicy: ToolCallPolicy)](./generateparameters/init%28maxtokens_maxkvsize_kvcache_kvbits_kvgroupsize_quantizedkvstart_kvscheme_temperature_topp_topk_minp_logprobabilities_repetitionpenalty_repetitioncontextsize_presencepenalty_presencecontextsize_frequencypenalty_fre-3cd8daf0.md)
### Instance Properties
- [var frequencyContextSize: Int](./generateparameters/frequencycontextsize.md)
  number of tokens to consider for frequency penalty
- [var frequencyPenalty: Float?](./generateparameters/frequencypenalty.md)
  additive penalty that scales with token frequency in recent context
- [var kvBits: Int?](./generateparameters/kvbits.md)
  Number of bits to use for KV cache quantization. nil implies no cache quantization.
- [var kvCache: KVCacheConfiguration?](./generateparameters/kvcache.md)
  Typed key-value cache configuration.
- [var kvGroupSize: Int](./generateparameters/kvgroupsize.md)
  Group size for KV cache quantization (default: 64)
- [var kvScheme: String?](./generateparameters/kvscheme.md)
  KV cache compression scheme. Overrides kvBits when set.
- [var logProbabilities: Int?](./generateparameters/logprobabilities.md)
  Per-token log-probability reporting. `nil` disables reporting; `0` reports the selected token only, and a positive value also reports that many top tokens. Use [`LogProbabilityTokenLoopHandler`](./logprobabilitytokenloophandler.md) to emit these values through a custom generation loop. Only [`TokenIterator`](./tokeniterator.md) reports them; speculative iterators ignore this setting.
- [var maxKVSize: Int?](./generateparameters/maxkvsize.md)
  Maximum size of the key-value cache. Old entries are overwritten while retaining up to the first 4 tokens when the requested size permits. The value must be greater than zero; generation and cache construction throw [`KVCacheConfigurationError.invalidCapacity(_:)`](./kvcacheconfigurationerror/invalidcapacity%28_%29.md) for an invalid value.
- [var maxTokens: Int?](./generateparameters/maxtokens.md)
  Maximum tokens to generate
- [var minP: Float](./generateparameters/minp.md)
  Min-p sampling threshold relative to the highest probability token (0 disables)
- [var prefill: PrefillParameters](./generateparameters/prefill.md)
  How the prompt is prefilled into the cache: step size, chunking strategy, and progress observation. See [`PrefillParameters`](./prefillparameters.md).
- [var prefillStepSize: Int?](./generateparameters/prefillstepsize.md)
  See [`stepSize`](./prefillparameters/stepsize.md).
- [var presenceContextSize: Int](./generateparameters/presencecontextsize.md)
  number of tokens to consider for presence penalty
- [var presencePenalty: Float?](./generateparameters/presencepenalty.md)
  additive penalty for tokens that appear in recent context
- [var quantizedKVStart: Int](./generateparameters/quantizedkvstart.md)
  Step to begin using a quantized KV cache when kvBits is non-nil (default: 0)
- [var repetitionContextSize: Int](./generateparameters/repetitioncontextsize.md)
  Number of tokens to consider for repetition penalty
- [var repetitionPenalty: Float?](./generateparameters/repetitionpenalty.md)
  Penalty factor for repeating tokens
- [var seed: UInt64?](./generateparameters/seed.md)
  Optional seed for reproducible sampling. When set, the sampler’s RNG (`TopPSampler` / `CategoricalSampler`) is seeded deterministically, so the same `(seed, prompt, parameters)` produces the same sampled tokens. `nil` ⇒ the sampler is seeded from system entropy (the prior default). Inert at `temperature == 0` (argmax has no RNG).
- [var temperature: Float](./generateparameters/temperature.md)
  Sampling temperature
- [var toolCallPolicy: ToolCallPolicy](./generateparameters/toolcallpolicy.md)
  Recovery and validation rules for generated tool calls.
- [var topK: Int](./generateparameters/topk.md)
  Top-k sampling (0 disables)
- [var topP: Float](./generateparameters/topp.md)
  Top-p sampling
### Instance Methods
- [func processor() -> LogitProcessor?](./generateparameters/processor%28%29.md)
- [func sampler() -> LogitSampler](./generateparameters/sampler%28%29.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generateparameters)*