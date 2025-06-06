# gpuDevices

**Framework**: ML Compute  
**Kind**: property

An array that contains the specific Metal devices you use to execute neural networks.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var gpuDevices: [any MTLDevice] { get }
```

## See Also

- [var type: MLCDeviceType](mlcdevice/type.md)
  The type you specify when creating the device.
- [var actualDeviceType: MLCDeviceType](mlcdevice/actualdevicetype.md)
  The active device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdevice/gpudevices)*