# autocorrectMode

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow Autocorrect during an assessment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var autocorrectMode: AEAssessmentConfiguration.AutocorrectMode { get set }
```

#### Discussion

Users can turn on autocorrect in the Settings app (General > Keyboard > Auto-Correction). An assessment session disables this feature by default, but you can allow it by setting [`autocorrectMode`](aeassessmentconfiguration/autocorrectmode-swift.property.md) in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session. Set the mode’s value to some combination of the the values from the [`AEAssessmentConfiguration.AutocorrectMode`](aeassessmentconfiguration/autocorrectmode-swift.struct.md) structure.

## See Also

- [var allowsSpellCheck: Bool](aeassessmentconfiguration/allowsspellcheck.md)
  A Boolean value that indicates whether to allow spell check during an assessment.
- [AEAssessmentConfiguration.AutocorrectMode](aeassessmentconfiguration/autocorrectmode-swift.struct.md)
  The set of autocorrect features that you can enable during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/autocorrectmode-swift.property)*