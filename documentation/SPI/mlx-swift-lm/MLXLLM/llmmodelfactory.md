---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmmodelfactory"
framework: "mlx-swift-lm/MLXLLM"
---

# LLMModelFactory

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

Factory for creating new LLMs.

## Declaration

```swift
final class LLMModelFactory
```

#### Overview

Callers can use the `shared` instance or create a new instance if custom configuration is required.

```swift
let modelContainer = try await LLMModelFactory.shared.loadContainer(
    configuration: LLMRegistry.llama3_8B_4bit)
```

## Topics

### Initializers
- [init(typeRegistry: ModelTypeRegistry<LanguageModel>, modelRegistry: AbstractModelRegistry, conventionsRegistry: ChatConventionsRegistry)](./llmmodelfactory/init%28typeregistry,modelregistry,conventionsregistry%29.md)
### Instance Properties
- [let conventionsRegistry: ChatConventionsRegistry](./llmmodelfactory/conventionsregistry.md)
  resolvers for chat conventions that are keyed on model id rather than declared by the model itself, e.g. DeepSeek-R1
- [let modelRegistry: AbstractModelRegistry](./llmmodelfactory/modelregistry.md)
  registry of model id to configuration, e.g. `mlx-community/Llama-3.2-3B-Instruct-4bit`
- [let typeRegistry: ModelTypeRegistry<LanguageModel>](./llmmodelfactory/typeregistry.md)
  registry of model type, e.g. configuration value `llama` -> configuration and init methods
### Instance Methods
- [func convert(configuration: ResolvedModelConfiguration, to: URL, options: ModelConversionOptions, progressHandler: @Sendable (ModelConversionProgress) -> Void) async throws -> ModelConversionResult](./llmmodelfactory/convert%28configuration,to,options,progresshandler%29.md)
  Quantize and save a resolved local safetensors-backed LLM.
- [func convert(from: any Downloader, configuration: ModelConfiguration, to: URL, bits: Int?, groupSize: Int?, mode: QuantizationMode, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> ModelConversionResult](./llmmodelfactory/convert%28from,configuration,to,bits,groupsize,mode,uselatest,progresshandler%29.md)
  Download, quantize, and save a safetensors-backed LLM.
- [func convert(from: any Downloader, configuration: ModelConfiguration, to: URL, options: ModelConversionOptions, useLatest: Bool, downloadProgressHandler: @Sendable (Progress) -> Void, progressHandler: @Sendable (ModelConversionProgress) -> Void) async throws -> ModelConversionResult](./llmmodelfactory/convert%28from,configuration,to,options,uselatest,downloadprogresshandler,progresshandler%29.md)
  Download, quantize, and save a safetensors-backed LLM.
- [func convert(from: URL, tokenizerDirectory: URL?, to: URL, options: ModelConversionOptions, progressHandler: @Sendable (ModelConversionProgress) -> Void) async throws -> ModelConversionResult](./llmmodelfactory/convert%28from,tokenizerdirectory,to,options,progresshandler%29.md)
  Quantize and save a local safetensors-backed LLM.
- [func loraMetadata(configurationData: Data) async throws -> LoRAModelMetadata?](./llmmodelfactory/lorametadata%28configurationdata%29.md)
  Returns the model’s LoRA metadata from its configuration without loading weights.
### Type Aliases
- [LLMModelFactory.ContainerType](./llmmodelfactory/containertype.md)
- [LLMModelFactory.ContextType](./llmmodelfactory/contexttype.md)
### Type Properties
- [static let shared: LLMModelFactory](./llmmodelfactory/shared.md)
  Shared instance with default behavior.
### Default Implementations
- [GenericModelFactory Implementations](./llmmodelfactory/genericmodelfactory-implementations.md)

## Relationships

### Conforms To
- MLXLMCommon.GenericModelFactory
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmmodelfactory)*