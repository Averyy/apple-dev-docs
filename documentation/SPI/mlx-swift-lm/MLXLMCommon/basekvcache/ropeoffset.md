---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/basekvcache/ropeoffset"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ropeOffset

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

RoPE offset for this cache. `open` so subclasses can return a non-scalar offset (e.g. a batched cache’s per-row `.batch(...)`).

## Declaration

```swift
var ropeOffset: RoPEOffset { get }
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/basekvcache/ropeoffset)*