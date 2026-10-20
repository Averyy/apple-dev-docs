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
final var defaultUnit: IntentParameter<Value>.Frequency? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitFrequency>`.

## See Also

### Accessing unit details
- [var unit: IntentParameter<Value>.Frequency?](./unit-69agf.md)
- [IntentParameter.Frequency](./frequency.md)
- [var supportsNegativeNumbers: Bool?](./supportsnegativenumbers-8i8i1.md)
- [var unitAdjustForLocale: Bool?](./unitadjustforlocale-52v1p.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/defaultunit-61co5)*