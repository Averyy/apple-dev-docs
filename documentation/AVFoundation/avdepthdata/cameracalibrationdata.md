# cameraCalibrationData

**Framework**: AVFoundation  
**Kind**: property

The imaging parameters with which this depth data was captured.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var cameraCalibrationData: AVCameraCalibrationData? { get }
```

#### Discussion

Using depth or disparity map data to render effects into a corresponding image or to perform computer vision tasks requires knowledge of the camera parameters that generated the depth data. Depth data captured by an [`AVCaptureDevice`](avcapturedevice.md) object contains camera calibration data that includes such information.

> **Note**:  Depth data read from a file (see the [`init(fromDictionaryRepresentation:)`](avdepthdata/init(fromdictionaryrepresentation:).md) initializer) or transformed through arbitrary editing of its data map might not contain calibration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/cameracalibrationdata)*