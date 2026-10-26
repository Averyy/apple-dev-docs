---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankexecutionoptions"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RerankExecutionOptions

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Resource limits and execution behavior for a reranking operation.

## Declaration

```swift
struct RerankExecutionOptions
```

## Topics

### Initializers
- [init(maxBatchSize: Int, maxBatchTokens: Int, prefillStepSize: Int, truncation: RerankTruncationPolicy)](./rerankexecutionoptions/init%28maxbatchsize,maxbatchtokens,prefillstepsize,truncation%29.md)
  Create execution options for pairwise and listwise rerankers.
### Instance Properties
- [var maxBatchSize: Int](./rerankexecutionoptions/maxbatchsize.md)
  Maximum number of query-document pairs in one pairwise model batch.
- [var maxBatchTokens: Int](./rerankexecutionoptions/maxbatchtokens.md)
  Maximum number of token slots in one model forward pass.
- [var prefillStepSize: Int](./rerankexecutionoptions/prefillstepsize.md)
  Preferred number of tokens processed by each cached causal-model prefill step.
- [var truncation: RerankTruncationPolicy](./rerankexecutionoptions/truncation.md)
  Behavior when an input exceeds the model context limit.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankexecutionoptions)*