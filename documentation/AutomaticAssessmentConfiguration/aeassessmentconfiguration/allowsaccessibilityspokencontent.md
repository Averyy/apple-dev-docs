# allowsAccessibilitySpokenContent

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow Spoken Content during an assessment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsAccessibilitySpokenContent: Bool { get set }
```

#### Discussion

Users can enable Spoken Content in the Settings app (Accessibility > Spoken Content) to have text read aloud. This includes Speak Selection, Speak Screen, and related features. An assessment session disables Spoken Content by default, but you can allow it by setting [`allowsAccessibilitySpokenContent`](aeassessmentconfiguration/allowsaccessibilityspokencontent.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilityspokencontent)*