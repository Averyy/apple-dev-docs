# builtInLiDARDepthCamera

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A device that consists of two cameras, one LiDAR and one YUV.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- tvOS 17.0+

## Declaration

```swift
static let builtInLiDARDepthCamera: AVCaptureDevice.DeviceType
```

```c
extern AVCaptureDeviceType const AVCaptureDeviceTypeBuiltInLiDARDepthCamera;
```

## Discussion

The LiDAR camera provides high-quality, high-accuracy depth information by measuring the round trip of an artificial light signal that a laser emits. The device synchronizes and perspective-corrects this data to frames that the YUV camera produces. While the resolution of the depth data and YUV frames may differ, their field of view and aspect ratio always match.

> **Note**:  You can only discover devices of this type by using an [`AVCaptureDevice.DiscoverySession`](../discoverysession.md) or by calling the [`default(_:for:position:)`](../default%28_,for,position%29.md) method.

## See Also

### Depth sensing
- [static let builtInTrueDepthCamera: AVCaptureDevice.DeviceType](./builtintruedepthcamera.md)
  A device that consists of two cameras, one Infrared and one YUV.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtinlidardepthcamera)*