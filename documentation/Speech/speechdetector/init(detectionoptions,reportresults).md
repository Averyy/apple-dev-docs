# init(detectionOptions:reportResults:)

**Framework**: Speech  
**Kind**: init  
**Role**: Initializer

Creates a speech detector.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(detectionOptions: SpeechDetector.DetectionOptions, reportResults: Bool)
```

## Parameters

- `detectionOptions`: Instance of [`SpeechDetector.DetectionOptions`](./detectionoptions.md) that allows clients to customize the behavior of [`SpeechDetector`](../speechdetector.md) beyond its default settings.
- `reportResults`: Enables the [`results`](./results.md) sequence to report the VAD model’s results (and any relevant errors) back to clients. The default behavior is that [`SpeechDetector`](../speechdetector.md) does not report results or errors back to the client and merely enables VAD as a power optimization.

## See Also

### Creating a detector
- [convenience init()](./init%28%29.md)
  Creates a speech detector with default settings.
- [SpeechDetector.DetectionOptions](./detectionoptions.md)
  Allows clients to customize an instance of a speech detector.
- [SpeechDetector.SensitivityLevel](./sensitivitylevel.md)
  Determines how “aggressive” the voice activity detection (VAD) model will be.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector/init(detectionoptions:reportresults:))*