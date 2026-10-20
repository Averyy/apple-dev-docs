# IntentParameter.Temperature

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

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
enum Temperature
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitTemperature>`.

## Topics

### Enumeration Cases
- [IntentParameter.Temperature.celsius](./temperature/celsius.md)
- [IntentParameter.Temperature.fahrenheit](./temperature/fahrenheit.md)
- [IntentParameter.Temperature.kelvin](./temperature/kelvin.md)

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Temperature?](./unit-irv.md)
- [var defaultUnit: IntentParameter<Value>.Temperature?](./defaultunit-62blf.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-9bl77.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-2ca9l.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/temperature)*