# computeDeviceUsageForMLProgramOperation:

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Returns The anticipated compute devices that would be used for executing an ML Program operation.

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
- (MLComputePlanDeviceUsage *) computeDeviceUsageForMLProgramOperation:(MLModelStructureProgramOperation *) operation;
```

#### Return Value

The anticipated compute devices that would be used for executing the operation or `nil`if the usage couldn’t be determined.

## Parameters

- `operation`: An ML Program operation.

## See Also

### Getting the device usage
- [- computeDeviceUsageForNeuralNetworkLayer:](./computedeviceusageforneuralnetworklayer_.md)
  Returns the anticipated compute devices that would be used for executing a NeuralNetwork layer.
- [MLComputePlanDeviceUsage](../mlcomputeplandeviceusage.md)
  The anticipated compute devices to use for executing a layer or operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeplan-85vdw/computedeviceusageformlprogramoperation:)*