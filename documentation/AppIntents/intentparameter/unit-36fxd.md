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
final var unit: IntentParameter<Value>.InformationStorage? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitInformationStorage>`.

## See Also

### Accessing unit details
- [IntentParameter.InformationStorage](./informationstorage.md)
- [var defaultUnit: IntentParameter<Value>.InformationStorage?](./defaultunit-ry6s.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-9qbxt.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-f41e.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/unit-36fxd)*