# IntentParameter.ValueState

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

Indicates whether an IntentParameter was provided an initial value or if it was unset

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
enum ValueState
```

Available when `Value` conforms to `_IntentValue` and `Sendable`.

## Topics

### Enumeration Cases
- [IntentParameter.ValueState.set(_:)](./valuestate-swift.enum/set%28_%29.md)
  The parameter was provided an initial value.
- [IntentParameter.ValueState.unset](./valuestate-swift.enum/unset.md)
  The parameter was never provided a value

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)

## See Also

### Accessing the underlying value
- [let defaultValue: Value.UnwrappedType?](./defaultvalue.md)
- [var projectedValue: IntentParameter<Value>](./projectedvalue.md)
- [var wrappedValue: Value](./wrappedvalue.md)
- [var valueState: IntentParameter<Value>.ValueState](./valuestate-swift.property.md)
  Check if an IntentParameter was provided an initial value


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/valuestate-swift.enum)*