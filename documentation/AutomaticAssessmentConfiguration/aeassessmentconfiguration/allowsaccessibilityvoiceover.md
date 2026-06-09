# allowsAccessibilityVoiceOver

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow VoiceOver during an assessment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsAccessibilityVoiceOver: Bool { get set }
```

#### Discussion

Users can enable VoiceOver in the Settings app (Accessibility > VoiceOver) to receive spoken descriptions of on-screen elements and gestures for navigating the interface. An assessment session **does not** disable VoiceOver by default, but you can disable it by setting [`allowsAccessibilityVoiceOver`](aeassessmentconfiguration/allowsaccessibilityvoiceover.md) to `NO` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilityvoiceover)*