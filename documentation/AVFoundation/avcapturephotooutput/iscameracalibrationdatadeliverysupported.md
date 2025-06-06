# isCameraCalibrationDataDeliverySupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value indicating whether the capture output currently supports delivery of camera calibration data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isCameraCalibrationDataDeliverySupported: Bool { get }
```

#### Discussion

[`AVCameraCalibrationData`](avcameracalibrationdata.md) objects describe the imaging parameters of a device camera, and can be useful for performing computer vision tasks in conjunction with dual photo delivery on dual-camera devices.This property’s value can be [`true`](https://developer.apple.com/documentation/swift/true) only when the [`isDualCameraDualPhotoDeliveryEnabled`](avcapturephotosettings/isdualcameradualphotodeliveryenabled.md) property is [`true`](https://developer.apple.com/documentation/swift/true). To enable camera calibration delivery, set the [`isCameraCalibrationDataDeliveryEnabled`](avcapturephotosettings/iscameracalibrationdatadeliveryenabled.md) property in a photo settings object.

This property is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/iscameracalibrationdatadeliverysupported)*