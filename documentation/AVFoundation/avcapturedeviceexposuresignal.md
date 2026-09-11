# AVCaptureDeviceExposureSignal

**Framework**: AVFoundation  
**Kind**: struct

Values that can be used to configure the auto exposure system via [`enabledExposureSignals`](avcapturedevice/enabledexposuresignals.md) and associated methods.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+

## Declaration

```swift
struct AVCaptureDeviceExposureSignal
```

## Topics

### Creating an exposure signal
- [init(rawValue: String)](avcapturedeviceexposuresignal/init(rawvalue:).md)
### Exposure signals
- [static let document: AVCaptureDeviceExposureSignal](avcapturedeviceexposuresignal/document.md)
  When enabled, auto exposure may close the aperture to improve sharpness of textual scenes.
- [static let flicker: AVCaptureDeviceExposureSignal](avcapturedeviceexposuresignal/flicker.md)
  When enabled, auto exposure may adjust the aperture to help exposure duration avoid synchronization with artificial lighting frequencies.
- [static let groupPhoto: AVCaptureDeviceExposureSignal](avcapturedeviceexposuresignal/groupphoto.md)
  When enabled, auto exposure may close the aperture to increase depth of field when multiple faces are in the scene.
- [static let starburst: AVCaptureDeviceExposureSignal](avcapturedeviceexposuresignal/starburst.md)
  When enabled, auto exposure may open the aperture to remove diffraction artifacts from point light sources.
- [static let subjectMotion: AVCaptureDeviceExposureSignal](avcapturedeviceexposuresignal/subjectmotion.md)
  When enabled, auto exposure may close the aperture or decrease the exposure duration to reduce motion blur when there is a lot of motion in the scene.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var activeExposureSignals: Set<AVCaptureDeviceExposureSignal>](avcapturedevice/activeexposuresignals.md)
  Reports which characteristics the auto exposure system associates with the current scene. Auto exposure may adjust properties such as lens aperture size based on these factors. This property is key-value observable.
- [var enabledExposureSignals: Set<AVCaptureDeviceExposureSignal>](avcapturedevice/enabledexposuresignals.md)
  Can be assigned to control which characteristics AE should use in its decision making, must be a subset of supportedExposureSignals.
- [var supportedExposureSignals: Set<AVCaptureDeviceExposureSignal>](avcapturedevice/supportedexposuresignals.md)
  Indicates what values can be included in `enabledExposureSignals`. This property is key-value observable.
- [var automaticallyEnablesExposureSignals: Bool](avcapturedevice/automaticallyenablesexposuresignals.md)
  When true (the default), capture sessions may automatically modify `enabledExposureSignals` based on changes to other device or session properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceexposuresignal)*