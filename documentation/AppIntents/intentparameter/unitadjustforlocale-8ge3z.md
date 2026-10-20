# unitAdjustForLocale

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
final var unitAdjustForLocale: Bool? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitDispersion>`.

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Dispersion?](./unit-9rnvi.md)
- [IntentParameter.Dispersion](./dispersion.md)
- [var defaultUnit: IntentParameter<Value>.Dispersion?](./defaultunit-tk2s.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-1bmpc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/unitadjustforlocale-8ge3z)*