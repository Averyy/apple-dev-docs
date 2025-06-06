# exposurePointOfInterest

**Framework**: AVFoundation  
**Kind**: property

The point of interest for exposure.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var exposurePointOfInterest: CGPoint { get set }
```

#### Discussion

Setting a value for this property doesn’t initiate an exposure rebalancing operation. To set exposure using a point of interest, first set this property’s value, then set the [`exposureMode`](avcapturedevice/exposuremode-swift.property.md) property to [`AVCaptureDevice.ExposureMode.autoExpose`](avcapturedevice/exposuremode-swift.enum/autoexpose.md) or [`AVCaptureDevice.ExposureMode.continuousAutoExposure`](avcapturedevice/exposuremode-swift.enum/continuousautoexposure.md).

This property’s [`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint) value uses a coordinate system where `{0,0}` is the top-left of the picture area and `{1,1}` is the bottom-right. This coordinate system is always relative to a landscape device orientation with the home button on the right, regardless of the actual device orientation. You can convert between this coordinate system and view coordinates using [`AVCaptureVideoPreviewLayer`](avcapturevideopreviewlayer.md) methods.

Before changing the value of this property, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re done configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

- [var isExposurePointOfInterestSupported: Bool](avcapturedevice/isexposurepointofinterestsupported.md)
  A Boolean value that indicates whether the device supports a point of interest for exposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposurepointofinterest)*