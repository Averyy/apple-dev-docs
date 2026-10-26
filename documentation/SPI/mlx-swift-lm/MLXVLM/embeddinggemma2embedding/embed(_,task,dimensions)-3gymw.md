---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/embeddinggemma2embedding/embed(_:task:dimensions:)-3gymw"
framework: "mlx-swift-lm/MLXVLM"
---

# embed(_:task:dimensions:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Instance Method

Embeds one item; returns a unit-length float32 vector.

## Declaration

```swift
func embed(_ input: Input, task: Task, dimensions: Int? = nil) async throws -> [Float]
```

#### Discussion

Each media item’s soft tokens are evaluated before the next one is prepared, so only one encoder’s activations are alive at a time.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/embeddinggemma2embedding/embed(_:task:dimensions:)-3gymw)*