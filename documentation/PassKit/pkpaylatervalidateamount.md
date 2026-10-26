# PKPayLaterValidateAmount

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: func  
**Role**: Function

Checks if the framework can display Apple Pay Later visual merchandising widget information for the given amount and currency.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS 1.0+

> **Deprecated**: Apple Pay Later is deprecated.

## Declaration

```c
extern void PKPayLaterValidateAmount(NSDecimalNumber *amount, NSString *currencyCode, void (^completion)(BOOL eligible));
```

## Parameters

- `amount`: The customer’s cart price or item pricing.
- `currencyCode`: The [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) currency code for the country or region of the merchant’s principle place of business.
- `completion`: The block the framework calls after calculating the eligibility result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylatervalidateamount)*