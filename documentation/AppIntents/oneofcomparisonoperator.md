# OneOfComparisonOperator

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

Operators that indicate the type of containment check for a conditional statement.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
enum OneOfComparisonOperator
```

## Topics

### Containment operators
- [OneOfComparisonOperator.oneOf](./oneofcomparisonoperator/oneof.md)
  An operator that determines if the parameter is equal to one of the values in the array.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Creating a conditional statement
- [init<Parameter>(KeyPath<Intent, Parameter>, HasValueComparisonOperator, () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28_,_,_,otherwise%29.md)
- [init<ValueType, Parameter>(KeyPath<Intent, Parameter>, ComparableComparisonOperator, ValueType, () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28_,_,_,_,otherwise%29-2aukt.md)
- [init<ValueType, Parameter>(KeyPath<Intent, Parameter>, EquatableComparisonOperator, ValueType, () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28_,_,_,_,otherwise%29-1u184.md)
- [init<ValueType, Parameter>(KeyPath<Intent, Parameter>, EquatableComparisonOperator, ValueType.ValueType, () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28_,_,_,_,otherwise%29-6edqt.md)
- [init<ValueType, Parameter>(KeyPath<Intent, Parameter>, OneOfComparisonOperator, [ValueType.ValueType], () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28_,_,_,_,otherwise%29-rfm5.md)
- [init<Value, Parameter>(KeyPath<Intent, Parameter>, ComparableComparisonOperator, Value.ValueType, () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28_,_,_,_,otherwise%29-3qvla.md)
- [init<Parameter>(KeyPath<Intent, Parameter>, identifier: ComparableComparisonOperator, Parameter.Value.ValueType.ID, () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28_,identifier,_,_,otherwise%29-215ub.md)
- [init<Parameter>(KeyPath<Intent, Parameter>, identifier: EquatableComparisonOperator, String, () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28_,identifier,_,_,otherwise%29-2yug9.md)
- [init<Parameter>(KeyPath<Intent, Parameter>, identifier: OneOfComparisonOperator, [Parameter.Value.ValueType.ID], () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28_,identifier,_,_,otherwise%29-3xth2.md)
- [init<IntentType, Parameter>(KeyPath<IntentType, Parameter>, identifier: ComparableComparisonOperator, Parameter.Value.ValueType.ID, () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28_,identifier,_,_,otherwise%29-4f45j.md)
- [init<Parameter>(KeyPath<Intent, Parameter>, identifier: StringComparisonOperator, String, () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28_,identifier,_,_,otherwise%29-5o5vc.md)
- [init<IntentType, Parameter>(KeyPath<IntentType, Parameter>, identifier: StringComparisonOperator, String, () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28_,identifier,_,_,otherwise%29-7g15l.md)
- [init<Parameter>(KeyPath<Intent, Parameter>, identifier: OneOfComparisonOperator, [String], () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28_,identifier,_,_,otherwise%29-7tayy.md)
- [init<Parameter>(KeyPath<Intent, Parameter>, identifier: EquatableComparisonOperator, Parameter.Value.ValueType.ID, () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28_,identifier,_,_,otherwise%29-9qlh.md)
- [init(widgetFamily: OneOfComparisonOperator, [IntentWidgetFamily], () -> WhenCondition, otherwise: () -> Otherwise)](./parametersummarywhencondition/init%28widgetfamily,_,_,otherwise%29-3fujn.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/oneofcomparisonoperator)*