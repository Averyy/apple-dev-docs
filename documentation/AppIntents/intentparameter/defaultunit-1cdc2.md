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
final var defaultUnit: IntentParameter<Value>.ElectricCharge? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitElectricCharge>`.

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.ElectricCharge?](./unit-81ehc.md)
- [IntentParameter.ElectricCharge](./electriccharge.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-2g1sv.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-3wgie.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/defaultunit-1cdc2)*