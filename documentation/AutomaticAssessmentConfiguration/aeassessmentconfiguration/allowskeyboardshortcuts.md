# allowsKeyboardShortcuts

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow keyboard shortcuts during an assessment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var allowsKeyboardShortcuts: Bool { get set }
```

#### Discussion

Users can add Keyboard Shortcuts in the Settings app (General > Keyboard > Text Replacement). An assessment session disables the use of keyboard shortcuts by default, but you can allow them by setting [`allowsKeyboardShortcuts`](aeassessmentconfiguration/allowskeyboardshortcuts.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.

## See Also

- [var allowsContinuousPathKeyboard: Bool](aeassessmentconfiguration/allowscontinuouspathkeyboard.md)
  A Boolean value that indicates whether to allow Slide to Type to operate during an assessment.
- [var allowsPredictiveKeyboard: Bool](aeassessmentconfiguration/allowspredictivekeyboard.md)
  A Boolean value that indicates whether to enable the predictive keyboard during an assessment.
- [var allowsPasswordAutoFill: Bool](aeassessmentconfiguration/allowspasswordautofill.md)
  A Boolean value that indicates whether to allow password autofill during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowskeyboardshortcuts)*