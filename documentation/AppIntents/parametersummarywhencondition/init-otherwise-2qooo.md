# init(_:_:_:_:otherwise:)

**Framework**: App Intents  
**Kind**: init

Creates a `When` condition comparing an optional union value parameter to a specific case.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init<ValueType, Parameter>(_ keyPath: KeyPath<Intent, Parameter>, _ comparisonOperator: EquatableComparisonOperator, _ value: ValueType.ValueType.Cases, @ParameterSummaryBuilder<Intent> _ when: () -> WhenCondition, @ParameterSummaryBuilder<Intent> otherwise: () -> Otherwise) where ValueType : ExpressibleByNilLiteral, ValueType == Parameter.Value, Parameter : AnyIntentValue, ValueType.ValueType : AppUnionValue
```

## Parameters

- `keyPath`: Key path to the optional union value parameter
- `comparisonOperator`: The comparison operator (`.equalTo` or `.notEqualTo`)
- `value`: The union value case to compare against
- `when`: The summary to use when the condition is true
- `otherwise`: The summary to use when the condition is false


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummarywhencondition/init(_:_:_:_:otherwise:)-2qooo)*