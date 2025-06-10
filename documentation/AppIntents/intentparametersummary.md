# IntentParameterSummary

**Framework**: App Intents  
**Kind**: struct

A type that describes the user interface configuration of an app intent’s parameters.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct IntentParameterSummary<Intent> where Intent : AppIntent
```

## Topics

### Crearing a parameter summary
- [init()](intentparametersummary/init.md)
- [init(() -> [PartialKeyPath<Intent>])](intentparametersummary/init(_:).md)
- [init(ParameterSummaryString<Intent>, table: String?)](intentparametersummary/init(_:table:).md)
- [init(ParameterSummaryString<Intent>, table: String?, () -> [PartialKeyPath<Intent>])](intentparametersummary/init(_:table:_:).md)
### Building the parameter key paths
- [IntentParameterSummary.ParameterKeyPathsBuilder](intentparametersummary/parameterkeypathsbuilder.md)
  A result builder that declaratively builds the path to a parameter.

## Relationships

### Conforms To
- [ParameterSummary](parametersummary.md)

## See Also

- [protocol ParameterSummary](parametersummary.md)
  An interface for defining the visual representation of an app intent’s parameters.
- [struct ParameterSummaryString](parametersummarystring.md)
  A human-readable string that interpolates parameter key paths to provide user-configurable placeholders in the Shortcuts app.
- [struct ParameterSummaryWhenCondition](parametersummarywhencondition.md)
  A type that represents a conditional statement in a parameter summary.
- [struct ParameterSummarySwitchCondition](parametersummaryswitchcondition.md)
  A type that represents a switch statement in a parameter summary.
- [struct ParameterSummaryCaseCondition](parametersummarycasecondition.md)
  A type that represents an individual case of a switch statement in a parameter summary.
- [struct ParameterSummaryDefaultCaseCondition](parametersummarydefaultcasecondition.md)
  A type that represents the default case of a switch statement in a parameter summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparametersummary)*