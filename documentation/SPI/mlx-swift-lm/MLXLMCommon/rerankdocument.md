---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankdocument"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RerankDocument

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

A text document with an application-defined identifier and metadata.

## Declaration

```swift
struct RerankDocument
```

## Overview

The reranker evaluates only [`text`](./rerankdocument/text.md). The identifier and metadata are carried through unchanged so callers can reconnect results to their retrieval records without copying model-specific data into the scoring layer.

## Topics

### Initializers
- [init(id: String, text: String, metadata: [String : String])](./rerankdocument/init%28id,text,metadata%29.md)
### Instance Properties
- [var id: String](./rerankdocument/id.md)
  Application-defined stable identifier.
- [var metadata: [String : String]](./rerankdocument/metadata.md)
  Application metadata preserved in results but not evaluated by the model.
- [var text: String](./rerankdocument/text.md)
  Text evaluated by the reranker.
### Default Implementations
- [Equatable Implementations](./rerankdocument/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Identifiable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankdocument)*