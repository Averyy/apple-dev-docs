---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/gemma3modelbackbone"
framework: "mlx-swift-lm/MLXEmbedders"
---

# Gemma3ModelBackbone

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: class  
**Role**: Class

The core backbone of the Gemma 3 model.

## Declaration

```swift
class Gemma3ModelBackbone
```

## Overview

This module handles token embeddings, the sequence of transformer blocks, and the final normalization. It is used as the base for the embedding model.

## Topics

### Initializers
- [init(Gemma3Configuration)](./gemma3modelbackbone/init%28_%29.md)
  Initializes the model backbone.
### Instance Methods
- [func callAsFunction(MLXArray, attentionMask: MLXArray?) -> MLXArray](./gemma3modelbackbone/callasfunction%28_,attentionmask%29.md)
  Processes input tokens through the model backbone.

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/gemma3modelbackbone)*