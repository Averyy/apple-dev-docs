---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcomponent"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelComponent

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

A part of a model that can load separately from the rest, such as the vision encoder of a VLM.

## Declaration

```swift
struct ModelComponent
```

## Mentions

- [Model Compatibility](./model-compatibility.md)

## Overview

A model declares its components through [`ModelComponentsProviding`](./modelcomponentsproviding.md). A component that the model lists in [`onDemandComponents`](./modelcomponentsproviding/ondemandcomponents.md) loads the first time an input needs it. List a component in [`excludedComponents`](./modelconfiguration/excludedcomponents.md) to never load it.

## Topics

### Initializers
- [init(String)](./modelcomponent/init%28_%29.md)
### Instance Properties
- [var description: String](./modelcomponent/description.md)
- [let name: String](./modelcomponent/name.md)
### Type Properties
- [static let audio: ModelComponent](./modelcomponent/audio.md)
  Audio encoders, with the projectors that feed them to the language model.
- [static let vision: ModelComponent](./modelcomponent/vision.md)
  Image and video encoders, with the projectors that feed them to the language model.
### Default Implementations
- [Equatable Implementations](./modelcomponent/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcomponent)*