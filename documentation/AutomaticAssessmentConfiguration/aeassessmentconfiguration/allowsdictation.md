# allowsDictation

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to allow the use of dictation during an assessment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var allowsDictation: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsDictation;
```

## Discussion

By turning on Enable Dictation (General > Keyboard in the Settings app on iOS and iPadOS), users can speak into their device and have the words they speak converted to text. An assessment session disables this feature by default, but you can allow it by setting [`allowsDictation`](./allowsdictation.md) to `true` in the [`AEAssessmentConfiguration`](../aeassessmentconfiguration.md) instance that you use to initialize a session.

## See Also

### Allowing accessibility
- [var allowsAccessibilitySpeech: Bool](./allowsaccessibilityspeech.md)
  A Boolean value that indicates whether to allow the speech-related accessibility features during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsdictation)*