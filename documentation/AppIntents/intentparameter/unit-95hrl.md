# unit

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
final var unit: IntentParameter<Value>.Volume? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitVolume>`.

## See Also

### Accessing unit details
- [IntentParameter.Volume](./volume.md)
- [var defaultUnit: IntentParameter<Value>.Volume?](./defaultunit-2bsyg.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-903r6.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-9ln52.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/unit-95hrl)*