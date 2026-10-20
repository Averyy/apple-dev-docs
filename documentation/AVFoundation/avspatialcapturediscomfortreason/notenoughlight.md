# notEnoughLight

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A value that indicates the lighting of the current scene isn’t bright enough.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
static let notEnoughLight: AVSpatialCaptureDiscomfortReason
```

```c
extern AVSpatialCaptureDiscomfortReason const AVSpatialCaptureDiscomfortReasonNotEnoughLight;
```

#### Discussion

The playback experience would likely be uncomfortable due to noise differences between the wide and ultrawide cameras.

## See Also

### Discomfort reasons
- [static let subjectTooClose: AVSpatialCaptureDiscomfortReason](./subjecttooclose.md)
  A value that indicates the focus point of the current scene is too close.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avspatialcapturediscomfortreason/notenoughlight)*