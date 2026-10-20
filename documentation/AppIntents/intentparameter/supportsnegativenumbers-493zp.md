# supportsNegativeNumbers

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
final var supportsNegativeNumbers: Bool? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitEnergy>`.

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Energy?](./unit-91p3x.md)
- [IntentParameter.Energy](./energy.md)
- [var defaultUnit: IntentParameter<Value>.Energy?](./defaultunit-2n8ud.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-6p731.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/supportsnegativenumbers-493zp)*