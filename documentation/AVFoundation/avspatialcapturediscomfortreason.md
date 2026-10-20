# AVSpatialCaptureDiscomfortReason

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * AVSpatialCaptureDiscomfortReason;
```

## Topics

### Discomfort reasons
- [static let notEnoughLight: AVSpatialCaptureDiscomfortReason](./avspatialcapturediscomfortreason/notenoughlight.md)
  A value that indicates the lighting of the current scene isn’t bright enough.
- [static let subjectTooClose: AVSpatialCaptureDiscomfortReason](./avspatialcapturediscomfortreason/subjecttooclose.md)
  A value that indicates the focus point of the current scene is too close.
### Initializers
- [init(rawValue: String)](./avspatialcapturediscomfortreason/init%28rawvalue%29.md)
  Creates a discomfort reason with a string value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting spatial capture
- [var spatialCaptureDiscomfortReasons: Set<AVSpatialCaptureDiscomfortReason>](./avcapturedevice/spatialcapturediscomfortreasons.md)
  Reasons why current environmental conditions aren’t suitable to capturing spatial videos that are comfortable to view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avspatialcapturediscomfortreason)*