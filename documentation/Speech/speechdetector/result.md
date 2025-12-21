# SpeechDetector.Result

**Framework**: Speech  
**Kind**: struct

A result from the speech detector. Please note, these must be enabled via [`init(detectionOptions:reportResults:)`](speechdetector/init(detectionoptions:reportresults:).md) and currently only support error handling from the VAD model.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Result
```

## Topics

### Getting detection results
- [let speechDetected: Bool](speechdetector/result/speechdetected.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpeechModuleResult](speechmoduleresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector/result)*