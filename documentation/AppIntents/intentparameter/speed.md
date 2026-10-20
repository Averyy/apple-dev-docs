# IntentParameter.Speed

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
enum Speed
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitSpeed>`.

## Topics

### Enumeration Cases
- [IntentParameter.Speed.kilometersPerHour](./speed/kilometersperhour.md)
- [IntentParameter.Speed.knots](./speed/knots.md)
- [IntentParameter.Speed.metersPerSecond](./speed/meterspersecond.md)
- [IntentParameter.Speed.milesPerHour](./speed/milesperhour.md)

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Speed?](./unit-620ka.md)
- [var defaultUnit: IntentParameter<Value>.Speed?](./defaultunit-92l04.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-1bekt.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-8a31x.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/speed)*