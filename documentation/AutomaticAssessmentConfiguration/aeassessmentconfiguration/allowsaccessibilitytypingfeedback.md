# allowsAccessibilityTypingFeedback

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow accessibility typing feedback during an assessment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var allowsAccessibilityTypingFeedback: Bool { get set }
```

#### Discussion

Users can enable typing feedback features in the Settings app (Accessibility > Keyboards & Typing > Typing Feedback)  to receive audio feedback when typing. An assessment session disables these accessibility typing feedback features by default, but you can allow them by setting [`allowsAccessibilityTypingFeedback`](aeassessmentconfiguration/allowsaccessibilitytypingfeedback.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilitytypingfeedback)*