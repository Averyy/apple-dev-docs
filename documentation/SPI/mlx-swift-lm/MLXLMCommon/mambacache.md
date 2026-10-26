---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mambacache"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MambaCache

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Simple cache for Mamba-style state space models

## Declaration

```swift
class MambaCache
```

## Topics

### Initializers
- [init(leftPadding: [Int]?)](./mambacache/init%28leftpadding%29.md)
### Instance Methods
- [func copy() -> any KVCache](./mambacache/copy%28%29.md)
### Type Properties
- [class var serializedClassName: String?](./mambacache/serializedclassname.md)
### Type Methods
- [class func restore(state: [MLXArray], metaState: [String]) throws -> any KVCache](./mambacache/restore%28state,metastate%29.md)

## Relationships

### Inherits From
- [ArraysCache](./arrayscache.md)
### Conforms To
- [KVCache](./kvcache.md)
- MLX.Evaluatable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mambacache)*