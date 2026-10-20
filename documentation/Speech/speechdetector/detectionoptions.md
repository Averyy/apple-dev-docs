# SpeechDetector.DetectionOptions

**Framework**: Speech  
**Kind**: struct  
**Role**: Structure

Allows clients to customize an instance of a speech detector.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DetectionOptions
```

## Parameters

- `sensitivityLevel`: One of [`SpeechDetector.SensitivityLevel`](./sensitivitylevel.md). This value is used to determine how “aggressive” the voice activity detection (VAD) model will be.

## Topics

### Creating an options object
- [init(sensitivityLevel: SpeechDetector.SensitivityLevel)](./detectionoptions/init%28sensitivitylevel%29.md)
### Inspecting options
- [let sensitivityLevel: SpeechDetector.SensitivityLevel](./detectionoptions/sensitivitylevel.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a detector
- [convenience init()](./init%28%29.md)
  Creates a speech detector with default settings.
- [init(detectionOptions: SpeechDetector.DetectionOptions, reportResults: Bool)](./init%28detectionoptions,reportresults%29.md)
  Creates a speech detector.
- [SpeechDetector.SensitivityLevel](./sensitivitylevel.md)
  Determines how “aggressive” the voice activity detection (VAD) model will be.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector/detectionoptions)*