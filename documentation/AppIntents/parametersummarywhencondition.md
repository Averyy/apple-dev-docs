# ParameterSummaryWhenCondition

**Framework**: App Intents  
**Kind**: struct

A type that represents a conditional statement in a parameter summary.

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
struct ParameterSummaryWhenCondition<Intent, WhenCondition, Otherwise> where Intent : AppIntent, WhenCondition : ParameterSummary, Otherwise : ParameterSummary
```

## Topics

### Creating a conditional statement
- [init<Parameter>(KeyPath<Intent, Parameter>, HasValueComparisonOperator, () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:_:_:otherwise:).md)
- [init<ValueType, Parameter>(KeyPath<Intent, Parameter>, ComparableComparisonOperator, ValueType, () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:_:_:_:otherwise:)-2aukt.md)
- [init<ValueType, Parameter>(KeyPath<Intent, Parameter>, EquatableComparisonOperator, ValueType, () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:_:_:_:otherwise:)-1u184.md)
- [init<ValueType, Parameter>(KeyPath<Intent, Parameter>, EquatableComparisonOperator, ValueType.ValueType, () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:_:_:_:otherwise:)-6edqt.md)
- [init<ValueType, Parameter>(KeyPath<Intent, Parameter>, OneOfComparisonOperator, [ValueType.ValueType], () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:_:_:_:otherwise:)-rfm5.md)
- [init<Value, Parameter>(KeyPath<Intent, Parameter>, ComparableComparisonOperator, Value.ValueType, () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:_:_:_:otherwise:)-3qvla.md)
- [init<Parameter>(KeyPath<Intent, Parameter>, identifier: ComparableComparisonOperator, Parameter.Value.ValueType.ID, () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:identifier:_:_:otherwise:)-215ub.md)
- [init<Parameter>(KeyPath<Intent, Parameter>, identifier: EquatableComparisonOperator, String, () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:identifier:_:_:otherwise:)-2yug9.md)
- [init<Parameter>(KeyPath<Intent, Parameter>, identifier: OneOfComparisonOperator, [Parameter.Value.ValueType.ID], () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:identifier:_:_:otherwise:)-3xth2.md)
- [init<IntentType, Parameter>(KeyPath<IntentType, Parameter>, identifier: ComparableComparisonOperator, Parameter.Value.ValueType.ID, () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:identifier:_:_:otherwise:)-4f45j.md)
- [init<Parameter>(KeyPath<Intent, Parameter>, identifier: StringComparisonOperator, String, () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:identifier:_:_:otherwise:)-5o5vc.md)
- [init<IntentType, Parameter>(KeyPath<IntentType, Parameter>, identifier: StringComparisonOperator, String, () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:identifier:_:_:otherwise:)-7g15l.md)
- [init<Parameter>(KeyPath<Intent, Parameter>, identifier: OneOfComparisonOperator, [String], () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:identifier:_:_:otherwise:)-7tayy.md)
- [init<Parameter>(KeyPath<Intent, Parameter>, identifier: EquatableComparisonOperator, Parameter.Value.ValueType.ID, () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(_:identifier:_:_:otherwise:)-9qlh.md)
- [init(widgetFamily: OneOfComparisonOperator, [IntentWidgetFamily], () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(widgetfamily:_:_:otherwise:)-3fujn.md)
- [init(widgetFamily: EquatableComparisonOperator, IntentWidgetFamily, () -> WhenCondition, otherwise: () -> Otherwise)](parametersummarywhencondition/init(widgetfamily:_:_:otherwise:)-9l1to.md)
- [enum EquatableComparisonOperator](equatablecomparisonoperator.md)
  Operators that indicate the type of equality check for a conditional statement.
- [enum ComparableComparisonOperator](comparablecomparisonoperator.md)
  Operators that indicate the type of comparison check for a conditional statement.
- [enum HasValueComparisonOperator](hasvaluecomparisonoperator.md)
  Operators that indicate the type of value check for a conditional statement.
- [enum OneOfComparisonOperator](oneofcomparisonoperator.md)
  Operators that indicate the type of containment check for a conditional statement.

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
- [struct ParameterSummarySwitchCondition](parametersummaryswitchcondition.md)
  A type that represents a switch statement in a parameter summary.
- [struct ParameterSummaryCaseCondition](parametersummarycasecondition.md)
  A type that represents an individual case of a switch statement in a parameter summary.
- [struct ParameterSummaryDefaultCaseCondition](parametersummarydefaultcasecondition.md)
  A type that represents the default case of a switch statement in a parameter summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummarywhencondition)*