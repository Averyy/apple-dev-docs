# allowsAccessibilityKeyboard

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow alternative input methods in the Accessibility Keyboard during an assessment.

**Availability**:
- Mac Catalyst 26.1+
- macOS 26.1+

## Declaration

```swift
var allowsAccessibilityKeyboard: Bool { get set }
```

#### Discussion

Users can enable the Accessibility Keyboard in the Settings app (Accessibility > Keyboard > Accessibility Keyboard) to access an on-screen keyboard with alternative input methods. An assessment session disables alternative input methods in the Accessibility Keyboard by default, but you can allow them by setting [`allowsAccessibilityKeyboard`](aeassessmentconfiguration/allowsaccessibilitykeyboard.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilitykeyboard)*