---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/prepare(_:cache:state:prefill:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# prepare(_:cache:state:prefill:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Prepare the cache state and consume the [`LMInput`](../lminput.md).

## Declaration

```swift
func prepare(_ input: LMInput, cache: [KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult
```

#### Discussion

`state` is the [`state`](../lmoutput/state-swift.property.md) a caller carried over from earlier evaluation against the same `cache` — present when `cache` is already warm (a multi-turn chat, a tool-call restart, a restored prompt cache). Models that keep per-call positional state (e.g. the M-RoPE `ropeDeltas` of the Qwen VLM families) use it to anchor the new tokens’ positions at the cache offset; models without such state can ignore it. In the typical cold call it is `nil`.

This can return:

- [`PrepareResult.tokens(_:)`](../prepareresult/tokens%28_%29.md) if the caller should evaluate the (remaining) tokens normally
- [`PrepareResult.logits(_:)`](../prepareresult/logits%28_%29.md) to produce the next token from the prompt

Implementations that chunk the prompt should drive the loop with [`forEachChunk(total:reserving:defaultStepSize:maximumStepSize:_:)`](../prefillparameters/foreachchunk%28total,reserving,defaultstepsize,maximumstepsize,_%29.md), which owns cancellation, pooling, buffer cache clearing, and per-chunk progress. An implementation returning `.logits` owns its whole [`progress`](../prefillparameters/progress.md) sequence, including the terminal `(total, total)`; one returning `.tokens` reports only its own chunks — the iterator that evaluates the remainder completes the sequence.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/prepare(_:cache:state:prefill:))*