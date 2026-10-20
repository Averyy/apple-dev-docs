# PKPayLater

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

Functions for validating information the framework displays in an Apple Pay Later visual merchandising widget.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS

> **Deprecated**: Apple Pay Later is deprecated.

## Declaration

```swift
@frozen
enum PKPayLater
```

## Topics

### Utilities
- [static func validate(amount: Decimal, currency: Locale.Currency) async -> Bool](./pkpaylater/validate%28amount,currency%29.md)
  Checks if the framework can display Apple Pay Later visual merchandising widget information for the given amount and currency.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylater)*