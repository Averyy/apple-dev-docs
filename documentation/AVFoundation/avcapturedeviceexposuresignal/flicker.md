# flicker

**Framework**: AVFoundation  
**Kind**: property

When enabled, auto exposure may adjust the aperture to help exposure duration avoid synchronization with artificial lighting frequencies.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+

## Declaration

```swift
static let flicker: AVCaptureDeviceExposureSignal
```

## See Also

- [static let document: AVCaptureDeviceExposureSignal](avcapturedeviceexposuresignal/document.md)
  When enabled, auto exposure may close the aperture to improve sharpness of textual scenes.
- [static let groupPhoto: AVCaptureDeviceExposureSignal](avcapturedeviceexposuresignal/groupphoto.md)
  When enabled, auto exposure may close the aperture to increase depth of field when multiple faces are in the scene.
- [static let starburst: AVCaptureDeviceExposureSignal](avcapturedeviceexposuresignal/starburst.md)
  When enabled, auto exposure may open the aperture to remove diffraction artifacts from point light sources.
- [static let subjectMotion: AVCaptureDeviceExposureSignal](avcapturedeviceexposuresignal/subjectmotion.md)
  When enabled, auto exposure may close the aperture or decrease the exposure duration to reduce motion blur when there is a lot of motion in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceexposuresignal/flicker)*