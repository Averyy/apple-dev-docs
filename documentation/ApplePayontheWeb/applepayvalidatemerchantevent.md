# ApplePayValidateMerchantEvent

**Framework**: Apple Pay on the Web  
**Kind**: class  
**Role**: Class

An event object that contains the validation URL.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
interface ApplePayValidateMerchantEvent
```

## Mentions

- [Providing Merchant Validation](./providing-merchant-validation.md)

#### Overview

The event handler [`onvalidatemerchant`](./applepaysession/onvalidatemerchant.md) receives this event object when the payment sheet is displayed.

## Topics

### Accessing the Merchant Validation Event Attributes
- [validationURL](./applepayvalidatemerchantevent/validationurl.md)
  The URL your server must use to validate itself and obtain a merchant session object.

## See Also

### Getting merchant validation
- [begin](./applepaysession/begin.md)
  Begins the merchant validation process.
- [onvalidatemerchant](./applepaysession/onvalidatemerchant.md)
  An event handler the system calls when it displays the payment sheet.
- [completeMerchantValidation](./applepaysession/completemerchantvalidation.md)
  Completes the validation for a merchant session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayvalidatemerchantevent)*