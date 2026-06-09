# allowsAccessibilitySwitchControl

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow Switch Control during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsAccessibilitySwitchControl: Bool { get set }
```

#### Discussion

Users can enable Switch Control in the Settings app (Accessibility > Switch Control) to control their device using adaptive switches. An assessment session **does not** disable Switch Control by default, but you can disable it by setting [`allowsAccessibilitySwitchControl`](aeassessmentconfiguration/allowsaccessibilityswitchcontrol.md) to `NO` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.

> **Note**: To allow Switch Control with alternative input methods (such as Dwell Control), you must also set [`allowsAccessibilityAlternativeInputMethods`](aeassessmentconfiguration/allowsaccessibilityalternativeinputmethods.md) to `YES`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilityswitchcontrol)*