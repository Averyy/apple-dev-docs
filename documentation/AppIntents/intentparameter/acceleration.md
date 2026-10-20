# IntentParameter.Acceleration

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
enum Acceleration
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitAcceleration>`.

## Topics

### Enumeration Cases
- [IntentParameter.Acceleration.gravity](./acceleration/gravity.md)
- [IntentParameter.Acceleration.metersPerSecondSquared](./acceleration/meterspersecondsquared.md)

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Acceleration?](./unit-4kgwq.md)
- [var defaultUnit: IntentParameter<Value>.Acceleration?](./defaultunit-6s3bu.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-8d17e.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-2jck9.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/acceleration)*