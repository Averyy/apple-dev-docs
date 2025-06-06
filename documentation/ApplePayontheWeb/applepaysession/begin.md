# begin

**Framework**: Apple Pay on the Web  
**Kind**: method

Begins the merchant validation process.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
undefined begin();
```

## Mentions

- [Creating an Apple Pay Session](creating-an-apple-pay-session.md)

#### Discussion

When this method is called, the payment sheet is presented and the merchant validation process is initiated.

## See Also

- [onvalidatemerchant](applepaysession/onvalidatemerchant.md)
  An event handler the system calls when it displays the payment sheet.
- [completeMerchantValidation](applepaysession/completemerchantvalidation.md)
  Completes the validation for a merchant session.
- [ApplePayValidateMerchantEvent](applepayvalidatemerchantevent.md)
  An event object that contains the validation URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/begin)*