# IntentParameter.Power

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
enum Power
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitPower>`.

## Topics

### Enumeration Cases
- [IntentParameter.Power.femtowatts](./power/femtowatts.md)
- [IntentParameter.Power.gigawatts](./power/gigawatts.md)
- [IntentParameter.Power.horsepower](./power/horsepower.md)
- [IntentParameter.Power.kilowatts](./power/kilowatts.md)
- [IntentParameter.Power.megawatts](./power/megawatts.md)
- [IntentParameter.Power.microwatts](./power/microwatts.md)
- [IntentParameter.Power.milliwatts](./power/milliwatts.md)
- [IntentParameter.Power.nanowatts](./power/nanowatts.md)
- [IntentParameter.Power.picowatts](./power/picowatts.md)
- [IntentParameter.Power.terawatts](./power/terawatts.md)
- [IntentParameter.Power.watts](./power/watts.md)

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Power?](./unit-3mp17.md)
- [var defaultUnit: IntentParameter<Value>.Power?](./defaultunit-4fr1a.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-2if8y.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-hnv2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/power)*