# currency

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The ISO-4217 currency code for the country or region of the merchant’s principle place of business.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var currency: Locale.Currency { get set }
```

#### Discussion

Use the [`ISO-4217`](https://developer.apple.comhttps://www.iso.org/iso-4217-currency-codes.html) currency code that represents the location of the merchant’s principal place of business.

## See Also

- [var amount: Decimal](pkpaylaterview/amount-f3gs.md)
  The decimal value that represents the amount of the customer’s shopping cart or item pricing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylaterview/currency)*