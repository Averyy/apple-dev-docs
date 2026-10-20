# type

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The type you specify when creating the device.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var type: MLCDeviceType { get }
```

```objc
@property (nonatomic, readonly) MLCDeviceType type;
```

## See Also

### Inspecting Devices
- [var actualDeviceType: MLCDeviceType](./actualdevicetype.md)
  The active device.
- [var gpuDevices: [any MTLDevice]](./gpudevices.md)
  An array that contains the specific Metal devices you use to execute neural networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdevice/type)*