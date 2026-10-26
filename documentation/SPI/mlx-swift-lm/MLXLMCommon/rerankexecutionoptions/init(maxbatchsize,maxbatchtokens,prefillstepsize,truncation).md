---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankexecutionoptions/init(maxbatchsize:maxbatchtokens:prefillstepsize:truncation:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(maxBatchSize:maxBatchTokens:prefillStepSize:truncation:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Create execution options for pairwise and listwise rerankers.

## Declaration

```swift
init(maxBatchSize: Int = 16, maxBatchTokens: Int = 8_192, prefillStepSize: Int = 512, truncation: RerankTruncationPolicy = .truncate)
```

## Parameters

- `maxBatchSize`: Maximum number of pairs evaluated in one batch.
- `maxBatchTokens`: Maximum token allocation for one model forward pass.
- `prefillStepSize`: Preferred cached prefill chunk size for causal models.
- `truncation`: Behavior for inputs that exceed the model context limit.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankexecutionoptions/init(maxbatchsize:maxbatchtokens:prefillstepsize:truncation:))*