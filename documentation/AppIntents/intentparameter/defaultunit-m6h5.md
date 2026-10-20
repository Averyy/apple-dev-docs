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
final var defaultUnit: IntentParameter<Value>.ElectricCurrent? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitElectricCurrent>`.

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.ElectricCurrent?](./unit-5prj2.md)
- [IntentParameter.ElectricCurrent](./electriccurrent.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-4hant.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-44r3e.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/defaultunit-m6h5)*