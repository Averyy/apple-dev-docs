---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheconfiguration/capacity-swift.struct"
framework: "mlx-swift-lm/MLXLMCommon"
---

# KVCacheConfiguration.Capacity

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Attention window for caches whose capacity is caller-configurable.

## Declaration

```swift
struct Capacity
```

## Overview

Model-native sliding-window layers retain their architecture-defined window and prefix behavior. This value bounds the remaining attention layers created by the model’s `newCache(parameters:)` implementation. A configured [`KVCacheConfiguration.Rewind`](./rewind-swift.struct.md) reserve adds storage beyond this window.

## Topics

### Initializers
- [init(maxTokens: Int, preservedPrefixTokens: Int) throws](./capacity-swift.struct/init%28maxtokens,preservedprefixtokens%29.md)
### Instance Properties
- [let maxTokens: Int](./capacity-swift.struct/maxtokens.md)
- [let preservedPrefixTokens: Int](./capacity-swift.struct/preservedprefixtokens.md)
### Default Implementations
- [Equatable Implementations](./capacity-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheconfiguration/capacity-swift.struct)*