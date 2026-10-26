# MLComputePlanDeviceUsage

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

The anticipated compute devices to use for executing a layer or operation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```objc
@interface MLComputePlanDeviceUsage : NSObject
```

## Topics

### Getting the compute device
- [preferredComputeDevice](./mlcomputeplandeviceusage/preferredcomputedevice.md)
  The compute device that the framework prefers to execute the layer/operation.
- [supportedComputeDevices](./mlcomputeplandeviceusage/supportedcomputedevices.md)
  The compute devices that can execute the layer/operation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Compute plan
- [MLComputePlan](./mlcomputeplan-85vdw.md)
  A class describing the plan for executing a model.
- [MLComputePlanCost](./mlcomputeplancost.md)
  A class that represents the estimated cost of executing a layer or operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeplandeviceusage)*