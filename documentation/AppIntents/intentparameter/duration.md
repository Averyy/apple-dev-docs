# IntentParameter.Duration

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
enum Duration
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitDuration>`.

## Topics

### Enumeration Cases
- [IntentParameter.Duration.hours](./duration/hours.md)
- [IntentParameter.Duration.microseconds](./duration/microseconds.md)
- [IntentParameter.Duration.milliseconds](./duration/milliseconds.md)
- [IntentParameter.Duration.minutes](./duration/minutes.md)
- [IntentParameter.Duration.nanoseconds](./duration/nanoseconds.md)
- [IntentParameter.Duration.picoseconds](./duration/picoseconds.md)
- [IntentParameter.Duration.seconds](./duration/seconds.md)

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Duration?](./unit-6yxwx.md)
- [var defaultUnit: IntentParameter<Value>.Duration?](./defaultunit-7lkkh.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-89ub3.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-2bek3.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/duration)*