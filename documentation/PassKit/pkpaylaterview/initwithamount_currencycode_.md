# initWithAmount:currencyCode:

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Creates a new Apple Pay Later visual merchandising widget view with the amount and currency code you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS 1.0+

> **Deprecated**: Apple Pay Later is deprecated.

## Declaration

```objc
- (instancetype) initWithAmount:(NSDecimalNumber *) amount currencyCode:(NSString *) currencyCode;
```

## Parameters

- `amount`: The customer’s shopping cart or item pricing.
- `currencyCode`: The string that represents the [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) currency code for the country or region of the merchant’s principle place of business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylaterview/initwithamount:currencycode:)*