# allowsEmojiKeyboard

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow the emoji keyboard during an assessment.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
var allowsEmojiKeyboard: Bool { get set }
```

#### Discussion

Users can access the emoji keyboard by tapping the emoji button on the keyboard. An assessment session disables access to the emoji keyboard by default, but you can allow it by setting [`allowsEmojiKeyboard`](aeassessmentconfiguration/allowsemojikeyboard.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsemojikeyboard)*