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
final var unit: IntentParameter<Value>.Pressure? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitPressure>`.

## See Also

### Accessing unit details
- [IntentParameter.Pressure](./pressure.md)
- [var defaultUnit: IntentParameter<Value>.Pressure?](./defaultunit-4p4yh.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-83fjo.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-832oo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/unit-991uj)*