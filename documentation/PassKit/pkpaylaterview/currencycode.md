# currencyCode

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A string that represents the ISO-4217 currency code for the country or region of the merchant’s principle place of business.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS 1.0+

> **Deprecated**: Apple Pay Later is deprecated.

## Declaration

```objc
@property (nonatomic, copy) NSString * currencyCode;
```

## Discussion

Use the [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) currency code string that represents the location of the merchant’s principal place of business.

## See Also

### Accessing information about the transaction
- [amount](./amount-1jzg2.md)
  The decimal value that represents the amount of the customer’s shopping cart or item pricing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylaterview/currencycode)*