---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rotatingkvcache/trim(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# trim(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Rewind the newest `n` positions.

## Declaration

```swift
@discardableResult
override func trim(_ n: Int) -> Int
```

## Mentions

- [KV Cache Quantization](../kv-cache-quantization.md)

#### Discussion

Before the ring wraps this is exact bookkeeping. After it wraps, the ring is linearized and the newest rows are cut: the cache stays consistent and the logical offset rewinds, but rows the rewound writes overwrote at the old edge of the window cannot come back, so the window is up to `n` rows short until it refills. An exact rewind requires `n <= maxTrimCount`; a configured reserve extends that limit beyond rotation. Once older rows have been evicted, trimming stops at the pinned `keep` prefix.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rotatingkvcache/trim(_:))*