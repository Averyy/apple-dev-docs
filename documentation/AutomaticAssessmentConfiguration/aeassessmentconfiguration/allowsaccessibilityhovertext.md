# allowsAccessibilityHoverText

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow Hover Text during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsAccessibilityHoverText: Bool { get set }
```

#### Discussion

Users can enable Hover Text in the Settings app (Accessibility > Zoom > Hover Text) to magnify text under the pointer. An assessment session **does not** disable Hover Text by default, but you can disable it by setting [`allowsAccessibilityHoverText`](aeassessmentconfiguration/allowsaccessibilityhovertext.md) to `NO` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilityhovertext)*