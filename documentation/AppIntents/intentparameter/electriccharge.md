# IntentParameter.ElectricCharge

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
enum ElectricCharge
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitElectricCharge>`.

## Topics

### Enumeration Cases
- [IntentParameter.ElectricCharge.ampereHours](./electriccharge/amperehours.md)
- [IntentParameter.ElectricCharge.coulombs](./electriccharge/coulombs.md)
- [IntentParameter.ElectricCharge.kiloampereHours](./electriccharge/kiloamperehours.md)
- [IntentParameter.ElectricCharge.megaampereHours](./electriccharge/megaamperehours.md)
- [IntentParameter.ElectricCharge.microampereHours](./electriccharge/microamperehours.md)
- [IntentParameter.ElectricCharge.milliampereHours](./electriccharge/milliamperehours.md)

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.ElectricCharge?](./unit-81ehc.md)
- [var defaultUnit: IntentParameter<Value>.ElectricCharge?](./defaultunit-1cdc2.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-2g1sv.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-3wgie.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/electriccharge)*