# amount

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The decimal value that represents the amount of the customer’s shopping cart or item pricing.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS

> **Deprecated**: Apple Pay Later is deprecated.

## Declaration

```swift
@MainActor
@preconcurrency var amount: Decimal { get set }
```

## See Also

### Accessing information about the transaction
- [var currency: Locale.Currency](./currency.md)
  The ISO-4217 currency code for the country or region of the merchant’s principle place of business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylaterview/amount-f3gs)*