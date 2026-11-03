---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelmemoryreporting"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelMemoryReporting

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

A type that owns a loaded model and can measure its tensor buffers.

## Declaration

```swift
protocol ModelMemoryReporting : Sendable
```

## Overview

[`ModelContainer`](./modelcontainer.md) and `EmbedderModelContainer` conform, so code that only needs memory can accept either one.

## Topics

### Instance Methods
- [func memory() async throws -> ModelMemory](./modelmemoryreporting/memory%28%29.md)
  Measure the current model tensor buffers, including loaded on-demand components.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [ModelContainer](./modelcontainer.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelmemoryreporting)*