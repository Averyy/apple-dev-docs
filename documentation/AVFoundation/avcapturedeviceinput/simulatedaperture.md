# simulatedAperture

**Framework**: AVFoundation  
**Kind**: property

Shallow depth of field simulated aperture.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var simulatedAperture: Float { get set }
```

#### Discussion

When capturing a Cinematic Video, use this property to control the amount of blur in the simulated depth of field effect.

This property only takes effect when [`isCinematicVideoCaptureEnabled`](avcapturedeviceinput/iscinematicvideocaptureenabled.md) is set to `true`.

> ❗ **Important**: Setting this property to a value less than the `AVCaptureDevice/activeFormat/minSimulatedAperture` or greater than the `AVCaptureDevice/activeFormat/maxSimulatedAperture` throws an `NSRangeException`. you may only set this property if `AVCaptureDevice/activeFormat/minSimulatedAperture` returns a non-zero value, otherwise an `NSInvalidArgumentException` is thrown. You must set this property before starting a Cinematic Video capture. If you attempt to set it while a recording is in progress, an `NSInvalidArgumentException` is thrown.

This property is initialized to the associated `AVCaptureDevice/activeFormat/defaultSimulatedAperture`.

This property is key-value observable.

## See Also

- [var isCinematicVideoCaptureSupported: Bool](avcapturedeviceinput/iscinematicvideocapturesupported.md)
  A BOOL value specifying whether Cinematic Video capture is supported.
- [var isCinematicVideoCaptureEnabled: Bool](avcapturedeviceinput/iscinematicvideocaptureenabled.md)
  A BOOL value specifying whether the Cinematic Video effect is being applied to any movie file output, video data output, metadata output, or video preview layer added to the capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/simulatedaperture)*