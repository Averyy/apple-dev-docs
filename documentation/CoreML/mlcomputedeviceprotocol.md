# MLComputeDeviceProtocol

**Framework**: Core ML  
**Kind**: protocol

An interface that represents a compute device type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
protocol MLComputeDeviceProtocol : NSObjectProtocol
```

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [MLCPUComputeDevice](mlcpucomputedevice.md)
- [MLGPUComputeDevice](mlgpucomputedevice.md)
- [MLNeuralEngineComputeDevice](mlneuralenginecomputedevice.md)

## See Also

- [enum MLComputeDevice](mlcomputedevice.md)
  Compute devices for framework operations.
- [class MLCPUComputeDevice](mlcpucomputedevice.md)
  An object that represents a CPU compute device.
- [class MLGPUComputeDevice](mlgpucomputedevice.md)
  An object that represents a GPU compute device.
- [class MLNeuralEngineComputeDevice](mlneuralenginecomputedevice.md)
  An object that represents a Neural Engine compute device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputedeviceprotocol)*