# isCameraCalibrationDataDeliverySupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the photo output currently supports the delivery of camera calibration data.

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

A photo output can deliver camera calibration data only when it’s [`isVirtualDeviceConstituentPhotoDeliveryEnabled`](avcapturephotooutput/isvirtualdeviceconstituentphotodeliveryenabled.md) property is `true` and its [`isContentAwareDistortionCorrectionEnabled`](avcapturephotooutput/iscontentawaredistortioncorrectionenabled.md) property is `false`. Additionally, the source capture device’s [`isGeometricDistortionCorrectionEnabled`](avcapturedevice/isgeometricdistortioncorrectionenabled.md) property must be `false`.

This property is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/iscameracalibrationdatadeliverysupported)*