# AEAutocorrectModeNone

**Framework**: Automatic Assessment Configuration  
**Kind**: case  
**Role**: Enumeration Case

A mode that indicates autocorrect doesn’t check anything.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS

## Declaration

```c
AEAutocorrectModeNone
```

## Discussion

Set the [`autocorrectMode`](../aeassessmentconfiguration/autocorrectmode-swift.property.md) value of an [`AEAssessmentConfiguration`](../aeassessmentconfiguration.md) instance to [`AEAutocorrectModeNone`](./aeautocorrectmodenone.md) to disable all autocorrect features during an assessment.

```objc
config.autocorrectMode = AEAutocorrectModeNone;
```

This is the default value of the [`autocorrectMode`](../aeassessmentconfiguration/autocorrectmode-swift.property.md) property.

## See Also

### Modes
- [static var punctuation: AEAssessmentConfiguration.AutocorrectMode](../aeassessmentconfiguration/autocorrectmode-swift.struct/punctuation.md)
  A mode in which autocorrect checks punctuation as the user types.
- [static var spelling: AEAssessmentConfiguration.AutocorrectMode](../aeassessmentconfiguration/autocorrectmode-swift.struct/spelling.md)
  A mode in which autocorrect checks for spelling as the user types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeautocorrectmode/aeautocorrectmodenone)*