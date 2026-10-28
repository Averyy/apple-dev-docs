# allowsContinuousPathKeyboard

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to allow Slide to Type to operate during an assessment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var allowsContinuousPathKeyboard: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsContinuousPathKeyboard;
```

## Discussion

Users can turn on Slide to Type in the Settings app (General > Keyboard). An assessment session disables this feature by default, but you can allow it by setting [`allowsContinuousPathKeyboard`](./allowscontinuouspathkeyboard.md) to `true` in the [`AEAssessmentConfiguration`](../aeassessmentconfiguration.md) instance that you use to initialize a session.

## See Also

### Allowing typing assistance
- [var allowsKeyboardShortcuts: Bool](./allowskeyboardshortcuts.md)
  A Boolean value that indicates whether to allow keyboard shortcuts during an assessment.
- [var allowsPredictiveKeyboard: Bool](./allowspredictivekeyboard.md)
  A Boolean value that indicates whether to enable the predictive keyboard during an assessment.
- [var allowsPasswordAutoFill: Bool](./allowspasswordautofill.md)
  A Boolean value that indicates whether to allow password autofill during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowscontinuouspathkeyboard)*