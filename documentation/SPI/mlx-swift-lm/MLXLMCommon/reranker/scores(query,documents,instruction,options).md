---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reranker/scores(query:documents:instruction:options:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# scores(query:documents:instruction:options:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Score documents while preserving their original order.

## Declaration

```swift
func scores(query: String, documents: [String], instruction: String?, options: RerankExecutionOptions) async throws -> RerankResponse
```

## Default Implementations

### Reranker Implementations
- [func scores(query: String, documents: [RerankDocument], instruction: String?, options: RerankExecutionOptions) async throws -> RerankDocumentsResponse](./scores%28query,documents,instruction,options%29-615k0.md)
  Score structured documents while preserving their original order.
- [func scores(query: String, documents: [String], instruction: String?, options: RerankExecutionOptions) async throws -> RerankResponse](./scores%28query,documents,instruction,options%29-mwn4.md)
  Score documents without changing their original order.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reranker/scores(query:documents:instruction:options:))*