# ParameterSummary

**Framework**: App Intents  
**Kind**: protocol

An interface for defining the visual representation of an app intent’s parameters.

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
protocol ParameterSummary
```

#### Overview

For more information about using parameters and providing a parameter summary, see [`Provide an interactive parameter summary for your intent`](adding-parameters-to-an-app-intent#Provide-an-interactive-parameter-summary-for-your-intent.md).

## Topics

### Associated Types
- [associatedtype Intent : AppIntent](parametersummary/intent.md)

## Relationships

### Conforming Types
- [IntentParameterSummary](intentparametersummary.md)
- [ParameterSummarySwitchCondition](parametersummaryswitchcondition.md)
- [ParameterSummaryWhenCondition](parametersummarywhencondition.md)

## See Also

- [struct IntentParameterSummary](intentparametersummary.md)
  A type that describes the user interface configuration of an app intent’s parameters.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummary)*