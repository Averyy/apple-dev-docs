# currencyCodes

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
final var currencyCodes: [String]? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `IntentCurrencyAmount`.

## See Also

### Accessing the configuration
- [var inclusiveRange: IntentParameter<Value>.InclusiveRange<Decimal>?](./inclusiverange-swift.property.md)
- [IntentParameter.InclusiveRange](./inclusiverange-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/currencycodes)*