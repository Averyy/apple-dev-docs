---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/cachelayerkind/statespace"
framework: "mlx-swift-lm/MLXLMCommon"
---

# CacheLayerKind.stateSpace

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

Fixed-size state-space / Mamba / GDN recurrent state ([`MambaCache`](../mambacache.md)).

## Declaration

```swift
case stateSpace
```

## Discussion

These caches are not token-windowed; a [`maxKVSize`](../generateparameters/maxkvsize.md) policy does not apply to them.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/cachelayerkind/statespace)*