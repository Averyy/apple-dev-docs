# SpeechDetector.SensitivityLevel

**Framework**: Speech  
**Kind**: enum  
**Role**: Enumeration

Determines how “aggressive” the voice activity detection (VAD) model will be.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum SensitivityLevel
```

## Overview

[`SpeechDetector.SensitivityLevel.low`](./sensitivitylevel/low.md) will allow for a more “forgiving” VAD model, whereas selecting [`SpeechDetector.SensitivityLevel.high`](./sensitivitylevel/high.md) will make the model more aggressive. [`SpeechDetector.SensitivityLevel.medium`](./sensitivitylevel/medium.md) is the recommended level for most use cases.

## Topics

### Sensitivity levels
- [SpeechDetector.SensitivityLevel.high](./sensitivitylevel/high.md)
- [SpeechDetector.SensitivityLevel.low](./sensitivitylevel/low.md)
- [SpeechDetector.SensitivityLevel.medium](./sensitivitylevel/medium.md)

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a detector
- [convenience init()](./init%28%29.md)
  Creates a speech detector with default settings.
- [init(detectionOptions: SpeechDetector.DetectionOptions, reportResults: Bool)](./init%28detectionoptions,reportresults%29.md)
  Creates a speech detector.
- [SpeechDetector.DetectionOptions](./detectionoptions.md)
  Allows clients to customize an instance of a speech detector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector/sensitivitylevel)*