# init(_:_:_:otherwise:)

**Framework**: App Intents  
**Kind**: init

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init<Parameter>(_ keyPath: KeyPath<Intent, Parameter>, _ comparisonOperator: HasValueComparisonOperator, @ParameterSummaryBuilder<Intent> _ when: () -> WhenCondition, @ParameterSummaryBuilder<Intent> otherwise: () -> Otherwise) where Parameter : AnyIntentValue
```

## See Also

- [enum EquatableComparisonOperator](equatablecomparisonoperator.md)
  Operators that indicate the type of equality check for a conditional statement.
- [enum ComparableComparisonOperator](comparablecomparisonoperator.md)
  Operators that indicate the type of comparison check for a conditional statement.
- [enum HasValueComparisonOperator](hasvaluecomparisonoperator.md)
  Operators that indicate the type of value check for a conditional statement.
- [enum OneOfComparisonOperator](oneofcomparisonoperator.md)
  Operators that indicate the type of containment check for a conditional statement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummarywhencondition/init(_:_:_:otherwise:))*