# MLAllComputeDevices

**Framework**: Core ML  
**Kind**: func  
**Role**: Function

Returns an array that contains all of the compute devices that are accessible.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```c
extern NSArray<id<MLComputeDeviceProtocol>> *MLAllComputeDevices();
```

## See Also

### Compute devices
- [class MLCPUComputeDevice](./mlcpucomputedevice.md)
  An object that represents a CPU compute device.
- [class MLGPUComputeDevice](./mlgpucomputedevice.md)
  An object that represents a GPU compute device.
- [class MLNeuralEngineComputeDevice](./mlneuralenginecomputedevice.md)
  An object that represents a Neural Engine compute device.
- [protocol MLComputeDeviceProtocol](./mlcomputedeviceprotocol.md)
  An interface that represents a compute device type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlallcomputedevices)*