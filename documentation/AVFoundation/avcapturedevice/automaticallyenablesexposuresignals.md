# automaticallyEnablesExposureSignals

**Framework**: AVFoundation  
**Kind**: property

When true (the default), capture sessions may automatically modify `enabledExposureSignals` based on changes to other device or session properties.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+

## Declaration

```swift
var automaticallyEnablesExposureSignals: Bool { get set }
```

#### Discussion

The `enabledExposureSignals` property can only be assigned when `automaticallyEnablesExposureSignals` is false, otherwise assignments to `enabledExposureSignals` will throw an exception.

> **Note**: `NSGenericException` if assigned without first obtaining exclusive access to the receiver using [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md).

## See Also

- [var activeExposureSignals: Set<AVCaptureDeviceExposureSignal>](avcapturedevice/activeexposuresignals.md)
  Reports which characteristics the auto exposure system associates with the current scene. Auto exposure may adjust properties such as lens aperture size based on these factors. This property is key-value observable.
- [var enabledExposureSignals: Set<AVCaptureDeviceExposureSignal>](avcapturedevice/enabledexposuresignals.md)
  Can be assigned to control which characteristics AE should use in its decision making, must be a subset of supportedExposureSignals.
- [var supportedExposureSignals: Set<AVCaptureDeviceExposureSignal>](avcapturedevice/supportedexposuresignals.md)
  Indicates what values can be included in `enabledExposureSignals`. This property is key-value observable.
- [struct AVCaptureDeviceExposureSignal](avcapturedeviceexposuresignal.md)
  Values that can be used to configure the auto exposure system via [`enabledExposureSignals`](avcapturedevice/enabledexposuresignals.md) and associated methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/automaticallyenablesexposuresignals)*