# IntentParameter.Angle

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
enum Angle
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitAngle>`.

## Topics

### Enumeration Cases
- [IntentParameter.Angle.arcMinutes](./angle/arcminutes.md)
- [IntentParameter.Angle.arcSeconds](./angle/arcseconds.md)
- [IntentParameter.Angle.degrees](./angle/degrees.md)
- [IntentParameter.Angle.gradians](./angle/gradians.md)
- [IntentParameter.Angle.radians](./angle/radians.md)
- [IntentParameter.Angle.revolutions](./angle/revolutions.md)

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Angle?](./unit-egg9.md)
- [var defaultUnit: IntentParameter<Value>.Angle?](./defaultunit-9huqe.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-35m3l.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-9lff6.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/angle)*