# allowsAutoFill

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow autofill during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsAutoFill: Bool { get set }
```

#### Discussion

Users can enable autofill in System Settings (Passwords > Password Options > AutoFill Passwords and Passkeys). An assessment session disables autofill by default, but you can allow it by setting [`allowsAutoFill`](aeassessmentconfiguration/allowsautofill.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsautofill)*