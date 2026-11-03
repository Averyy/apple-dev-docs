---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelmemory"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelMemory

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

The memory held by a model’s tensors, measured from their MLX buffers.

## Declaration

```swift
struct ModelMemory
```

## Mentions

- [Wired Memory and Weight Reservations](./wired-memory.md)

## Overview

A buffer shared by several tensors is counted once. It is attributed to the model first, then to on-demand components in name order. A component counts once its load has finished.

KV caches, temporary arrays, and the tokenizer are not included. For the cache, use [`memoryBytes`](./kvcachestatus/memorybytes.md).

```swift
let memory = try await container.memory()
print(memory.model, memory.total)
for component in memory.components {
    print(component.kind.name, component.bytes)
}
```

## Topics

### Structures
- [ModelMemory.Component](./modelmemory/component.md)
  The share of buffers attributed to a loaded component.
### Initializers
- [init(model: Int)](./modelmemory/init%28model%29.md)
### Instance Properties
- [let components: [Component]](./modelmemory/components.md)
  Bytes attributed to loaded on-demand components, ordered by component name.
- [let model: Int](./modelmemory/model.md)
  Bytes held by the model’s own tensors.
- [var total: Int](./modelmemory/total.md)
  Total bytes attributed to the model and its loaded components.
### Default Implementations
- [Equatable Implementations](./modelmemory/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelmemory)*