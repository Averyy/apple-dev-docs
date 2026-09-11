# enabledExposureSignals

**Framework**: AVFoundation  
**Kind**: property

Can be assigned to control which characteristics AE should use in its decision making, must be a subset of supportedExposureSignals.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+

## Declaration

```swift
var enabledExposureSignals: Set<AVCaptureDeviceExposureSignal> { get set }
```

#### Discussion

When `automaticallyEnablesExposureSignals` is true, the system may automatically change the enabled signals based on other enabled device properties. When `automaticallyEnablesExposureSignals` is false, you may assign a custom set of exposure signals to this property. This property is key-value observable.

> **Note**: `NSInvalidArgumentException` if assigned while `automaticallyEnablesExposureSignals` is true

> **Note**: `NSGenericException` if assigned without first obtaining exclusive access to the receiver using [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md).

## See Also

- [var activeExposureSignals: Set<AVCaptureDeviceExposureSignal>](avcapturedevice/activeexposuresignals.md)
  Reports which characteristics the auto exposure system associates with the current scene. Auto exposure may adjust properties such as lens aperture size based on these factors. This property is key-value observable.
- [var supportedExposureSignals: Set<AVCaptureDeviceExposureSignal>](avcapturedevice/supportedexposuresignals.md)
  Indicates what values can be included in `enabledExposureSignals`. This property is key-value observable.
- [var automaticallyEnablesExposureSignals: Bool](avcapturedevice/automaticallyenablesexposuresignals.md)
  When true (the default), capture sessions may automatically modify `enabledExposureSignals` based on changes to other device or session properties.
- [struct AVCaptureDeviceExposureSignal](avcapturedeviceexposuresignal.md)
  Values that can be used to configure the auto exposure system via [`enabledExposureSignals`](avcapturedevice/enabledexposuresignals.md) and associated methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/enabledexposuresignals)*