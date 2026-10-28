---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/synchronize()"
framework: "mlx-swift-lm/MLXLMCommon"
---

# synchronize()

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Wait for exclusive access to the KVCache.

## Declaration

```swift
func synchronize() async
```

## Discussion

This is useful for cases where a program is terminating and wants to ensure that any async operations are complete.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/synchronize())*