# init(_:_:_:_:otherwise:)

**Framework**: App Intents  
**Kind**: init

Creates a `When` condition checking if a union value parameter matches any case in a list.

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
init<ValueType, Parameter>(_ keyPath: KeyPath<Intent, Parameter>, _ comparisonOperator: OneOfComparisonOperator, _ values: [ValueType.ValueType.Cases], @ParameterSummaryBuilder<Intent> _ when: () -> WhenCondition, @ParameterSummaryBuilder<Intent> otherwise: () -> Otherwise) where ValueType == Parameter.Value, Parameter : AnyIntentValue, ValueType.ValueType : AppUnionValue
```

#### Discussion

Example:

```swift
When(\.$reaction, .oneOf, [.text, .emoji]) {
    Summary("Text-based reaction")
} otherwise: {
    Summary("Other reaction type")
}
```

## Parameters

- `keyPath`: Key path to the union value parameter
- `comparisonOperator`: The comparison operator (`.oneOf` or `.noneOf`)
- `values`: The array of union value cases to check against
- `when`: The summary to use when the condition is true
- `otherwise`: The summary to use when the condition is false


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummarywhencondition/init(_:_:_:_:otherwise:)-8d14d)*