# isCameraCalibrationDataDeliverySupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isCameraCalibrationDataDeliverySupported) BOOL cameraCalibrationDataDeliverySupported;
```

## Discussion

A photo output can deliver camera calibration data only when it’s [`isVirtualDeviceConstituentPhotoDeliveryEnabled`](./isvirtualdeviceconstituentphotodeliveryenabled.md) property is `true` and its [`isContentAwareDistortionCorrectionEnabled`](./iscontentawaredistortioncorrectionenabled.md) property is `false`. Additionally, the source capture device’s [`isGeometricDistortionCorrectionEnabled`](../avcapturedevice/isgeometricdistortioncorrectionenabled.md) property must be `false`.

This property is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/iscameracalibrationdatadeliverysupported)*