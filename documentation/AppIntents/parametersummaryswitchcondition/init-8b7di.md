# init(_:_:)

**Framework**: App Intents  
**Kind**: init

Creates a `Switch` statement that branches based on union value parameter cases.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(_ keyPath: KeyPath<Intent, IntentParameter<Value>>, @ParameterSummaryCaseBuilder<Intent, Value.ValueType.Cases> _ builder: () -> CaseCondition) where Value : Sendable, Value.ValueType : AppUnionValue
```

## Parameters

- `keyPath`: Key path to the union value parameter
- `builder`: A result builder that constructs the case conditions


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummaryswitchcondition/init(_:_:)-8b7di)*