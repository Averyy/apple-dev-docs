# IntentParameter.Energy

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
enum Energy
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitEnergy>`.

## Topics

### Enumeration Cases
- [IntentParameter.Energy.calories](./energy/calories.md)
- [IntentParameter.Energy.joules](./energy/joules.md)
- [IntentParameter.Energy.kilocalories](./energy/kilocalories.md)
- [IntentParameter.Energy.kilojoules](./energy/kilojoules.md)
- [IntentParameter.Energy.kilowattHours](./energy/kilowatthours.md)

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Energy?](./unit-91p3x.md)
- [var defaultUnit: IntentParameter<Value>.Energy?](./defaultunit-2n8ud.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-493zp.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-6p731.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/energy)*