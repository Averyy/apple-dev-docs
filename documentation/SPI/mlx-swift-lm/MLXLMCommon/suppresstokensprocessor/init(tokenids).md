---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/suppresstokensprocessor/init(tokenids:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(tokenIds:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Create a processor masking the given token IDs.

## Declaration

```swift
init?(tokenIds: Set<Int>)
```

#### Discussion

Negative IDs are ignored. Returns `nil` when no valid IDs remain (nothing to suppress).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/suppresstokensprocessor/init(tokenids:))*