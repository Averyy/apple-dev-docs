---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/loratrain"
framework: "mlx-swift-lm/MLXLLM"
---

# LoRATrain

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: enum  
**Role**: Enumeration

Collection of functions for adding LoRA adapters to an LLM model, training, fusing and saving/loading weights.

## Declaration

```swift
enum LoRATrain
```

#### Overview

The typical flow for training is:

```swift
// load the base model and tokenizer
let (model, tokenizer) = try await LLM.load(configuration: ModelConfiguration.mistral7B4bit)

// add LoRALinear adapter layers
LoRATrain.convert(model: model, layers: Array(model.loraLinearLayers().suffix(4)))

// optionally load LoRA weights
try LoRATrain.loadLoRAWeights(model: model, url: ...)

// load the train/validation data
let train = try loadLoRAData(directory: data, name: "train")
let valid = try loadLoRAData(directory: data, name: "valid")

// train
let optimizer = Adam(learningRate: 1e-5)
try await LoRATrain.train(
    model: model, train: train, validate: valid, optimizer: optimizer, tokenizer: tokenizer,
    parameters: LoRATrain.Parameters()
) { progress in
    print(progress)
    return .more
}
```

At this point the model will be trained and you could do one of the following:

- [`saveLoRAWeights(model:url:)`](./loratrain/saveloraweights%28model,url%29.md): write the LoRA weights to a file
- fuse the LoRA weights and convert back into the original model architecture using the LoRA adapter APIs in `MLXLMCommon`
- [`evaluate(model:dataset:loss:tokenizer:batchSize:batchCount:)`](./loratrain/evaluate%28model,dataset,loss,tokenizer,batchsize,batchcount%29.md)– compute the test loss againts a test dataset
- use the in memory model as a normal `LLMModel` and evaluate a prompt

## Topics

### Structures
- [LoRATrain.Parameters](./loratrain/parameters.md)
  LoRA training parameters
### Type Aliases
- [LoRATrain.LoraLossFunction](./loratrain/loralossfunction.md)
### Type Methods
- [static func evaluate(model: Module, dataset: [String], loss: LoraLossFunction, tokenizer: Tokenizer, batchSize: Int, batchCount: Int) -> Float](./loratrain/evaluate%28model,dataset,loss,tokenizer,batchsize,batchcount%29.md)
  Evaluate the model and dataset and return the loss over the entire dataset.
- [static func loadLoRAWeights(model: Module, url: URL) throws](./loratrain/loadloraweights%28model,url%29.md)
  Load saved LoRA weights into a model that already has matching adapter layers applied.
- [static func loss(model: Module, inputs: MLXArray, targets: MLXArray, lengths: MLXArray) -> (MLXArray, MLXArray)](./loratrain/loss%28model,inputs,targets,lengths%29.md)
- [static func saveLoRAWeights(model: Module, url: URL) throws](./loratrain/saveloraweights%28model,url%29.md)
  Given a model with LoRA adaptors applied, write adapter weights to a `.safetensors` file.
- [static func train(model: Module, train: [String], validate: [String], optimizer: Optimizer, loss: LoraLossFunction, tokenizer: Tokenizer, parameters: Parameters, progress: (Progress) -> ProgressDisposition) throws](./loratrain/train%28model,train,validate,optimizer,loss,tokenizer,parameters,progress%29.md)
  Train (or continue training) LoRA weights.
### Enumerations
- [LoRATrain.Progress](./loratrain/progress.md)
- [LoRATrain.ProgressDisposition](./loratrain/progressdisposition.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/loratrain)*