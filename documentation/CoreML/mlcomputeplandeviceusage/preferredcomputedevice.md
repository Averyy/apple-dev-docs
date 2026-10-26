# preferredComputeDevice

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The compute device that the framework prefers to execute the layer/operation.

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
@property (nonatomic, strong, readonly) id<MLComputeDeviceProtocol> preferredComputeDevice;
```

## See Also

### Getting the compute device
- [supportedComputeDevices](./supportedcomputedevices.md)
  The compute devices that can execute the layer/operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeplandeviceusage/preferredcomputedevice)*