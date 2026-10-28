---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmprocessorloadingresolver"
framework: "mlx-swift-lm/MLXVLM"
---

# VLMProcessorLoadingResolver

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: protocol  
**Role**: Protocol

Supplies model-specific processor loading policy that is not present in a checkpoint.

## Declaration

```swift
protocol VLMProcessorLoadingResolver : Sendable
```

## Overview

Both hooks are optional. A fallback is consulted only when neither `preprocessor_config.json` nor `processor_config.json` exists. Processor type resolvers are consulted after a configuration has been selected, so they can supply missing metadata or correct metadata shipped by a checkpoint.

## Topics

### Instance Methods
- [func fallbackProcessorConfiguration(for: VLMProcessorLoadingContext) throws -> VLMProcessorConfiguration?](./vlmprocessorloadingresolver/fallbackprocessorconfiguration%28for%29.md)
- [func processorType(for: VLMProcessorLoadingContext, declaredProcessorType: String?) throws -> String?](./vlmprocessorloadingresolver/processortype%28for,declaredprocessortype%29.md)
  The processor type to use for this model, or `nil` to defer to another resolver or the checkpoint declaration. `declaredProcessorType` is `nil` when the selected processor configuration does not contain `processor_class`.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [ModelTypeProcessorResolver](./modeltypeprocessorresolver.md)
- [Qwen35ProcessorLoadingResolver](./qwen35processorloadingresolver.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmprocessorloadingresolver)*