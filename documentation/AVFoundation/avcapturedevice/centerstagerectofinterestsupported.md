# centerStageRectOfInterestSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

## Declaration

```objc
@property (nonatomic, readonly, getter=isCenterStageRectOfInterestSupported) BOOL centerStageRectOfInterestSupported;
```

## Discussion

Indicates whether the device supports the Center Stage Rect of Interest feature.

This property returns YES if the device supports Center Stage Rect of Interest.

## See Also

### Configuring Center Stage
- [var isCenterStageActive: Bool](./iscenterstageactive.md)
  A Boolean value that indicates whether Center Stage is active on a device.
- [class var isCenterStageEnabled: Bool](./iscenterstageenabled.md)
  A Boolean value that indicates whether a user or an app enabled Center Stage on a device.
- [var centerStageRectOfInterest: CGRect](./centerstagerectofinterest.md)
  The effective region within the output pixel buffer to perform Center Stage framing.
- [class var centerStageControlMode: AVCaptureDevice.CenterStageControlMode](./centerstagecontrolmode-swift.type.property.md)
  A value that indicates the current mode of Center Stage control.
- [AVCaptureDevice.CenterStageControlMode](./centerstagecontrolmode-swift.enum.md)
  Constants that indicate the current Center Stage control mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/centerstagerectofinterestsupported)*