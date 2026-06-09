# allowsAccessibilityAlternativeInputMethods

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow alternative input methods for accessibility features during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsAccessibilityAlternativeInputMethods: Bool { get set }
```

#### Discussion

When the Accessibility Keyboard or Switch Control is enabled, alternative input methods such as Dwell Control may be available. An assessment session disables these alternative input methods by default, but you can allow them by setting [`allowsAccessibilityAlternativeInputMethods`](aeassessmentconfiguration/allowsaccessibilityalternativeinputmethods.md) to `YES` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.

> **Note**: This property only takes effect when [`allowsAccessibilityKeyboard`](aeassessmentconfiguration/allowsaccessibilitykeyboard.md) or [`allowsAccessibilitySwitchControl`](aeassessmentconfiguration/allowsaccessibilityswitchcontrol.md) is `YES`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilityalternativeinputmethods)*