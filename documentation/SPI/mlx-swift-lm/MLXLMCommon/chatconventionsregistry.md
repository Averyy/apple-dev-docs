---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatconventionsregistry"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ChatConventionsRegistry

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Ordered registry of [`ChatConventionsResolving`](./chatconventionsresolving.md) consulted by the model factories.

## Declaration

```swift
final class ChatConventionsRegistry
```

## Overview

Resolution precedence when a model is loaded:

1. an explicit value already set on the `ModelConfiguration` (registry entry or caller),
2. a registered resolver here,
3. the model’s own [`ChatConventionsProviding`](./chatconventionsproviding.md) declaration.

Resolvers sit above the model because repo-id knowledge is more specific than model-intrinsic knowledge, and so that a downstream package can correct a built-in declaration without constructing a `ModelConfiguration`.

Most recently registered wins: [`register(_:)`](./chatconventionsregistry/register%28_%29.md) appends, and lookup walks the resolvers in reverse registration order, returning the first non-`nil` answer.

## Topics

### Initializers
- [init(resolvers: [any ChatConventionsResolving])](./chatconventionsregistry/init%28resolvers%29.md)
### Instance Methods
- [func reasoningConfig(modelId: String, modelType: String) -> ReasoningConfig?](./chatconventionsregistry/reasoningconfig%28modelid,modeltype%29.md)
  First reasoning config offered by a resolver, in reverse registration order.
- [func register(any ChatConventionsResolving)](./chatconventionsregistry/register%28_%29.md)
  Add a resolver. It takes precedence over everything registered before it.
- [func toolCallFormat(modelId: String, modelType: String) -> ToolCallFormat?](./chatconventionsregistry/toolcallformat%28modelid,modeltype%29.md)
  First tool-call format offered by a resolver, in reverse registration order.
### Type Properties
- [static let shared: ChatConventionsRegistry](./chatconventionsregistry/shared.md)
  Shared instance, preloaded with this package’s built-in resolvers.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatconventionsregistry)*