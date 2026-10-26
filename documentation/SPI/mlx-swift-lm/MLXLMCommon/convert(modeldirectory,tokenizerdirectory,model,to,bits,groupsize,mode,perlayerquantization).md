---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/convert(modeldirectory:tokenizerdirectory:model:to:bits:groupsize:mode:perlayerquantization:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# convert(modelDirectory:tokenizerDirectory:model:to:bits:groupSize:mode:perLayerQuantization:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Quantize and save an already-instantiated model from a compatible safetensors directory.

## Declaration

```swift
func convert(modelDirectory: URL, tokenizerDirectory: URL? = nil, model: BaseLanguageModel, to outputDirectory: URL, bits: Int? = nil, groupSize: Int? = nil, mode: QuantizationMode = .affine, perLayerQuantization: BaseConfiguration.PerLayerQuantization? = nil) throws -> ModelConversionResult
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/convert(modeldirectory:tokenizerdirectory:model:to:bits:groupsize:mode:perlayerquantization:))*