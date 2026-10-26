# supportedComputeDevices

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The compute devices that can execute the layer/operation.

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
@property (nonatomic, copy, readonly) NSArray<id<MLComputeDeviceProtocol>> * supportedComputeDevices;
```

## See Also

### Getting the compute device
- [preferredComputeDevice](./preferredcomputedevice.md)
  The compute device that the framework prefers to execute the layer/operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeplandeviceusage/supportedcomputedevices)*