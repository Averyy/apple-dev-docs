# activeExposureSignals

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Reports which characteristics the auto exposure system associates with the current scene. Auto exposure may adjust properties such as lens aperture size based on these factors. This property is key-value observable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+

## Declaration

```swift
var activeExposureSignals: Set<AVCaptureDeviceExposureSignal> { get }
```

```objc
@property (nonatomic, readonly, nonnull) NSSet<NSString *> * activeExposureSignals;
```

## See Also

### Configuring exposure signals
- [var enabledExposureSignals: Set<AVCaptureDeviceExposureSignal>](./enabledexposuresignals.md)
  Can be assigned to control which characteristics AE should use in its decision making, must be a subset of supportedExposureSignals.
- [var supportedExposureSignals: Set<AVCaptureDeviceExposureSignal>](./supportedexposuresignals.md)
  Indicates what values can be included in `enabledExposureSignals`. This property is key-value observable.
- [var automaticallyEnablesExposureSignals: Bool](./automaticallyenablesexposuresignals.md)
  When true (the default), capture sessions may automatically modify `enabledExposureSignals` based on changes to other device or session properties.
- [struct AVCaptureDeviceExposureSignal](../avcapturedeviceexposuresignal.md)
  Values that can be used to configure the auto exposure system via [`enabledExposureSignals`](./enabledexposuresignals.md) and associated methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activeexposuresignals)*