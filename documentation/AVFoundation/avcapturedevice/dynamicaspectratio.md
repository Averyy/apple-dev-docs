# dynamicAspectRatio

**Framework**: AVFoundation  
**Kind**: property

A key-value observable property indicating the current aspect ratio for a device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var dynamicAspectRatio: AVCaptureDevice.AspectRatio? { get }
```

#### Discussion

This property is initialized to the first [`AVCaptureDevice.AspectRatio`](avcapturedevice/aspectratio.md) listed in the device’s activeFormat’s [`supportedDynamicAspectRatios`](avcapturedevice/format/supporteddynamicaspectratios.md) property. If the activeFormat’s [`supportedDynamicAspectRatios`](avcapturedevice/format/supporteddynamicaspectratios.md) is an empty array, this property returns nil.

## See Also

- [func setDynamicAspectRatio(AVCaptureDevice.AspectRatio, completionHandler: ((CMTime, (any Error)?) -> Void)?)](avcapturedevice/setdynamicaspectratio(_:completionhandler:).md)
  Updates the dynamic aspect ratio of the device.
- [AVCaptureDevice.AspectRatio](avcapturedevice/aspectratio.md)
  String constants describing the different video aspect ratios you can configure for a particular device.
- [var dynamicDimensions: CMVideoDimensions](avcapturedevice/dynamicdimensions.md)
  A key-value observable property describing the output dimensions of the video buffer based on the device’s dynamic aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/dynamicaspectratio)*