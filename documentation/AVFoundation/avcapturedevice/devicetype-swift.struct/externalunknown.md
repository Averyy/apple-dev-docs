# externalUnknown

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

An unknown external device type.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0 (renamed: AVCaptureDevice.DeviceType.external)

> **Deprecated**: Use [`external`](./external.md) instead.

## Declaration

```swift
static let externalUnknown: AVCaptureDevice.DeviceType
```

```c
extern AVCaptureDeviceType const AVCaptureDeviceTypeExternalUnknown;
```

#### Discussion

In macOS, use this type to specify external devices, such as an iPhone camera.

> ❗ **Important**:  In [Mac Catalyst](../../../UIKit/mac-catalyst.md) apps, use [`builtInWideAngleCamera`](./builtinwideanglecamera.md) instead.

## See Also

### External devices
- [static let external: AVCaptureDevice.DeviceType](./external.md)
  An external device type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/externalunknown)*