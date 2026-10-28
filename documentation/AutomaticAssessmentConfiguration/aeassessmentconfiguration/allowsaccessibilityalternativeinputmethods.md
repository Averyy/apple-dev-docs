# allowsAccessibilityAlternativeInputMethods

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to allow alternative input methods for accessibility features during an assessment.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var allowsAccessibilityAlternativeInputMethods: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsAccessibilityAlternativeInputMethods;
```

## Discussion

When the Accessibility Keyboard or Switch Control is enabled, alternative input methods such as Dwell Control may be available. An assessment session disables these alternative input methods by default, but you can allow them by setting [`allowsAccessibilityAlternativeInputMethods`](./allowsaccessibilityalternativeinputmethods.md) to `YES` in the [`AEAssessmentConfiguration`](../aeassessmentconfiguration.md) instance that you use to initialize a session.

> **Note**: This property only takes effect when [`allowsAccessibilityKeyboard`](./allowsaccessibilitykeyboard.md) or [`allowsAccessibilitySwitchControl`](./allowsaccessibilityswitchcontrol.md) is `YES`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilityalternativeinputmethods)*