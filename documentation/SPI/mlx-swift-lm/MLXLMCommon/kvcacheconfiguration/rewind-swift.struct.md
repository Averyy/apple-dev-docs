---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheconfiguration/rewind-swift.struct"
framework: "mlx-swift-lm/MLXLMCommon"
---

# KVCacheConfiguration.Rewind

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Extra historical rows retained by rotating caches for exact prefix rewinds.

## Declaration

```swift
struct Rewind
```

## Overview

This adds storage beyond each attention window without widening attention. Rewinds beyond the available history still require rebuilding the cache.

## Topics

### Initializers
- [init(maxTokens: Int) throws](./rewind-swift.struct/init%28maxtokens%29.md)
### Instance Properties
- [let maxTokens: Int](./rewind-swift.struct/maxtokens.md)
### Default Implementations
- [Equatable Implementations](./rewind-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheconfiguration/rewind-swift.struct)*