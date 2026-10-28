---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheruntimereport"
framework: "mlx-swift-lm/MLXLMCommon"
---

# KVCacheRuntimeReport

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Effective per-layer state for a configured KV cache.

## Declaration

```swift
struct KVCacheRuntimeReport
```

## Overview

Prefer [`KVCacheStatus`](./kvcachestatus.md) for application diagnostics. This report remains useful when directly applying a configuration to a raw cache array.

## Topics

### Instance Properties
- [var compressedLayerCount: Int](./kvcacheruntimereport/compressedlayercount.md)
- [let layers: [Layer]](./kvcacheruntimereport/layers.md)
- [var pendingLayerCount: Int](./kvcacheruntimereport/pendinglayercount.md)
- [let processedTokenCount: Int?](./kvcacheruntimereport/processedtokencount.md)
  Authoritative model-wide position when the report comes from shared cache storage. Raw array reports leave this value `nil`.
- [let requestedConfiguration: KVCacheConfiguration](./kvcacheruntimereport/requestedconfiguration.md)
- [var skippedLayerCount: Int](./kvcacheruntimereport/skippedlayercount.md)
### Type Aliases
- [KVCacheRuntimeReport.Layer](./kvcacheruntimereport/layer.md)
### Default Implementations
- [Equatable Implementations](./kvcacheruntimereport/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheruntimereport)*