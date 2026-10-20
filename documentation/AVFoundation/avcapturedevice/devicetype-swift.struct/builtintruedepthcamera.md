# builtInTrueDepthCamera

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A device that consists of two cameras, one Infrared and one YUV.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
static let builtInTrueDepthCamera: AVCaptureDevice.DeviceType
```

```c
extern AVCaptureDeviceType const AVCaptureDeviceTypeBuiltInTrueDepthCamera;
```

## Mentions

- [Capturing photos with depth](../../capturing-photos-with-depth.md)

#### Discussion

The infrared camera provides high-quality depth information that’s synchronized and perspective corrected to the frame the YUV camera produces. While the resolution of the depth data and YUV frames may differ, their field of view and aspect ratio always match.

> ❗ **Important**:  To obtain a device of this type, use the [`default(_:for:position:)`](../default%28_,for,position%29.md) method or the [`AVCaptureDevice.DiscoverySession`](../discoverysession.md) class. Other methods don’t discover devices of this type.

## See Also

### Depth sensing
- [static let builtInLiDARDepthCamera: AVCaptureDevice.DeviceType](./builtinlidardepthcamera.md)
  A device that consists of two cameras, one LiDAR and one YUV.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtintruedepthcamera)*