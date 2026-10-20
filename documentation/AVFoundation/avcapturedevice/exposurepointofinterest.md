# exposurePointOfInterest

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) CGPoint exposurePointOfInterest;
```

#### Discussion

Setting a value for this property doesn’t initiate an exposure rebalancing operation. To set exposure using a point of interest, first set this property’s value, then set the [`exposureMode`](./exposuremode-swift.property.md) property to [`AVCaptureDevice.ExposureMode.autoExpose`](./exposuremode-swift.enum/autoexpose.md) or [`AVCaptureDevice.ExposureMode.continuousAutoExposure`](./exposuremode-swift.enum/continuousautoexposure.md).

This property’s [`CGPoint`](../../CoreFoundation/cgpoint.md) value uses a coordinate system where `{0,0}` is the top-left of the picture area and `{1,1}` is the bottom-right. This coordinate system is always relative to a landscape device orientation with the home button on the right, regardless of the actual device orientation. You can convert between this coordinate system and view coordinates using [`AVCaptureVideoPreviewLayer`](../avcapturevideopreviewlayer.md) methods.

Before changing the value of this property, you must call [`lockForConfiguration()`](./lockforconfiguration%28%29.md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re done configuring the device, call [`unlockForConfiguration()`](./unlockforconfiguration%28%29.md) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

### Setting an exposure point of interest
- [var isExposurePointOfInterestSupported: Bool](./isexposurepointofinterestsupported.md)
  A Boolean value that indicates whether the device supports a point of interest for exposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposurepointofinterest)*