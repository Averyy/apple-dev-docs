# HasValueComparisonOperator

**Framework**: App Intents  
**Kind**: enum

Operators that indicate the type of value check for a conditional statement.

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
enum HasValueComparisonOperator
```

## Topics

### Value operators
- [HasValueComparisonOperator.hasAnyValue](hasvaluecomparisonoperator/hasanyvalue.md)
  An operator that determines if the parameter has a value.
- [HasValueComparisonOperator.hasNoValue](hasvaluecomparisonoperator/hasnovalue.md)
  An operator that determines if the parameter’s empty.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/hasvaluecomparisonoperator)*