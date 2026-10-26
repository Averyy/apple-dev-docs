---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/nomicbertmodel/init(_:pooler:lmhead:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# init(_:pooler:lmHead:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: init  
**Role**: Initializer

Initializes the Nomic BERT model.

## Declaration

```swift
init(_ config: NomicBertConfiguration, pooler: Bool = true, lmHead: Bool = false)
```

## Parameters

- `config`: The model configuration.
- `pooler`: If `true`, initializes a linear pooling layer for sequence classification/embedding tasks.
- `lmHead`: If `true`, initializes the language modeling head for token prediction.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/nomicbertmodel/init(_:pooler:lmhead:))*