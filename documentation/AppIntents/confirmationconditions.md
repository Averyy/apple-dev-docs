# ConfirmationConditions

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

Conditions for a confirmation request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ConfirmationConditions
```

#### Overview

If any of the conditions are met, confirmation will be requested.

## Topics

### Type Properties
- [static let lowConfidenceSource: ConfirmationConditions](./confirmationconditions/lowconfidencesource.md)
  Only confirm if initiated from a low-confidence action source.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Disambiguation
- [struct IntentChoiceOption](./intentchoiceoption.md)
  A structure representing an entry in a list of options for a person to choose from before an app intent resumes its action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/confirmationconditions)*