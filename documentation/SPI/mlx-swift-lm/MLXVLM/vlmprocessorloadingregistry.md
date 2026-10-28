---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmprocessorloadingregistry"
framework: "mlx-swift-lm/MLXVLM"
---

# VLMProcessorLoadingRegistry

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

Ordered registry of processor-loading resolvers used by [`VLMModelFactory`](./vlmmodelfactory.md).

## Declaration

```swift
final class VLMProcessorLoadingRegistry
```

## Overview

Most recently registered wins for each hook independently. This lets a downstream package choose one value while deferring the other to an earlier resolver.

## Topics

### Initializers
- [init(resolvers: [any VLMProcessorLoadingResolver])](./vlmprocessorloadingregistry/init%28resolvers%29.md)
### Instance Methods
- [func register(any VLMProcessorLoadingResolver)](./vlmprocessorloadingregistry/register%28_%29.md)
  Add a resolver. It takes precedence over resolvers registered before it.
### Type Properties
- [static let shared: VLMProcessorLoadingRegistry](./vlmprocessorloadingregistry/shared.md)
  Shared instance, preloaded with this package’s built-in loading rules.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmprocessorloadingregistry)*