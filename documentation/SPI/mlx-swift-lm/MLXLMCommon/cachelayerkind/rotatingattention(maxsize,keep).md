---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/cachelayerkind/rotatingattention(maxsize:keep:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# CacheLayerKind.rotatingAttention(maxSize:keep:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

Sliding / rotating attention window ([`RotatingKVCache`](../rotatingkvcache.md)).

## Declaration

```swift
case rotatingAttention(maxSize: Int, keep: Int)
```

## Discussion

Used both for architecture-imposed sliding-window attention and for caller-requested capacity limits on full-attention layers.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/cachelayerkind/rotatingattention(maxsize:keep:))*