---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/cachelayerkind/attention(maxsize:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# CacheLayerKind.attention(maxSize:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

Standard or implementation-defined attention KV.

## Declaration

```swift
case attention(maxSize: Int?)
```

#### Discussion

A `nil` `maxSize` is unbounded. A non-nil value describes a bounded custom cache that is not a [`RotatingKVCache`](../rotatingkvcache.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/cachelayerkind/attention(maxsize:))*