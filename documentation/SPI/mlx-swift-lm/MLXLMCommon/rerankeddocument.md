---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankeddocument"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RerankedDocument

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

A structured document and its relevance score.

## Declaration

```swift
struct RerankedDocument
```

## Topics

### Initializers
- [init(index: Int, document: RerankDocument, score: Double)](./rerankeddocument/init%28index,document,score%29.md)
### Instance Properties
- [let document: RerankDocument](./rerankeddocument/document.md)
  The original document, including its identifier and metadata.
- [let index: Int](./rerankeddocument/index.md)
  The document’s position in the request array.
- [let score: Double](./rerankeddocument/score.md)
  The model’s relevance score.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankeddocument)*