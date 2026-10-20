# dynamicAspectRatio

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A key-value observable property indicating the current aspect ratio for a device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var dynamicAspectRatio: AVCaptureDevice.AspectRatio? { get }
```

```objc
@property (readonly, nullable) AVCaptureAspectRatio dynamicAspectRatio;
```

#### Discussion

This property is initialized to the first [`AVCaptureDevice.AspectRatio`](./aspectratio.md) listed in the device’s activeFormat’s [`supportedDynamicAspectRatios`](./format/supporteddynamicaspectratios.md) property. If the activeFormat’s [`supportedDynamicAspectRatios`](./format/supporteddynamicaspectratios.md) is an empty array, this property returns nil.

## See Also

### Configuring dynamic aspect ratio
- [func setDynamicAspectRatio(AVCaptureDevice.AspectRatio, completionHandler: ((CMTime, (any Error)?) -> Void)?)](./setdynamicaspectratio%28_,completionhandler%29.md)
  Updates the dynamic aspect ratio of the device.
- [AVCaptureDevice.AspectRatio](./aspectratio.md)
  String constants describing the different video aspect ratios you can configure for a particular device.
- [var dynamicDimensions: CMVideoDimensions](./dynamicdimensions.md)
  A key-value observable property describing the output dimensions of the video buffer based on the device’s dynamic aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/dynamicaspectratio)*