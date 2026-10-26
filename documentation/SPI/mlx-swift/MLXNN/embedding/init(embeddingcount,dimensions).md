---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/embedding/init(embeddingcount:dimensions:)"
framework: "mlx-swift/MLXNN"
---

# init(embeddingCount:dimensions:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Implements a simple lookup table that maps each input integer to a high-dimensional vector.

## Declaration

```swift
init(embeddingCount: Int, dimensions: Int)
```

#### Discussion

Typically used to embed discrete tokens for processing by neural networks.

## Parameters

- `embeddingCount`: How many possible discrete tokens can we embed.  Usually called the vocabulary size.
- `dimensions`: Dimensionality of the embeddings.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/embedding/init(embeddingcount:dimensions:))*