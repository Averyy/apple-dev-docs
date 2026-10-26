---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/loratrain/evaluate(model:dataset:loss:tokenizer:batchsize:batchcount:)"
framework: "mlx-swift-lm/MLXLLM"
---

# evaluate(model:dataset:loss:tokenizer:batchSize:batchCount:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Type Method

Evaluate the model and dataset and return the loss over the entire dataset.

## Declaration

```swift
static func evaluate(model: Module, dataset: [String], loss: LoraLossFunction = loss, tokenizer: Tokenizer, batchSize: Int, batchCount: Int) -> Float
```

#### Return Value

The loss over the enumerate data

#### Discussion

The model is temporarily placed in evaluation mode and its previous mode is restored before this function returns.

##### See Also

- [`loadLoRAData(directory:name:)`](../loadloradata%28directory,name%29.md)

## Parameters

- `model`: The model to evaluate
- `dataset`: The dataset
- `loss`: Loss function
- `tokenizer`: Tokenizer
- `batchSize`: Number of items from the dataset to evaluate at once
- `batchCount`: Number of batch elements to evaluate, 0 for all


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/loratrain/evaluate(model:dataset:loss:tokenizer:batchsize:batchcount:))*