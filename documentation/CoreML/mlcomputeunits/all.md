# MLComputeUnits.all

**Framework**: Core ML  
**Kind**: case  
**Role**: Case

The option you choose to allow the model to use all compute units available, including the neural engine.

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
case all
```

```c
MLComputeUnitsAll
```

## See Also

### Processing Unit Configurations
- [MLComputeUnits.cpuOnly](./cpuonly.md)
  The option you choose to limit the model to only use the CPU.
- [MLComputeUnits.cpuAndGPU](./cpuandgpu.md)
  The option you choose to allow the model to use both the CPU and GPU, but not the neural engine.
- [MLComputeUnits.cpuAndNeuralEngine](./cpuandneuralengine.md)
  The option you choose to allow the model to use both the CPU and neural engine, but not the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeunits/all)*