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
final var unit: IntentParameter<Value>.ConcentrationMass? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitConcentrationMass>`.

## See Also

### Accessing unit details
- [IntentParameter.ConcentrationMass](./concentrationmass.md)
- [var defaultUnit: IntentParameter<Value>.ConcentrationMass?](./defaultunit-6mid8.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-5s36k.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-831sz.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/unit-4ukvz)*