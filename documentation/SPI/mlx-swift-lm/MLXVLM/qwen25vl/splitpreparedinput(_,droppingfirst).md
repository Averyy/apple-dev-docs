---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen25vl/splitpreparedinput(_:droppingfirst:)"
framework: "mlx-swift-lm/MLXVLM"
---

# splitPreparedInput(_:droppingFirst:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Instance Method

Opt into `ChatSession` warm-cache reuse for append-only media turns by delegating to `QwenVL.splitPreparedInput` with this model’s image and video token ids and spatial merge size.

## Declaration

```swift
func splitPreparedInput(_ input: LMInput, droppingFirst prefixTokenCount: Int) -> LMInput?
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen25vl/splitpreparedinput(_:droppingfirst:))*