---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankercontainer/rerank(query:documents:instruction:topk:minimumscore:options:)-91ali"
framework: "mlx-swift-lm/MLXLMCommon"
---

# rerank(query:documents:instruction:topK:minimumScore:options:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Score and sort documents by descending relevance.

## Declaration

```swift
func rerank(query: String, documents: [String], instruction: String? = nil, topK: Int? = nil, minimumScore: Double? = nil, options: RerankExecutionOptions = .init()) async throws -> RerankResponse
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankercontainer/rerank(query:documents:instruction:topk:minimumscore:options:)-91ali)*