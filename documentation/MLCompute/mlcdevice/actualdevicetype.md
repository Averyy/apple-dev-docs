# actualDeviceType

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The active device.

**Availability**:
- iOS 15.0+ - Deprecated in 17.4
- iPadOS 15.0+ - Deprecated in 17.4
- Mac Catalyst 15.0+ - Deprecated in 17.4
- macOS 12.0+ - Deprecated in 14.3
- tvOS 15.0+ - Deprecated in 17.4

## Declaration

```swift
var actualDeviceType: MLCDeviceType { get }
```

```objc
@property (nonatomic, readonly) MLCDeviceType actualDeviceType;
```

## See Also

### Inspecting Devices
- [var type: MLCDeviceType](./type.md)
  The type you specify when creating the device.
- [var gpuDevices: [any MTLDevice]](./gpudevices.md)
  An array that contains the specific Metal devices you use to execute neural networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdevice/actualdevicetype)*