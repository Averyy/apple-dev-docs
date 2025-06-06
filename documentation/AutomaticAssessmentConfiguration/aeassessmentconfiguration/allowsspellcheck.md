# allowsSpellCheck

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow spell check during an assessment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var allowsSpellCheck: Bool { get set }
```

#### Discussion

Users can activate the spell checker by turning on the Check Spelling feature in the Settings app (General > Keyboard). An assessment session disables spell checking by default, but you can allow it by setting [`allowsSpellCheck`](aeassessmentconfiguration/allowsspellcheck.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.

## See Also

- [var autocorrectMode: AEAssessmentConfiguration.AutocorrectMode](aeassessmentconfiguration/autocorrectmode-swift.property.md)
  A Boolean value that indicates whether to allow Autocorrect during an assessment.
- [AEAssessmentConfiguration.AutocorrectMode](aeassessmentconfiguration/autocorrectmode-swift.struct.md)
  The set of autocorrect features that you can enable during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsspellcheck)*