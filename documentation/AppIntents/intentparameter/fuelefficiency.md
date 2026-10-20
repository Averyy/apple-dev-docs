# IntentParameter.FuelEfficiency

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
enum FuelEfficiency
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitFuelEfficiency>`.

## Topics

### Enumeration Cases
- [IntentParameter.FuelEfficiency.litersPer100Kilometers](./fuelefficiency/litersper100kilometers.md)
- [IntentParameter.FuelEfficiency.milesPerGallon](./fuelefficiency/milespergallon.md)
- [IntentParameter.FuelEfficiency.milesPerImperialGallon](./fuelefficiency/milesperimperialgallon.md)

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.FuelEfficiency?](./unit-3ek73.md)
- [var defaultUnit: IntentParameter<Value>.FuelEfficiency?](./defaultunit-2u2qw.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-6wblf.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-322mt.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/fuelefficiency)*