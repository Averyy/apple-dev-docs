# allowsAccessibilityLiveCaptions

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow Live Captions during an assessment.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+

## Declaration

```swift
var allowsAccessibilityLiveCaptions: Bool { get set }
```

#### Discussion

Users can enable Live Captions in the Settings app (Accessibility > Live Captions) to receive real-time transcription of spoken audio as text on screen. An assessment session disables Live Captions by default, but you can allow it by setting [`allowsAccessibilityLiveCaptions`](aeassessmentconfiguration/allowsaccessibilitylivecaptions.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilitylivecaptions)*