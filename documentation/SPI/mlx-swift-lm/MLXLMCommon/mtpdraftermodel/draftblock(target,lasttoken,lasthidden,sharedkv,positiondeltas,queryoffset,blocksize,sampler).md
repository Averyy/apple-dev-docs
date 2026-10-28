---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodel/draftblock(target:lasttoken:lasthidden:sharedkv:positiondeltas:queryoffset:blocksize:sampler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# draftBlock(target:lastToken:lastHidden:sharedKV:positionDeltas:queryOffset:blockSize:sampler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

K-step drafting from a constant position.

## Declaration

```swift
func draftBlock(target: any LanguageModel, lastToken: MLXArray, lastHidden: MLXArray, sharedKV: [String : (MLXArray, MLXArray)], positionDeltas: MLXArray?, queryOffset: Int, blockSize: Int, sampler: any LogitSampler) -> MLXArray
```

## Return Value

`[B, blockSize - 1]` token array.

## Discussion

Returns the proposed tokens as a `[B, blockSize - 1]` MLXArray. The drafter holds no transient round-state on the model instance — every per-round input is threaded as a method argument.

## Parameters

- `target`: The main language model this drafter is speculating for. Used to look up target-derived constants (input embeddings, embed scale, etc.) inline per round; conformers must not retain or mutate references derived from `target`.
- `lastToken`: Bonus token from the target’s last verify pass, shape `[B]`.
- `lastHidden`: Target’s last hidden state, shape `[B, 1, backbone_hidden_size]`.
- `sharedKV`: Dict keyed by `layer_type` (`"full_attention"` / `"sliding_attention"`) mapping to `(keys, values)` `MLXArray`s for the last layer of that layer-type in the target.
- `positionDeltas`: Optional target-emitted position delta state for multimodal RoPE models whose continuation positions are not derivable from cache length alone.
- `queryOffset`: Constant absolute position for the round (the position the bonus token sits at in the target’s KV cache). Passed as a Swift `Int` rather than an `MLXArray` to avoid the `.item()` round-trip that would otherwise stall the GPU per speculation round.
- `blockSize`: Total tokens in the round (the drafter returns `blockSize - 1`; the bonus token is implicit).
- `sampler`: `LogitSampler` to apply to each step’s logits.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodel/draftblock(target:lasttoken:lasthidden:sharedkv:positiondeltas:queryoffset:blocksize:sampler:))*