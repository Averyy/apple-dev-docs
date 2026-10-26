---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmtyperegistry"
framework: "mlx-swift-lm/MLXVLM"
---

# VLMTypeRegistry

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: enum  
**Role**: Enumeration

Registry of model type, e.g ‘llama’, to functions that can instantiate the model from configuration.

## Declaration

```swift
enum VLMTypeRegistry
```

#### Overview

Typically called via [`load(from:using:configuration:useLatest:progressHandler:)`](./vlmmodelfactory/load%28from,using,configuration,uselatest,progresshandler%29.md).

## Topics

### Type Properties
- [static let shared: ModelTypeRegistry<LanguageModel>](./vlmtyperegistry/shared.md)
  Shared instance with default model types.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmtyperegistry)*