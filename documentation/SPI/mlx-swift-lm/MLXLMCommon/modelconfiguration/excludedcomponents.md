---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration/excludedcomponents"
framework: "mlx-swift-lm/MLXLMCommon"
---

# excludedComponents

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Components to never load, such as [`vision`](../modelcomponent/vision.md) for text-only use.

## Declaration

```swift
var excludedComponents: Set<ModelComponent>
```

## Mentions

- [Model Compatibility](../model-compatibility.md)

#### Discussion

Their weights are never read, and inputs that need them fail. You do not need this to save memory: on-demand components, such as the vision encoder of some VLMs, already load the first time an input needs them. Models that cannot load without a component load it anyway; see [`ModelComponentsProviding`](../modelcomponentsproviding.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration/excludedcomponents)*