# supportsNegativeNumbers

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
final var supportsNegativeNumbers: Bool? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitArea>`.

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Area?](./unit-42nhg.md)
- [IntentParameter.Area](./area.md)
- [var defaultUnit: IntentParameter<Value>.Area?](./defaultunit-9sm2x.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-8xbaf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/supportsnegativenumbers-38cqc)*