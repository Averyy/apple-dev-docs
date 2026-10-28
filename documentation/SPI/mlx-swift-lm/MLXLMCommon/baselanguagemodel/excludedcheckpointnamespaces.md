---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baselanguagemodel/excludedcheckpointnamespaces"
framework: "mlx-swift-lm/MLXLMCommon"
---

# excludedCheckpointNamespaces

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Serialized namespaces whose tensors this model never loads, such as the target model in a checkpoint that a drafter shares with it. The loader does not read them.

## Declaration

```swift
var excludedCheckpointNamespaces: [String] { get }
```

## Mentions

- [Model Compatibility](../model-compatibility.md)

## Discussion

Namespaces match whole dot-separated prefixes of the names before [`prepareCheckpoint(_:)`](./preparecheckpoint%28_%29.md). The default is empty.

## Default Implementations

### BaseLanguageModel Implementations
- [var excludedCheckpointNamespaces: [String]](./excludedcheckpointnamespaces-7pg.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baselanguagemodel/excludedcheckpointnamespaces)*