# SpeechDetector.SensitivityLevel

**Framework**: Speech  
**Kind**: enum

Determines how “aggressive” the voice activity detection (VAD) model will be.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum SensitivityLevel
```

#### Overview

[`SpeechDetector.SensitivityLevel.low`](speechdetector/sensitivitylevel/low.md) will allow for a more “forgiving” VAD model, whereas selecting [`SpeechDetector.SensitivityLevel.high`](speechdetector/sensitivitylevel/high.md) will make the model more aggressive. [`SpeechDetector.SensitivityLevel.medium`](speechdetector/sensitivitylevel/medium.md) is the recommended level for most use cases.

## Topics

### Sensitivity levels
- [SpeechDetector.SensitivityLevel.high](speechdetector/sensitivitylevel/high.md)
- [SpeechDetector.SensitivityLevel.low](speechdetector/sensitivitylevel/low.md)
- [SpeechDetector.SensitivityLevel.medium](speechdetector/sensitivitylevel/medium.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init()](speechdetector/init.md)
  Creates a speech detector with default settings.
- [init(detectionOptions: SpeechDetector.DetectionOptions, reportResults: Bool)](speechdetector/init(detectionoptions:reportresults:).md)
  Creates a speech detector.
- [SpeechDetector.DetectionOptions](speechdetector/detectionoptions.md)
  Allows clients to customize an instance of a speech detector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector/sensitivitylevel)*