---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/loratrain/parameters"
framework: "mlx-swift-lm/MLXLLM"
---

# LoRATrain.Parameters

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: struct  
**Role**: Structure

LoRA training parameters

## Declaration

```swift
struct Parameters
```

## Topics

### Initializers
- [init(batchSize: Int, iterations: Int, stepsPerReport: Int, stepsPerEval: Int, validationBatches: Int, saveEvery: Int, adapterURL: URL?, completedIterations: Int)](./parameters/init%28batchsize,iterations,stepsperreport,stepspereval,validationbatches,saveevery,adapterurl,completediterations%29.md)
### Instance Properties
- [var adapterURL: URL?](./parameters/adapterurl.md)
  save path for the adapter `.safetensors`
- [var batchSize: Int](./parameters/batchsize.md)
  number of prompts to evaluate per iteration
- [var completedIterations: Int](./parameters/completediterations.md)
  number of iterations already completed when resuming from saved adapter weights
- [var iterations: Int](./parameters/iterations.md)
  number of iterations to train for
- [var saveEvery: Int](./parameters/saveevery.md)
  save the model every N iterations
- [var stepsPerEval: Int](./parameters/stepspereval.md)
  number of steps between validations
- [var stepsPerReport: Int](./parameters/stepsperreport.md)
  number of training steps between loss reporting
- [var validationBatches: Int](./parameters/validationbatches.md)
  number of validations batches, `0` uses the entire validation set

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/loratrain/parameters)*