# IntentParameter.ValueState

**Framework**: App Intents  
**Kind**: enum

Indicates whether an IntentParameter was provided an initial value or if it was unset

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst ?+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
enum ValueState
```

## Topics

### Enumeration Cases
- [IntentParameter.ValueState.set(_:)](intentparameter/valuestate-swift.enum/set(_:).md)
  The parameter was provided an initial value.
- [IntentParameter.ValueState.unset](intentparameter/valuestate-swift.enum/unset.md)
  The parameter was never provided a value

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [let defaultValue: Value.UnwrappedType?](intentparameter/defaultvalue.md)
- [var projectedValue: IntentParameter<Value>](intentparameter/projectedvalue.md)
- [var wrappedValue: Value](intentparameter/wrappedvalue.md)
- [var valueState: IntentParameter<Value>.ValueState](intentparameter/valuestate-swift.property.md)
  Check if an IntentParameter was provided an initial value


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/valuestate-swift.enum)*