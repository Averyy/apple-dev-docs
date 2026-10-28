# deviceUsage(for:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Returns the anticipated compute devices that would be used for executing a NeuralNetwork layer.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
func deviceUsage(for layer: MLModelStructure.NeuralNetwork.Layer) -> MLComputePlan.DeviceUsage?
```

**Other overloads**:

```swift
func deviceUsage(for operation: MLModelStructure.Program.Operation) -> MLComputePlan.DeviceUsage?
```

## Return Value

The anticipated compute devices that would be used for evaluating the layer or `nil` if the usage couldn’t be determined.

## Parameters

- `layer`: A NeuralNetwork layer

## See Also

### Getting the device usage
- [func deviceUsage(for:)](./deviceusage%28for%29.md)
  Returns the anticipated compute devices that would be used for executing a NeuralNetwork layer.
- [func deviceUsage(for: MLModelStructure.Program.Operation) -> MLComputePlan.DeviceUsage?](./deviceusage%28for%29-7cdlm.md)
  Returns the anticipated compute devices that would be used for executing a MLProgram operation.
- [MLComputePlan.DeviceUsage](./deviceusage.md)
  The anticipated compute devices that would be used for executing a layer/operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeplan-1w21n/deviceusage(for:)-9em1q)*