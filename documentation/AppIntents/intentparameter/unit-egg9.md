# unit

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

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
final var unit: IntentParameter<Value>.Angle? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitAngle>`.

## See Also

### Accessing unit details
- [IntentParameter.Angle](./angle.md)
- [var defaultUnit: IntentParameter<Value>.Angle?](./defaultunit-9huqe.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-35m3l.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-9lff6.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/unit-egg9)*