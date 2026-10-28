---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/kvcacheruntimereport()"
framework: "mlx-swift-lm/MLXLMCommon"
---

# kvCacheRuntimeReport()

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Return the legacy runtime-only view of the configured KV-cache strategy.

> **Deprecated**: Use cacheStatus() for unified cache diagnostics.

## Declaration

```swift
func kvCacheRuntimeReport() async throws -> KVCacheRuntimeReport?
```

## Discussion

The report is `nil` until a typed or legacy cache configuration exists, or when the session currently stores history rather than a realized cache.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/kvcacheruntimereport())*