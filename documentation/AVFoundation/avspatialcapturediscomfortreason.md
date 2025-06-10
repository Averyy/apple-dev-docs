# AVSpatialCaptureDiscomfortReason

**Framework**: AVFoundation  
**Kind**: struct

Constants that indicate the suitability of the current scene to create a comfortable viewing experience.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
struct AVSpatialCaptureDiscomfortReason
```

## Topics

### Discomfort Reasons
- [static let notEnoughLight: AVSpatialCaptureDiscomfortReason](avspatialcapturediscomfortreason/notenoughlight.md)
  A value that indicates the lighting of the current scene isn’t bright enough.
- [static let subjectTooClose: AVSpatialCaptureDiscomfortReason](avspatialcapturediscomfortreason/subjecttooclose.md)
  A value that indicates the focus point of the current scene is too close.
### Initializers
- [init(rawValue: String)](avspatialcapturediscomfortreason/init(rawvalue:).md)
  Creates a discomfort reason with a string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var spatialCaptureDiscomfortReasons: Set<AVSpatialCaptureDiscomfortReason>](avcapturedevice/spatialcapturediscomfortreasons.md)
  Reasons why current environmental conditions aren’t suitable to capturing spatial videos that are comfortable to view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avspatialcapturediscomfortreason)*