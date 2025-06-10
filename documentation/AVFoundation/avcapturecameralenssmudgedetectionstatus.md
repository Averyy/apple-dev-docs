# AVCaptureCameraLensSmudgeDetectionStatus

**Framework**: AVFoundation  
**Kind**: enum

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
enum AVCaptureCameraLensSmudgeDetectionStatus
```

#### Overview

Constants indicating the current camera lens smudge detection status.

Indicates that the detection is not enabled.

Indicates that the most recent detection identifies smudge is not detected on camera lens.

Indicates that the most recent detection identifies camera lens is smudged.

Indicates that the detection result hasn’t settled, commonly caused by excessive camera movement or the content of image.

## Topics

### Enumeration Cases
- [AVCaptureCameraLensSmudgeDetectionStatus.disabled](avcapturecameralenssmudgedetectionstatus/disabled.md)
- [AVCaptureCameraLensSmudgeDetectionStatus.smudgeNotDetected](avcapturecameralenssmudgedetectionstatus/smudgenotdetected.md)
- [AVCaptureCameraLensSmudgeDetectionStatus.smudged](avcapturecameralenssmudgedetectionstatus/smudged.md)
- [AVCaptureCameraLensSmudgeDetectionStatus.unknown](avcapturecameralenssmudgedetectionstatus/unknown.md)
### Initializers
- [init?(rawValue: Int)](avcapturecameralenssmudgedetectionstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturecameralenssmudgedetectionstatus)*