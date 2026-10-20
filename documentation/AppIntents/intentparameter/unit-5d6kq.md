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
final var unit: IntentParameter<Value>.Illuminance? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitIlluminance>`.

## See Also

### Accessing unit details
- [IntentParameter.Illuminance](./illuminance.md)
- [var defaultUnit: IntentParameter<Value>.Illuminance?](./defaultunit-2j2ui.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-6mvvw.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-po5z.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/unit-5d6kq)*