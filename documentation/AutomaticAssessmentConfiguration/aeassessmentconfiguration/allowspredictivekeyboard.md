# allowsPredictiveKeyboard

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to enable the predictive keyboard during an assessment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var allowsPredictiveKeyboard: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsPredictiveKeyboard;
```

#### Discussion

Users can turn on the Predictive Keyboard feature in the Settings app (General > Keyboard). An assessment session disables this feature by default, but you can allow it by setting [`allowsPredictiveKeyboard`](./allowspredictivekeyboard.md) to `true` in the [`AEAssessmentConfiguration`](../aeassessmentconfiguration.md) instance that you use to initialize a session.

## See Also

### Allowing typing assistance
- [var allowsContinuousPathKeyboard: Bool](./allowscontinuouspathkeyboard.md)
  A Boolean value that indicates whether to allow Slide to Type to operate during an assessment.
- [var allowsKeyboardShortcuts: Bool](./allowskeyboardshortcuts.md)
  A Boolean value that indicates whether to allow keyboard shortcuts during an assessment.
- [var allowsPasswordAutoFill: Bool](./allowspasswordautofill.md)
  A Boolean value that indicates whether to allow password autofill during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowspredictivekeyboard)*