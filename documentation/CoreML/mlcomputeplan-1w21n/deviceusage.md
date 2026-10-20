# MLComputePlan.DeviceUsage

**Framework**: Core ML  
**Kind**: struct  
**Role**: Structure

The anticipated compute devices that would be used for executing a layer/operation.

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
struct DeviceUsage
```

## Topics

### Getting the device usage
- [let preferred: MLComputeDevice](./deviceusage/preferred.md)
  The compute device that the framework prefers to execute the layer/operation.
- [let supported: [MLComputeDevice]](./deviceusage/supported.md)
  The compute devices that can execute the layer/operation.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the device usage
- [func deviceUsage(for:)](./deviceusage%28for%29.md)
  Returns the anticipated compute devices that would be used for executing a NeuralNetwork layer.
- [func deviceUsage(for: MLModelStructure.NeuralNetwork.Layer) -> MLComputePlan.DeviceUsage?](./deviceusage%28for%29-9em1q.md)
  Returns the anticipated compute devices that would be used for executing a NeuralNetwork layer.
- [func deviceUsage(for: MLModelStructure.Program.Operation) -> MLComputePlan.DeviceUsage?](./deviceusage%28for%29-7cdlm.md)
  Returns the anticipated compute devices that would be used for executing a MLProgram operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeplan-1w21n/deviceusage)*