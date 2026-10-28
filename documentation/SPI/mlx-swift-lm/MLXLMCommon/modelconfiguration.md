---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelConfiguration

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Configuration for a given model:  at least an org/name identifier or a directory with the model files.

## Declaration

```swift
struct ModelConfiguration
```

## Mentions

- [Model Compatibility](./model-compatibility.md)

## Overview

Optionally callers can provide some default values and overrides for:

- a default prompt
- EOS tokens / strings
- tool calling formats

Some of these are specific to LLMs and VLMs – embedding models will ignore those properties.

See e.g. `MLXLM.ModelRegistry` for an example of use.

## Topics

### Initializers
- [init(directory: URL, tokenizerSource: TokenizerSource?, defaultPrompt: String, extraEOSTokens: Set<String>, stopStrings: Set<String>?, eosTokenIds: Set<Int>, toolCallFormat: ToolCallFormat?, reasoningConfig: ReasoningConfig?, messageGenerator: (any MessageGenerator)?)](./modelconfiguration/init%28directory,tokenizersource,defaultprompt,extraeostokens,stopstrings,eostokenids,toolcallformat,reasoningconfig,messagegenerator%29.md)
- [init(id: String, revision: String, tokenizerSource: TokenizerSource?, defaultPrompt: String, extraEOSTokens: Set<String>, stopStrings: Set<String>?, eosTokenIds: Set<Int>, toolCallFormat: ToolCallFormat?, reasoningConfig: ReasoningConfig?, messageGenerator: (any MessageGenerator)?)](./modelconfiguration/init%28id,revision,tokenizersource,defaultprompt,extraeostokens,stopstrings,eostokenids,toolcallformat,reasoningconfig,messagegenerator%29.md)
### Instance Properties
- [var defaultPrompt: String](./modelconfiguration/defaultprompt.md)
  A reasonable default prompt for the model
- [var effectiveStopStrings: Set<String>](./modelconfiguration/effectivestopstrings.md)
  Text sequences to use for decoded stop-string matching.
- [var eosTokenIds: Set<Int>](./modelconfiguration/eostokenids.md)
  EOS token IDs loaded from config.json/generation_config.json
- [var excludedComponents: Set<ModelComponent>](./modelconfiguration/excludedcomponents.md)
  Components to never load, such as [`vision`](./modelcomponent/vision.md) for text-only use.
- [var extraEOSTokens: Set<String>](./modelconfiguration/extraeostokens.md)
  Additional tokens to use for end of string (specified as strings, converted to IDs at runtime)
- [var id: Identifier](./modelconfiguration/id.md)
  The model’s identifier (ID or Directory).
- [var messageGenerator: (any MessageGenerator)?](./modelconfiguration/messagegenerator.md)
  Overrides the [`MessageGenerator`](./messagegenerator.md) the model would otherwise supply.
- [var name: String](./modelconfiguration/name.md)
  A display-friendly name for the model.
- [var reasoningConfig: ReasoningConfig?](./modelconfiguration/reasoningconfig.md)
  Reasoning (chain-of-thought) protocol for this model (nil = non-reasoning model)
- [var stopStrings: Set<String>?](./modelconfiguration/stopstrings.md)
  Text sequences that stop decoded generation when encountered.
- [let tokenizerSource: TokenizerSource?](./modelconfiguration/tokenizersource.md)
  Where to load the tokenizer from when it differs from the model directory.
- [var toolCallFormat: ToolCallFormat?](./modelconfiguration/toolcallformat.md)
  Tool call format for this model (nil = default JSON format)
- [var weightFileSelection: WeightFileSelection](./modelconfiguration/weightfileselection.md)
  How to choose which safetensors files in the model directory hold the model’s weights.
### Instance Methods
- [func resolved(modelDirectory: URL, tokenizerDirectory: URL) -> ResolvedModelConfiguration](./modelconfiguration/resolved%28modeldirectory,tokenizerdirectory%29.md)
  Maps this configuration’s behavioral properties into a [`ResolvedModelConfiguration`](./resolvedmodelconfiguration.md) with the given directories.
### Enumerations
- [ModelConfiguration.DirectoryError](./modelconfiguration/directoryerror.md)
- [ModelConfiguration.Identifier](./modelconfiguration/identifier.md)
  The backing storage for the model’s location.
### Default Implementations
- [Equatable Implementations](./modelconfiguration/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration)*