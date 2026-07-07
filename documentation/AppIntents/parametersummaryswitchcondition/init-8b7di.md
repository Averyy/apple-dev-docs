# init(_:_:)

**Framework**: App Intents  
**Kind**: init

Creates a `Switch` statement that branches based on union value parameter cases.

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
init(_ keyPath: KeyPath<Intent, IntentParameter<Value>>, @ParameterSummaryCaseBuilder<Intent, Value.ValueType.Cases> _ builder: () -> CaseCondition) where Value : Sendable, Value.ValueType : AppUnionValue
```

## Parameters

- `keyPath`: Key path to the union value parameter
- `builder`: A result builder that constructs the case conditions


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummaryswitchcondition/init(_:_:)-8b7di)*