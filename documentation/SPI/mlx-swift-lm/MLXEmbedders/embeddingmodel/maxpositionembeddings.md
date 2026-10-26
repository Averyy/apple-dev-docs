---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddingmodel/maxpositionembeddings"
framework: "mlx-swift-lm/MLXEmbedders"
---

# maxPositionEmbeddings

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The maximum number of position embeddings supported by this model, or `nil` if the model uses a position encoding (e.g. RoPE) that handles arbitrary lengths.

## Declaration

```swift
var maxPositionEmbeddings: Int? { get }
```

#### Discussion

Inputs exceeding this length are truncated internally with a warning. Callers may pre-truncate for efficiency or to implement custom strategies (e.g. chunking with pooling).

## Default Implementations

### EmbeddingModel Implementations
- [var maxPositionEmbeddings: Int?](./maxpositionembeddings-92l06.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddingmodel/maxpositionembeddings)*