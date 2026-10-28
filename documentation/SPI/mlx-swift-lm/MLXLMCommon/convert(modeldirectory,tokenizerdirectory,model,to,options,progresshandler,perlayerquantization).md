---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/convert(modeldirectory:tokenizerdirectory:model:to:options:progresshandler:perlayerquantization:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# convert(modelDirectory:tokenizerDirectory:model:to:options:progressHandler:perLayerQuantization:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Quantize and save an already-instantiated model from a compatible safetensors directory.

## Declaration

```swift
func convert(modelDirectory: URL, tokenizerDirectory: URL? = nil, model: BaseLanguageModel, to outputDirectory: URL, options: ModelConversionOptions = .init(), progressHandler: @Sendable (ModelConversionProgress) -> Void = { _ in }, perLayerQuantization: BaseConfiguration.PerLayerQuantization? = nil) throws -> ModelConversionResult
```

## Discussion

The function loads safetensors weights, runs the model’s sanitizer through [`loadWeights(modelDirectory:model:quantization:perLayerQuantization:weightFileSelection:excludedComponents:componentLoading:)`](./loadweights%28modeldirectory,model,quantization,perlayerquantization,weightfileselection,excludedcomponents,componentloading%29-858j8.md), applies quantization, writes safetensors shards and an index, copies tokenizer/config sidecar files, and updates `config.json` with the requested quantization block.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/convert(modeldirectory:tokenizerdirectory:model:to:options:progresshandler:perlayerquantization:))*