---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankrequest/init(query:documents:instruction:topk:minimumscore:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(query:documents:instruction:topK:minimumScore:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Create a request for sorted reranking.

## Declaration

```swift
init(query: String, documents: [String], instruction: String? = nil, topK: Int? = nil, minimumScore: Double? = nil)
```

## Parameters

- `query`: Search query or user intent.
- `documents`: Candidate documents to score.
- `instruction`: Optional task instruction for instruction-aware models.
- `topK`: Maximum number of sorted results to return, or `nil` for all results.
- `minimumScore`: Inclusive score threshold applied before `topK`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankrequest/init(query:documents:instruction:topk:minimumscore:))*