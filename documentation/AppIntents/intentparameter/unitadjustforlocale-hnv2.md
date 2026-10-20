# unitAdjustForLocale

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
final var unitAdjustForLocale: Bool? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitPower>`.

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Power?](./unit-3mp17.md)
- [IntentParameter.Power](./power.md)
- [var defaultUnit: IntentParameter<Value>.Power?](./defaultunit-4fr1a.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-2if8y.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/unitadjustforlocale-hnv2)*