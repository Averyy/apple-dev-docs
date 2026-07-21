# allowsAccessibilityFullKeyboardAccess

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow Full Keyboard Access during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsAccessibilityFullKeyboardAccess: Bool { get set }
```

#### Discussion

Users can enable Full Keyboard Access in the Settings app (Accessibility > Keyboard > Full Keyboard Access) to navigate and operate the system using only the keyboard. An assessment session **does not** disable Full Keyboard Access by default, but you can disable it by setting [`allowsAccessibilityFullKeyboardAccess`](aeassessmentconfiguration/allowsaccessibilityfullkeyboardaccess.md) to `NO` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilityfullkeyboardaccess)*