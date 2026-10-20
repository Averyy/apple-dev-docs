# IntentParameter.InclusiveRange

**Framework**: App Intents  
**Kind**: typealias  
**Role**: Type Alias

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
typealias InclusiveRange<Bound> = (lowerBound: Bound, upperBound: Bound) where Bound : Comparable
```

Available when `Value` conforms to `_IntentValue` and `Sendable`.

## See Also

### Accessing the configuration
- [var currencyCodes: [String]?](./currencycodes.md)
- [var inclusiveRange: IntentParameter<Value>.InclusiveRange<Decimal>?](./inclusiverange-swift.property.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/inclusiverange-swift.typealias)*