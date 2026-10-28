---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcache/maxtrimcount"
framework: "mlx-swift-lm/MLXLMCommon"
---

# maxTrimCount

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Maximum number of newest positions that can be removed with an exact rewind.

## Declaration

```swift
var maxTrimCount: Int { get }
```

## Mentions

- [KV Cache Quantization](../kv-cache-quantization.md)

## Discussion

Unlike [`isTrimmable`](./istrimmable.md), this can describe a bounded rewind into retained history.

## Default Implementations

### KVCache Implementations
- [var maxTrimCount: Int](./maxtrimcount-e5zc.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcache/maxtrimcount)*