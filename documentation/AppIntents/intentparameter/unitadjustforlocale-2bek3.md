# unitAdjustForLocale

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

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
final var unitAdjustForLocale: Bool? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitDuration>`.

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Duration?](./unit-6yxwx.md)
- [IntentParameter.Duration](./duration.md)
- [var defaultUnit: IntentParameter<Value>.Duration?](./defaultunit-7lkkh.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-89ub3.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/unitadjustforlocale-2bek3)*