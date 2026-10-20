# gpuDevices

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

An array that contains the specific Metal devices you use to execute neural networks.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var gpuDevices: [any MTLDevice] { get }
```

```objc
@property (nonatomic, readonly) NSArray<id<MTLDevice>> * gpuDevices;
```

## See Also

### Inspecting Devices
- [var type: MLCDeviceType](./type.md)
  The type you specify when creating the device.
- [var actualDeviceType: MLCDeviceType](./actualdevicetype.md)
  The active device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdevice/gpudevices)*