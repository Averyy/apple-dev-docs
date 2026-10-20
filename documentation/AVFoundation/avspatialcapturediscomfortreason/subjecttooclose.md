# subjectTooClose

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A value that indicates the focus point of the current scene is too close.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
static let subjectTooClose: AVSpatialCaptureDiscomfortReason
```

```c
extern AVSpatialCaptureDiscomfortReason const AVSpatialCaptureDiscomfortReasonSubjectTooClose;
```

#### Discussion

The playback experience would likely be uncomfortable due to the subject being closer than the minimum focus distance of one or both of the lenses.

## See Also

### Discomfort reasons
- [static let notEnoughLight: AVSpatialCaptureDiscomfortReason](./notenoughlight.md)
  A value that indicates the lighting of the current scene isn’t bright enough.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avspatialcapturediscomfortreason/subjecttooclose)*