---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator/init(prompt:model:cache:parameters:components:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(prompt:model:cache:parameters:components:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize a `TokenIterator` with the given tokens. Note: this has been replaced with [`init(input:model:cache:state:parameters:components:)`](./init%28input,model,cache,state,parameters,components%29.md).

> **Deprecated**: please use init(input:model:cache:parameters:)

## Declaration

```swift
init(prompt: MLXArray, model: any LanguageModel, cache: [KVCache]? = nil, parameters: GenerateParameters, components: GenerationComponents = .init()) throws
```

## Parameters

- `prompt`: The prompt tokens
- `model`: The [`LanguageModel`](../languagemodel.md)
- `cache`: Optional [`KVCache`](../kvcache.md)
- `parameters`: The generation parameters
- `components`: Optional behavioral components, e.g. a custom [`LogitProcessor`](../logitprocessor.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator/init(prompt:model:cache:parameters:components:))*