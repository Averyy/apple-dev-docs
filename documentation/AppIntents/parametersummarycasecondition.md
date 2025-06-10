# ParameterSummaryCaseCondition

**Framework**: App Intents  
**Kind**: struct

A type that represents an individual case of a switch statement in a parameter summary.

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
struct ParameterSummaryCaseCondition<Intent, Value, Summary> where Intent : AppIntent, Value : _IntentValue, Summary : ParameterSummary
```

## Topics

### Creating the case condition
- [init(Value, () -> Summary)](parametersummarycasecondition/init(_:_:)-3680j.md)
- [init([Value], () -> Summary)](parametersummarycasecondition/init(_:_:)-4029f.md)

## See Also

- [protocol ParameterSummary](parametersummary.md)
  An interface for defining the visual representation of an app intent’s parameters.
- [struct IntentParameterSummary](intentparametersummary.md)
  A type that describes the user interface configuration of an app intent’s parameters.
- [struct ParameterSummaryString](parametersummarystring.md)
  A human-readable string that interpolates parameter key paths to provide user-configurable placeholders in the Shortcuts app.
- [struct ParameterSummaryWhenCondition](parametersummarywhencondition.md)
  A type that represents a conditional statement in a parameter summary.
- [struct ParameterSummarySwitchCondition](parametersummaryswitchcondition.md)
  A type that represents a switch statement in a parameter summary.
- [struct ParameterSummaryDefaultCaseCondition](parametersummarydefaultcasecondition.md)
  A type that represents the default case of a switch statement in a parameter summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummarycasecondition)*