# SpeechDetector.DetectionOptions

**Framework**: Speech  
**Kind**: struct

Allows clients to customize an instance of a speech detector.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DetectionOptions
```

## Parameters

- `sensitivityLevel`: One of  . This value is used to determine how “aggressive” the voice activity detection (VAD) model will be.

## Topics

### Creating an options object
- [init(sensitivityLevel: SpeechDetector.SensitivityLevel)](speechdetector/detectionoptions/init(sensitivitylevel:).md)
### Inspecting options
- [let sensitivityLevel: SpeechDetector.SensitivityLevel](speechdetector/detectionoptions/sensitivitylevel.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init()](speechdetector/init.md)
  Creates a speech detector with default settings.
- [init(detectionOptions: SpeechDetector.DetectionOptions, reportResults: Bool)](speechdetector/init(detectionoptions:reportresults:).md)
  Creates a speech detector.
- [SpeechDetector.SensitivityLevel](speechdetector/sensitivitylevel.md)
  Determines how “aggressive” the voice activity detection (VAD) model will be.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector/detectionoptions)*