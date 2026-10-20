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

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitMass>`.

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Mass?](./unit-15bj6.md)
- [IntentParameter.Mass](./mass.md)
- [var defaultUnit: IntentParameter<Value>.Mass?](./defaultunit-6a913.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-5kbp3.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/unitadjustforlocale-1lh4n)*