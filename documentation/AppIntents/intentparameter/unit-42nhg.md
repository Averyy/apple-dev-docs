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
final var unit: IntentParameter<Value>.Area? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitArea>`.

## See Also

### Accessing unit details
- [IntentParameter.Area](./area.md)
- [var defaultUnit: IntentParameter<Value>.Area?](./defaultunit-9sm2x.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-38cqc.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-8xbaf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/unit-42nhg)*