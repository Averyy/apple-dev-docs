# init(amount:currency:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Creates a new Apple Pay Later visual merchandising widget view with the shopping cart amount and currency you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(amount: Decimal, currency: Locale.Currency)
```

## Parameters

- `amount`: The customer’s shopping cart or item pricing.
- `currency`: The   currency code for the country or region of the merchant’s principle place of business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylaterview/init(amount:currency:))*