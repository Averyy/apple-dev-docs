---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadparoquantmodel(from:typeregistry:tokenizerloader:toolcallformat:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loadParoQuantModel(from:typeRegistry:tokenizerLoader:toolCallFormat:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Load a ParoQuant model from a local directory, returning a [`ModelContainer`](./modelcontainer.md).

## Declaration

```swift
func loadParoQuantModel<T>(from directory: URL, typeRegistry: ModelTypeRegistry<T>, tokenizerLoader: any TokenizerLoader, toolCallFormat: ToolCallFormat? = nil) async throws -> ModelContainer where T : LanguageModel
```

## Return Value

A [`ModelContainer`](./modelcontainer.md) ready for inference.

## Discussion

Handles AutoAWQ weight conversion, rotation layer patching, and IO layer quantization. Rotation parameters (theta, pairs, channel_scales) are kept in the model and applied to activations at runtime via Metal kernel.

## Parameters

- `directory`: Local path to the model checkpoint directory.
- `typeRegistry`: Registry used to create the underlying model architecture.
- `tokenizerLoader`: Loader for tokenizer.
- `toolCallFormat`: Optional tool-call format for the model configuration.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadparoquantmodel(from:typeregistry:tokenizerloader:toolcallformat:))*