---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadweights(modeldirectory:model:quantization:perlayerquantization:weightfileselection:excludedcomponents:componentloading:)-858j8"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loadWeights(modelDirectory:model:quantization:perLayerQuantization:weightFileSelection:excludedComponents:componentLoading:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Load model weights.

## Declaration

```swift
func loadWeights(modelDirectory: URL, model: BaseLanguageModel, quantization: BaseConfiguration.Quantization? = nil, perLayerQuantization: BaseConfiguration.PerLayerQuantization? = nil, weightFileSelection: WeightFileSelection = .automatic, excludedComponents: Set<ModelComponent> = [], componentLoading: ComponentLoading = .onFirstUse) throws
```

#### Discussion

This is typically called via [`load(from:using:configuration:useLatest:progressHandler:)`](./genericmodelfactory/load%28from,using,configuration,uselatest,progresshandler%29.md). This function loads model weight `safetensor` files in the given `modelDirectory`, calls [`prepareCheckpoint(_:)`](./baselanguagemodel/preparecheckpoint%28_%29.md) to allow per-model preprocessing, applies optional quantization, and updates the model with the weights. Derived inference-only state is prepared after the checkpoint update and before the model is evaluated and returned to callers.

The weight files are chosen from `model.safetensors.index.json` when it names files that exist, and otherwise by the conventional `model*.safetensors` names. A model can name extra files it needs by conforming to [`AdditionalWeightFilesProviding`](./additionalweightfilesproviding.md), and a caller can override the choice with [`weightFileSelection`](./modelconfiguration/weightfileselection.md).

The model loads without the `excludedComponents` it supports, see [`ModelComponentsProviding`](./modelcomponentsproviding.md). Its on-demand components load the first time an input needs them, unless `componentLoading` is [`ComponentLoading.immediate`](./componentloading/immediate.md). Tensors of components that do not load now and of the model’s [`excludedCheckpointNamespaces`](./baselanguagemodel/excludedcheckpointnamespaces.md) are not read.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadweights(modeldirectory:model:quantization:perlayerquantization:weightfileselection:excludedcomponents:componentloading:)-858j8)*