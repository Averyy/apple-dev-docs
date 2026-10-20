# valueState

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

Check if an IntentParameter was provided an initial value

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
final var valueState: IntentParameter<Value>.ValueState { get }
```

Available when `Value` conforms to `_IntentValue` and `Sendable`.

## See Also

### Accessing the underlying value
- [let defaultValue: Value.UnwrappedType?](./defaultvalue.md)
- [var projectedValue: IntentParameter<Value>](./projectedvalue.md)
- [var wrappedValue: Value](./wrappedvalue.md)
- [IntentParameter.ValueState](./valuestate-swift.enum.md)
  Indicates whether an IntentParameter was provided an initial value or if it was unset


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/valuestate-swift.property)*