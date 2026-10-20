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

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitSpeed>`.

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Speed?](./unit-620ka.md)
- [IntentParameter.Speed](./speed.md)
- [var defaultUnit: IntentParameter<Value>.Speed?](./defaultunit-92l04.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-1bekt.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/unitadjustforlocale-8a31x)*