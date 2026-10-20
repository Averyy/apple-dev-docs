# unit

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
final var unit: IntentParameter<Value>.Temperature? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitTemperature>`.

## See Also

### Accessing unit details
- [IntentParameter.Temperature](./temperature.md)
- [var defaultUnit: IntentParameter<Value>.Temperature?](./defaultunit-62blf.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-9bl77.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-2ca9l.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/unit-irv)*