---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/resolvedmodelconfiguration"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ResolvedModelConfiguration

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

A fully resolved model configuration where all sources have been resolved to local directory paths.

## Declaration

```swift
struct ResolvedModelConfiguration
```

#### Overview

Created by resolving a [`ModelConfiguration`](./modelconfiguration.md) — downloading remote sources via a [`Downloader`](./downloader.md) and mapping behavioral properties. Factory implementations receive this type in their `_load` method, so they work purely with local files.

## Topics

### Initializers
- [init(directory: URL)](./resolvedmodelconfiguration/init%28directory%29.md)
  Convenience for loading everything from a single local directory.
- [init(modelDirectory: URL, tokenizerDirectory: URL, name: String, defaultPrompt: String, extraEOSTokens: Set<String>, stopStrings: Set<String>?, eosTokenIds: Set<Int>, toolCallFormat: ToolCallFormat?, reasoningConfig: ReasoningConfig?, messageGenerator: (any MessageGenerator)?, weightFileSelection: WeightFileSelection, excludedComponents: Set<ModelComponent>)](./resolvedmodelconfiguration/init%28modeldirectory,tokenizerdirectory,name,defaultprompt,extraeostokens,stopstrings,eostokenids,toolcallformat,reasoningconfig,messagegenerator,weightfileselection,excludedcomponents%29.md)
### Instance Properties
- [var defaultPrompt: String](./resolvedmodelconfiguration/defaultprompt.md)
- [var eosTokenIds: Set<Int>](./resolvedmodelconfiguration/eostokenids.md)
- [var excludedComponents: Set<ModelComponent>](./resolvedmodelconfiguration/excludedcomponents.md)
  Components to load the model without.
- [var extraEOSTokens: Set<String>](./resolvedmodelconfiguration/extraeostokens.md)
- [var messageGenerator: (any MessageGenerator)?](./resolvedmodelconfiguration/messagegenerator.md)
- [var modelDirectory: URL](./resolvedmodelconfiguration/modeldirectory.md)
- [var name: String](./resolvedmodelconfiguration/name.md)
- [var reasoningConfig: ReasoningConfig?](./resolvedmodelconfiguration/reasoningconfig.md)
- [var stopStrings: Set<String>](./resolvedmodelconfiguration/stopstrings.md)
- [var tokenizerDirectory: URL](./resolvedmodelconfiguration/tokenizerdirectory.md)
- [var toolCallFormat: ToolCallFormat?](./resolvedmodelconfiguration/toolcallformat.md)
- [var weightFileSelection: WeightFileSelection](./resolvedmodelconfiguration/weightfileselection.md)
  How to choose the safetensors files holding the model’s weights.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Related Documentation
- [func resolved(modelDirectory: URL, tokenizerDirectory: URL) -> ResolvedModelConfiguration](./modelconfiguration/resolved%28modeldirectory,tokenizerdirectory%29.md)
  Maps this configuration’s behavioral properties into a [`ResolvedModelConfiguration`](./resolvedmodelconfiguration.md) with the given directories.
- [protocol Downloader](./downloader.md)
  A protocol for downloading model repository snapshots to local directories.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/resolvedmodelconfiguration)*