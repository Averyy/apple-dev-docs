# captureDeviceType

**Framework**: ARKit  
**Kind**: property

The camera that supplies the video format.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+

## Declaration

```swift
var captureDeviceType: AVCaptureDevice.DeviceType { get }
```

#### Discussion

To specify a particular video format, select from your configuration’s [`supportedVideoFormats`](arconfiguration/supportedvideoformats.md) and set the desired format to the configuration’s [`videoFormat`](arconfiguration/videoformat-swift.property.md) property.

For example, to specify the ultra-wide camera in a face-tracking session, search the supported video formats for the [`builtInUltraWideCamera`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/DeviceType-swift.struct/builtInUltraWideCamera) capture device.

```swift
let config = ARFaceTrackingConfiguration()
for videoFormat in ARFaceTrackingConfiguration.supportedVideoFormats {
    if videoFormat.captureDeviceType == .builtInUltraWideCamera {
        config.videoFormat = videoFormat
        break
    }
}
session.run(config)
```

> ❗ **Important**:  AR frames only contain depth data ([`capturedDepthData`](arframe/captureddepthdata.md)) in face-tracking sessions that use the TrueDepth camera.

## See Also

- [var captureDevicePosition: AVCaptureDevice.Position](arconfiguration/videoformat-swift.class/capturedeviceposition.md)
  The position of the capture device.
- [enum AVCaptureDevice.Position](../avfoundation/avcapturedevice/position.md)
  Constants that indicate the physical position of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/videoformat-swift.class/capturedevicetype)*