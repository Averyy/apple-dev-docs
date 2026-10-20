# defaultUnit

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
final var defaultUnit: IntentParameter<Value>.ElectricResistance? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitElectricResistance>`.

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.ElectricResistance?](./unit-670ic.md)
- [IntentParameter.ElectricResistance](./electricresistance.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-8gwi5.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-14ddy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/defaultunit-4mrsv)*