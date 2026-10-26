---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddermodelcontainer/perform(_:)-37clz"
framework: "mlx-swift-lm/MLXEmbedders"
---

# perform(_:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

> **Deprecated**: use perform(_: (EmbedderModelContext) -> R) instead

## Declaration

```swift
func perform<R>(_ action: @Sendable (EmbeddingModel, Tokenizer, Pooling) async throws -> sending R) async rethrows -> sending R where R : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddermodelcontainer/perform(_:)-37clz)*