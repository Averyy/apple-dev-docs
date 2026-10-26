---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/loratrainerror"
framework: "mlx-swift-lm/MLXLLM"
---

# LoRATrainError

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: enum  
**Role**: Enumeration

Errors thrown by [`train(model:train:validate:optimizer:loss:tokenizer:parameters:progress:)`](./loratrain/train%28model,train,validate,optimizer,loss,tokenizer,parameters,progress%29.md).

## Declaration

```swift
enum LoRATrainError
```

## Topics

### Enumeration Cases
- [case sampleTooShort(dataset: Dataset, index: Int, tokenCount: Int)](./loratrainerror/sampletooshort%28dataset,index,tokencount%29.md)
  A sample encodes to fewer than two tokens, so it has nothing to predict.
### Instance Properties
- [var errorDescription: String?](./loratrainerror/errordescription.md)
### Enumerations
- [LoRATrainError.Dataset](./loratrainerror/dataset.md)
  Which dataset a sample came from.
### Default Implementations
- [Equatable Implementations](./loratrainerror/equatable-implementations.md)
- [Error Implementations](./loratrainerror/error-implementations.md)
- [LocalizedError Implementations](./loratrainerror/localizederror-implementations.md)

## Relationships

### Conforms To
- Foundation.LocalizedError
- Swift.Equatable
- Swift.Error
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/loratrainerror)*