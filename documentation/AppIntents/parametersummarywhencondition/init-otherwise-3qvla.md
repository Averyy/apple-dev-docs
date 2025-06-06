# init(_:_:_:_:otherwise:)

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
init<Value, Parameter>(_ keyPath: KeyPath<Intent, Parameter>, _ comparisonOperator: ComparableComparisonOperator, _ value: Value.ValueType, @ParameterSummaryBuilder<Intent> _ when: () -> WhenCondition, @ParameterSummaryBuilder<Intent> otherwise: () -> Otherwise) where Value : ExpressibleByNilLiteral, Value == Parameter.Value, Parameter : AnyIntentValue, Value.ValueType : Comparable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummarywhencondition/init(_:_:_:_:otherwise:)-3qvla)*