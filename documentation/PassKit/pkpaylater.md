# PKPayLater

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

Functions for validating information the framework displays in an Apple Pay Later visual merchandising widget.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS ?+

## Declaration

```swift
@frozen
enum PKPayLater
```

## Topics

### Utilities
- [static func validate(amount: Decimal, currency: Locale.Currency) async -> Bool](pkpaylater/validate(amount:currency:).md)
  Checks if the framework can display Apple Pay Later visual merchandising widget information for the given amount and currency.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylater)*