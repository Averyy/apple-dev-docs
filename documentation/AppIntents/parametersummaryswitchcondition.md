# ParameterSummarySwitchCondition

**Framework**: App Intents  
**Kind**: struct

A type that represents a switch statement in a parameter summary.

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
struct ParameterSummarySwitchCondition<Intent, Value, CaseCondition> where Intent : AppIntent, Value : _IntentValue, CaseCondition : _ParameterSummarySwitchCase
```

## Topics

### Creating a switch condition
- [init(ParameterSummarySwitchCondition<Intent, Value, CaseCondition>.WidgetFamily, () -> CaseCondition)](parametersummaryswitchcondition/init(_:_:)-4vxvs.md)
  Initializes a parameter summary Switch statement over widget family.
- [init(KeyPath<Intent, IntentParameter<Value>>, () -> CaseCondition)](parametersummaryswitchcondition/init(_:_:)-6cdw3.md)
- [enum ParameterSummaryCaseBuilder](parametersummarycasebuilder.md)
  A result builder that allows you to declaratively describe the cases of a switch statement in a parameter summary.
- [ParameterSummarySwitchCondition.WidgetFamily](parametersummaryswitchcondition/widgetfamily.md)
  An enum that represents a parameter summary Switch statement over widget family.

## Relationships

### Conforms To
- [ParameterSummary](parametersummary.md)

## See Also

- [protocol ParameterSummary](parametersummary.md)
  An interface for defining the visual representation of an app intent’s parameters.
- [struct IntentParameterSummary](intentparametersummary.md)
  A type that describes the user interface configuration of an app intent’s parameters.
- [struct ParameterSummaryString](parametersummarystring.md)
  A human-readable string that interpolates parameter key paths to provide user-configurable placeholders in the Shortcuts app.
- [struct ParameterSummaryWhenCondition](parametersummarywhencondition.md)
  A type that represents a conditional statement in a parameter summary.
- [struct ParameterSummaryCaseCondition](parametersummarycasecondition.md)
  A type that represents an individual case of a switch statement in a parameter summary.
- [struct ParameterSummaryDefaultCaseCondition](parametersummarydefaultcasecondition.md)
  A type that represents the default case of a switch statement in a parameter summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummaryswitchcondition)*