# allowsAccessibilityVoiceControl

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow Voice Control during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsAccessibilityVoiceControl: Bool { get set }
```

#### Discussion

Users can enable Voice Control in the Settings app (Accessibility > Voice Control) to control their device using voice commands. An assessment session **does not** disable Voice Control by default, but you can disable it by setting [`allowsAccessibilityVoiceControl`](aeassessmentconfiguration/allowsaccessibilityvoicecontrol.md) to `NO` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilityvoicecontrol)*