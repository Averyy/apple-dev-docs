---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadweights(modeldirectory:model:quantization:perlayerquantization:weightfileselection:excludedcomponents:componentloading:)-fqoy"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loadWeights(modelDirectory:model:quantization:perLayerQuantization:weightFileSelection:excludedComponents:componentLoading:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Async variant of [`loadWeights(modelDirectory:model:quantization:perLayerQuantization:weightFileSelection:excludedComponents:componentLoading:)`](./loadweights%28modeldirectory,model,quantization,perlayerquantization,weightfileselection,excludedcomponents,componentloading%29-858j8.md).

## Declaration

```swift
func loadWeights(modelDirectory: URL, model: BaseLanguageModel, quantization: BaseConfiguration.Quantization? = nil, perLayerQuantization: BaseConfiguration.PerLayerQuantization? = nil, weightFileSelection: WeightFileSelection = .automatic, excludedComponents: Set<ModelComponent> = [], componentLoading: ComponentLoading = .onFirstUse) async throws
```

## Mentions

- [Porting Models](./porting.md)

#### Discussion

Loading blocks its thread on file I/O and fans out with `DispatchQueue.concurrentPerform`. Swift concurrency’s cooperative threads must never block, so this overload runs the load on a global queue and suspends the caller instead. Async callers resolve to this overload; the synchronous one remains for synchronous code such as model conversion.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadweights(modeldirectory:model:quantization:perlayerquantization:weightfileselection:excludedcomponents:componentloading:)-fqoy)*