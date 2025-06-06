# init(captureDevice:cameraPosition:orientation:cameraIntrinsics:referenceDimensions:)

**Framework**: DockKit  
**Kind**: init

Creates an object that describes the camera in use for tracking.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.1+

## Declaration

```swift
init(captureDevice: AVCaptureDevice.DeviceType, cameraPosition: AVCaptureDevice.Position, orientation: DockAccessory.CameraOrientation, cameraIntrinsics: matrix_float3x3?, referenceDimensions: CGSize?)
```

## Parameters

- `captureDevice`: The capture device generating the video.
- `cameraPosition`: The physical position of the capture device.
- `orientation`: The orientation of the capture device.
- `cameraIntrinsics`: A matrix that represents the characteristics of the lens.
- `referenceDimensions`: The size of the video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/camerainformation/init(capturedevice:cameraposition:orientation:cameraintrinsics:referencedimensions:))*