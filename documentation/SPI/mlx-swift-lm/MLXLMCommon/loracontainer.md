---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loracontainer"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LoRAContainer

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

A container for managing LoRA or DoRA adapters and applying them to a language model.

## Declaration

```swift
struct LoRAContainer
```

## Overview

This struct conforms to `ModelAdapter` and can dynamically inject, remove, or fuse adapters into a model at runtime.

## Topics

### Initializers
- [init(configuration: LoRAConfiguration, parameters: consuming ModuleParameters)](./loracontainer/init%28configuration,parameters%29.md)
### Instance Properties
- [let configuration: LoRAConfiguration](./loracontainer/configuration.md)
  The configuration used to construct this adapter container.
- [let parameters: ModuleParameters](./loracontainer/parameters.md)
  The parameter values for the adapter modules.
### Instance Methods
- [func fuse(with: LanguageModel) throws](./loracontainer/fuse%28with%29.md)
  Permanently fuses the adapter weights into the model’s base layers.
- [func load(into: LanguageModel) throws](./loracontainer/load%28into%29.md)
  Applies adapter modules (LoRA or DoRA) to the given model.
- [func unload(from: LanguageModel)](./loracontainer/unload%28from%29.md)
  Removes adapter layers (LoRA or DoRA) and restores the model to its original form.
### Type Methods
- [static func from(directory: URL) throws -> LoRAContainer](./loracontainer/from%28directory%29.md)
  Loads a `LoRAContainer` from a directory containing adapter weights and configuration.
- [static func from(model: LanguageModel, configuration: LoRAConfiguration) throws -> LoRAContainer](./loracontainer/from%28model,configuration%29.md)
  Creates a `LoRAContainer` by applying the configuration to a compatible `LanguageModel`.
- [static func fromPEFT(directory: URL, numLayers: Int) throws -> LoRAContainer](./loracontainer/frompeft%28directory,numlayers%29.md)
  Loads a PEFT-format LoRA adapter directory and returns a [`LoRAContainer`](./loracontainer.md) you can [`load(into:)`](./loracontainer/load%28into%29.md) on a model.

## Relationships

### Conforms To
- [ModelAdapter](./modeladapter.md)
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loracontainer)*