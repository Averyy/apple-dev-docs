# formats

**Framework**: AVFoundation  
**Kind**: property

The capture formats a device supports.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var formats: [AVCaptureDevice.Format] { get }
```

#### Discussion

A capture device format describes the details of the video, image, or audio parameters of a specific mode of capture. If you require specifying capture settings not covered by a capture session preset, you can set the [`activeFormat`](avcapturedevice/activeformat.md) property to any of the formats in this array.

This property value is key-value observable.

## See Also

- [var activeFormat: AVCaptureDevice.Format](avcapturedevice/activeformat.md)
  The capture format in use by the device.
- [var activeDepthDataFormat: AVCaptureDevice.Format?](avcapturedevice/activedepthdataformat.md)
  The currently active depth data format of the capture device.
- [AVCaptureDevice.Format](avcapturedevice/format.md)
  A class that defines media formats and capture settings that capture devices support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/formats)*