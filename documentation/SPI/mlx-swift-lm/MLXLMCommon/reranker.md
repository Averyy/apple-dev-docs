---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reranker"
framework: "mlx-swift-lm/MLXLMCommon"
---

# Reranker

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Architecture-neutral interface for local reranker models.

## Declaration

```swift
protocol Reranker : Sendable
```

## Overview

Use [`scores(query:documents:instruction:options:)`](./reranker/scores%28query,documents,instruction,options%29.md) when scores must stay aligned with the input documents. Use [`rerank(_:options:)`](./reranker/rerank%28_,options%29.md) for sorted retrieval results.

Rerankers consume document text rather than cached document embeddings. Pairwise cross-encoders jointly encode each query-document pair, while listwise models jointly encode the query and complete candidate set. Independently computed document embeddings therefore cannot reproduce their relevance scores.

## Topics

### Instance Properties
- [var modelID: String](./reranker/modelid.md)
  Identifier of the loaded model.
- [var scoreKind: RerankScoreKind](./reranker/scorekind.md)
  Semantic meaning and numeric range of returned scores.
### Instance Methods
- [func rerank(RerankRequest, options: RerankExecutionOptions) async throws -> RerankResponse](./reranker/rerank%28_,options%29.md)
  Score and sort documents by descending relevance.
- [func rerank(query: String, documents: [RerankDocument], instruction: String?, topK: Int?, minimumScore: Double?, options: RerankExecutionOptions) async throws -> RerankDocumentsResponse](./reranker/rerank%28query,documents,instruction,topk,minimumscore,options%29-3aqce.md)
  Score and sort structured documents by descending relevance.
- [func rerank(query: String, documents: [String], instruction: String?, topK: Int?, minimumScore: Double?, options: RerankExecutionOptions) async throws -> RerankResponse](./reranker/rerank%28query,documents,instruction,topk,minimumscore,options%29-4wtew.md)
  Score and sort documents by descending relevance.
- [func scores(query: String, documents: [String], instruction: String?, options: RerankExecutionOptions) async throws -> RerankResponse](./reranker/scores%28query,documents,instruction,options%29.md)
  Score documents while preserving their original order.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [RerankerContainer](./rerankercontainer.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reranker)*