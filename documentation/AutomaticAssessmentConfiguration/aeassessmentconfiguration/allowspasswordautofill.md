# allowsPasswordAutoFill

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to allow password autofill during an assessment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var allowsPasswordAutoFill: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsPasswordAutoFill;
```

#### Discussion

Users can store passwords for use with Password Autofill by turning on the feature in the Settings app (General > Passwords > AutoFill Passwords). An assessment session disables Password Autofill by default, but you can allow it by setting [`allowsPasswordAutoFill`](./allowspasswordautofill.md) to `true` in the [`AEAssessmentConfiguration`](../aeassessmentconfiguration.md) instance that you use to initialize a session.

## See Also

### Allowing typing assistance
- [var allowsContinuousPathKeyboard: Bool](./allowscontinuouspathkeyboard.md)
  A Boolean value that indicates whether to allow Slide to Type to operate during an assessment.
- [var allowsKeyboardShortcuts: Bool](./allowskeyboardshortcuts.md)
  A Boolean value that indicates whether to allow keyboard shortcuts during an assessment.
- [var allowsPredictiveKeyboard: Bool](./allowspredictivekeyboard.md)
  A Boolean value that indicates whether to enable the predictive keyboard during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowspasswordautofill)*