# allowsAccessibilityKeyboard

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow the Accessibility Keyboard during an assessment.

**Availability**:
- Mac Catalyst 26.1+
- macOS 26.1+

## Declaration

```swift
var allowsAccessibilityKeyboard: Bool { get set }
```

#### Discussion

Users can enable the Accessibility Keyboard in the Settings app (Accessibility > Keyboard > Accessibility Keyboard) to access an on-screen keyboard. An assessment session **does not** disable the Accessibility Keyboard by default, but you can disable it by setting [`allowsAccessibilityKeyboard`](aeassessmentconfiguration/allowsaccessibilitykeyboard.md) to `NO` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.

> **Note**: To allow the full Accessibility Keyboard with alternative input methods (such as Dwell Control), you must also set [`allowsAccessibilityAlternativeInputMethods`](aeassessmentconfiguration/allowsaccessibilityalternativeinputmethods.md) to `YES`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilitykeyboard)*