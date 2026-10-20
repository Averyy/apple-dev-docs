# supportsNegativeNumbers

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

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
final var supportsNegativeNumbers: Bool? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitLength>`.

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Length?](./unit-9xzg4.md)
- [IntentParameter.Length](./length.md)
- [var defaultUnit: IntentParameter<Value>.Length?](./defaultunit-2blhs.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-8ouwi.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/supportsnegativenumbers-1r83r)*