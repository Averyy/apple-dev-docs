---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/embeddinggemma2embedding/embed(_:task:dimensions:)-9m6eh"
framework: "mlx-swift-lm/MLXVLM"
---

# embed(_:task:dimensions:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Instance Method

Embeds independent items in input order, one at a time to bound working memory. Retrieval uses `.searchQuery` for queries and `.document` for corpus items.

## Declaration

```swift
func embed(_ inputs: [Input], task: Task, dimensions: Int? = nil) async throws -> [[Float]]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/embeddinggemma2embedding/embed(_:task:dimensions:)-9m6eh)*