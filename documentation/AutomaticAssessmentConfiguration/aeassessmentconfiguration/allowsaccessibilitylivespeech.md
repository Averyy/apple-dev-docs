# allowsAccessibilityLiveSpeech

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow Live Speech during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsAccessibilityLiveSpeech: Bool { get set }
```

#### Discussion

Users can enable Live Speech in the Settings app (Accessibility > Speech > Live Speech) to type what they want to say and have it spoken aloud. An assessment session disables Live Speech by default, but you can allow it by setting [`allowsAccessibilityLiveSpeech`](aeassessmentconfiguration/allowsaccessibilitylivespeech.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilitylivespeech)*