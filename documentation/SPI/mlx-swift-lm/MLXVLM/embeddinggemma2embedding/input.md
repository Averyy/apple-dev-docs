---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/embeddinggemma2embedding/input"
framework: "mlx-swift-lm/MLXVLM"
---

# EmbeddingGemma2Embedding.Input

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

One independently embedded item: text and media in reading order.

## Declaration

```swift
struct Input
```

## Topics

### Initializers
- [init([Part], title: String?)](./input/init%28_,title%29.md)
- [init(text: String, title: String?, images: [UserInput.Image])](./input/init%28text,title,images%29.md)
  Text followed by images.
### Instance Properties
- [let parts: [Part]](./input/parts.md)
- [let title: String?](./input/title.md)
  A document title or file name; used by the `.document` task.
### Enumerations
- [EmbeddingGemma2Embedding.Input.Part](./input/part.md)
  One piece of an input.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/embeddinggemma2embedding/input)*