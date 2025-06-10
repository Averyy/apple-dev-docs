# SpeechDetector.DetectionOptions

**Framework**: Speech  
**Kind**: struct

Allows clients to customize an instance of a speech detector.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct DetectionOptions
```

## Parameters

- `sensitivityLevel`: One of  . This value is used to determine how “aggressive” the voice activity detection (VAD) model will be.

## Topics

### Initializers
- [init(sensitivityLevel: SpeechDetector.SensitivityLevel)](speechdetector/detectionoptions/init(sensitivitylevel:).md)
### Instance Properties
- [let sensitivityLevel: SpeechDetector.SensitivityLevel](speechdetector/detectionoptions/sensitivitylevel.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [SpeechDetector.Result](speechdetector/result.md)
  A result from the speech detector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector/detectionoptions)*