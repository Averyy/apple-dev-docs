# IntentParameter.ElectricCurrent

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
enum ElectricCurrent
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitElectricCurrent>`.

## Topics

### Enumeration Cases
- [IntentParameter.ElectricCurrent.amperes](./electriccurrent/amperes.md)
- [IntentParameter.ElectricCurrent.kiloamperes](./electriccurrent/kiloamperes.md)
- [IntentParameter.ElectricCurrent.megaamperes](./electriccurrent/megaamperes.md)
- [IntentParameter.ElectricCurrent.microamperes](./electriccurrent/microamperes.md)
- [IntentParameter.ElectricCurrent.milliamperes](./electriccurrent/milliamperes.md)

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.ElectricCurrent?](./unit-5prj2.md)
- [var defaultUnit: IntentParameter<Value>.ElectricCurrent?](./defaultunit-m6h5.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-4hant.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-44r3e.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/electriccurrent)*