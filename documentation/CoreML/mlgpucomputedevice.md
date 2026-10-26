# MLGPUComputeDevice

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

An object that represents a GPU compute device.

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
class MLGPUComputeDevice
```

```objc
@interface MLGPUComputeDevice : NSObject
```

## Topics

### Getting the metal device
- [var metalDevice: (any MTLDevice)!](./mlgpucomputedevice/metaldevice.md)
  The device that represents the underlying metal device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MLComputeDeviceProtocol](./mlcomputedeviceprotocol.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Compute devices
- [enum MLComputeDevice](./mlcomputedevice.md)
  Compute devices for framework operations.
- [class MLCPUComputeDevice](./mlcpucomputedevice.md)
  An object that represents a CPU compute device.
- [class MLNeuralEngineComputeDevice](./mlneuralenginecomputedevice.md)
  An object that represents a Neural Engine compute device.
- [protocol MLComputeDeviceProtocol](./mlcomputedeviceprotocol.md)
  An interface that represents a compute device type.
- [MLAllComputeDevices](./mlallcomputedevices.md)
  Returns an array that contains all of the compute devices that are accessible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlgpucomputedevice)*