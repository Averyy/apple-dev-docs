---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/bertmodel/init(_:lmhead:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# init(_:lmHead:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: init  
**Role**: Initializer

Initializes a BERT model.

## Declaration

```swift
init(_ config: BertConfiguration, lmHead: Bool = false)
```

## Parameters

- `config`: The architecture settings (layers, heads, dimensions).
- `lmHead`: If `true`, includes the decoder head for token prediction. If `false`, includes a pooler for sentence embeddings.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/bertmodel/init(_:lmhead:))*