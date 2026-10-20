# IntentParameter.Pressure

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
enum Pressure
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitPressure>`.

## Topics

### Enumeration Cases
- [IntentParameter.Pressure.bars](./pressure/bars.md)
- [IntentParameter.Pressure.gigapascals](./pressure/gigapascals.md)
- [IntentParameter.Pressure.hectopascals](./pressure/hectopascals.md)
- [IntentParameter.Pressure.inchesOfMercury](./pressure/inchesofmercury.md)
- [IntentParameter.Pressure.kilopascals](./pressure/kilopascals.md)
- [IntentParameter.Pressure.megapascals](./pressure/megapascals.md)
- [IntentParameter.Pressure.millibars](./pressure/millibars.md)
- [IntentParameter.Pressure.millimetersOfMercury](./pressure/millimetersofmercury.md)
- [IntentParameter.Pressure.newtonsPerMetersSquared](./pressure/newtonspermeterssquared.md)
- [IntentParameter.Pressure.poundsForcePerSquareInch](./pressure/poundsforcepersquareinch.md)

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Pressure?](./unit-991uj.md)
- [var defaultUnit: IntentParameter<Value>.Pressure?](./defaultunit-4p4yh.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-83fjo.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-832oo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/pressure)*