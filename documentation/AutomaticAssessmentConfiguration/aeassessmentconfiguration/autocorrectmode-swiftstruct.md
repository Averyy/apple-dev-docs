# AEAssessmentConfiguration.AutocorrectMode

**Framework**: Automatic Assessment Configuration  
**Kind**: struct

The set of autocorrect features that you can enable during an assessment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
struct AutocorrectMode
```

#### Overview

Use one or more of the autocorrect modes to set the [`autocorrectMode`](aeassessmentconfiguration/autocorrectmode-swift.property.md) property of an [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance. For example, you can enable both spelling and punctuation corrections by combining [`spelling`](aeassessmentconfiguration/autocorrectmode-swift.struct/spelling.md) and [`punctuation`](aeassessmentconfiguration/autocorrectmode-swift.struct/punctuation.md):

## Topics

### Creating a mode
- [init(rawValue: UInt)](aeassessmentconfiguration/autocorrectmode-swift.struct/init(rawvalue:).md)
  Creates a new mode instance.
### Modes
- [static var punctuation: AEAssessmentConfiguration.AutocorrectMode](aeassessmentconfiguration/autocorrectmode-swift.struct/punctuation.md)
  A mode in which autocorrect checks punctuation as the user types.
- [static var spelling: AEAssessmentConfiguration.AutocorrectMode](aeassessmentconfiguration/autocorrectmode-swift.struct/spelling.md)
  A mode in which autocorrect checks for spelling as the user types.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var allowsSpellCheck: Bool](aeassessmentconfiguration/allowsspellcheck.md)
  A Boolean value that indicates whether to allow spell check during an assessment.
- [var autocorrectMode: AEAssessmentConfiguration.AutocorrectMode](aeassessmentconfiguration/autocorrectmode-swift.property.md)
  A Boolean value that indicates whether to allow Autocorrect during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/autocorrectmode-swift.struct)*