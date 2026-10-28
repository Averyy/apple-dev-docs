---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/loratrain/train(model:train:validate:optimizer:loss:tokenizer:parameters:progress:)"
framework: "mlx-swift-lm/MLXLLM"
---

# train(model:train:validate:optimizer:loss:tokenizer:parameters:progress:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Type Method

Train (or continue training) LoRA weights.

## Declaration

```swift
static func train(model: Module, train: [String], validate: [String], optimizer: Optimizer, loss: @escaping LoraLossFunction = loss, tokenizer: Tokenizer, parameters: Parameters, progress: (Progress) -> ProgressDisposition) throws
```

## Discussion

> **Throws**: [`LoRATrainError.sampleTooShort(dataset:index:tokenCount:)`](../loratrainerror/sampletooshort%28dataset,index,tokencount%29.md) if a training or validation sample encodes to fewer than 2 tokens. Checked before training starts.

The model is temporarily placed in training mode and its previous mode is restored before this function returns.

## Parameters

- `model`: Model to train
- `train`: Training dataset
- `validate`: Validate dataset
- `optimizer`: Optimizer used in training
- `loss`: Loss function
- `tokenizer`: Tokenizer
- `parameters`: Training parameters
- `progress`: Progress callback


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/loratrain/train(model:train:validate:optimizer:loss:tokenizer:parameters:progress:))*