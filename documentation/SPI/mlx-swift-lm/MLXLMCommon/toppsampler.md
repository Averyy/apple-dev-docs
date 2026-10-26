---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toppsampler"
framework: "mlx-swift-lm/MLXLMCommon"
---

# TopPSampler

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Sampler that uses probability filters (`topP`, `topK`, `minP`) and `temperature` to sample the logits.

## Declaration

```swift
struct TopPSampler
```

#### Overview

Filters are applied in the same order as Python mlx-lm: top_p → min_p → top_k. Each filter operates on the full vocabulary in original token order, masking rejected tokens with `-inf`. This matches the composable filter chain in `mlx_lm.sample_utils.make_sampler`.

## Topics

### Initializers
- [init(temperature: Float, topP: Float, topK: Int, minP: Float, seed: UInt64?)](./toppsampler/init%28temperature,topp,topk,minp,seed%29.md)
### Instance Methods
- [func sample(logits: MLXArray) -> MLXArray](./toppsampler/sample%28logits%29.md)

## Relationships

### Conforms To
- [LogitSampler](./logitsampler.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toppsampler)*