# MLComputeUnits

**Framework**: Core ML  
**Kind**: enum

The set of processing-unit configurations the model can use to make predictions.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum MLComputeUnits
```

#### Overview

Use this enumeration to set or inspect the processing units you allow a model to use when it makes a prediction.

Use `all` to allow the OS to select the best processing unit to use (including the neural engine, if available).

Use [`MLComputeUnits.cpuOnly`](mlcomputeunits/cpuonly.md) to restrict the model to the CPU, if your app might run in the background or runs other GPU intensive tasks.

## Topics

### Processing Unit Configurations
- [MLComputeUnits.all](mlcomputeunits/all.md)
  The option you choose to allow the model to use all compute units available, including the neural engine.
- [MLComputeUnits.cpuOnly](mlcomputeunits/cpuonly.md)
  The option you choose to limit the model to only use the CPU.
- [MLComputeUnits.cpuAndGPU](mlcomputeunits/cpuandgpu.md)
  The option you choose to allow the model to use both the CPU and GPU, but not the neural engine.
- [MLComputeUnits.cpuAndNeuralEngine](mlcomputeunits/cpuandneuralengine.md)
  The option you choose to allow the model to use both the CPU and neural engine, but not the GPU.
### Initializers
- [init?(rawValue: Int)](mlcomputeunits/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var computeUnits: MLComputeUnits](mlmodelconfiguration/computeunits.md)
  The processing unit or units the model uses to make predictions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeunits)*