# MLComputeDevice

**Framework**: Core ML  
**Kind**: enum

Compute devices for framework operations.

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
enum MLComputeDevice
```

## Topics

### Device Types
- [case cpu(MLCPUComputeDevice)](mlcomputedevice/cpu(_:).md)
  A device that represents a CPU compute device.
- [case gpu(MLGPUComputeDevice)](mlcomputedevice/gpu(_:).md)
  A device that represents a GPU compute device.
- [case neuralEngine(MLNeuralEngineComputeDevice)](mlcomputedevice/neuralengine(_:).md)
  A device that represents a Neural Engine compute device.
### Getting All Devices
- [static var allComputeDevices: [MLComputeDevice]](mlcomputedevice/allcomputedevices.md)
  Returns an array that contains all of the compute devices that are accessible.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MLCPUComputeDevice](mlcpucomputedevice.md)
  An object that represents a CPU compute device.
- [class MLGPUComputeDevice](mlgpucomputedevice.md)
  An object that represents a GPU compute device.
- [class MLNeuralEngineComputeDevice](mlneuralenginecomputedevice.md)
  An object that represents a Neural Engine compute device.
- [protocol MLComputeDeviceProtocol](mlcomputedeviceprotocol.md)
  An interface that represents a compute device type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputedevice)*